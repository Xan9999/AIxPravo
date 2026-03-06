"""
Legal Chatbot with Context-Aware Reasoning and Citation
"""
import json
import os
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from openai import OpenAI
import numpy as np
from sentence_transformers import SentenceTransformer

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not required if env vars are set manually


@dataclass
class LegalDocument:
    """Represents a legal document with metadata"""
    id: str
    title: str
    content: str
    source: str
    jurisdiction: Optional[str] = None
    
    
@dataclass
class Citation:
    """Represents a citation to a legal document"""
    document_id: str
    document_title: str
    excerpt: str
    relevance_score: float


@dataclass
class Response:
    """Chatbot response with reasoning and citations"""
    answer: str
    reasoning: str
    citations: List[Citation]
    confidence: float


class LegalKnowledgeBase:
    """Manages legal documents and retrieval with vector search"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.documents: Dict[str, LegalDocument] = {}
        self.embeddings: Dict[str, np.ndarray] = {}
        # Use a lightweight, fast embedding model
        print("Loading embedding model...")
        self.encoder = SentenceTransformer(model_name)
        print("✓ Embedding model loaded")
    
    def add_document(self, doc: LegalDocument):
        """Add a legal document to the knowledge base and compute its embedding"""
        self.documents[doc.id] = doc
        # Create embedding from title + content for better semantic matching
        text = f"{doc.title}. {doc.content}"
        self.embeddings[doc.id] = self.encoder.encode(text, convert_to_numpy=True)
    
    def search(self, query: str, top_k: int = 3) -> List[tuple[LegalDocument, float]]:
        """Vector-based semantic search using cosine similarity"""
        if not self.documents:
            return []
        
        # Encode the query
        query_embedding = self.encoder.encode(query, convert_to_numpy=True)
        
        # Calculate cosine similarity with all documents
        results = []
        for doc_id, doc_embedding in self.embeddings.items():
            # Cosine similarity
            similarity = np.dot(query_embedding, doc_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
            )
            results.append((self.documents[doc_id], float(similarity)))
        
        # Sort by similarity (highest first)
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]


class LegalChatbot:
    """Main chatbot with reasoning and citation capabilities"""
    
    def __init__(self, knowledge_base: LegalKnowledgeBase, api_key: Optional[str] = None):
        self.kb = knowledge_base
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("MODEL", "gpt-4o-mini")  # Default to cheapest model
    
    def answer(self, question: str) -> Response:
        """Generate answer with reasoning and citations using AI"""
        # Parse and understand the question
        parsed_query = self._parse_question(question)
        
        # Retrieve relevant documents
        relevant_docs = self.kb.search(parsed_query)
        
        if not relevant_docs:
            return Response(
                answer="I don't have sufficient legal documents to answer this question.",
                reasoning="No relevant legal documents found in the knowledge base.",
                citations=[],
                confidence=0.0
            )
        
        # Build citations
        citations = []
        context_parts = []
        
        for doc, score in relevant_docs:
            excerpt = self._extract_relevant_excerpt(doc.content, question)
            citations.append(Citation(
                document_id=doc.id,
                document_title=doc.title,
                excerpt=excerpt,
                relevance_score=score  # Already 0-1 from cosine similarity
            ))
            context_parts.append(f"[{doc.title}]: {doc.content}")
        
        # Use AI to generate answer with reasoning
        context = "\n\n".join(context_parts)
        ai_response = self._generate_ai_response(question, context)
        
        # Calculate confidence based on document relevance (similarity is 0-1)
        confidence = relevant_docs[0][1] if relevant_docs else 0.0
        
        return Response(
            answer=ai_response["answer"],
            reasoning=ai_response["reasoning"],
            citations=citations,
            confidence=confidence
        )
    
    def _parse_question(self, question: str) -> str:
        """Use AI to parse and extract key legal concepts from question"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Extract key legal concepts and search terms from the user's question. Return only the enhanced search query."},
                    {"role": "user", "content": question}
                ],
                temperature=0.3,
                max_tokens=100
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"AI parsing failed: {e}. Using original question.")
            return question
    
    def _generate_ai_response(self, question: str, context: str) -> Dict[str, str]:
        """Use AI to generate answer and reasoning from legal context"""
        try:
            prompt = f"""You are a legal assistant. Based on the provided legal documents, answer the question with clear reasoning.

Legal Documents:
{context}

Question: {question}

Provide your response in JSON format with two fields:
1. "reasoning": Explain your logical process, which documents you used, and why
2. "answer": A clear, accurate answer citing specific legal principles

Be precise and cite specific parts of the documents."""

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a legal research assistant. Provide accurate, well-reasoned answers based on provided legal documents."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=800,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            return {
                "answer": result.get("answer", "Unable to generate answer"),
                "reasoning": result.get("reasoning", "Unable to generate reasoning")
            }
        except Exception as e:
            print(f"AI generation failed: {e}")
            return {
                "answer": "Error generating AI response. Please check your API key and connection.",
                "reasoning": f"AI processing error: {str(e)}"
            }
    
    def _extract_relevant_excerpt(self, content: str, query: str, max_length: int = 200) -> str:
        """Extract most relevant excerpt from document"""
        query_terms = query.lower().split()
        sentences = content.split('.')
        
        best_sentence = ""
        best_score = 0
        
        for sentence in sentences:
            score = sum(1 for term in query_terms if term in sentence.lower())
            if score > best_score:
                best_score = score
                best_sentence = sentence.strip()
        
        if len(best_sentence) > max_length:
            best_sentence = best_sentence[:max_length] + "..."
        
        return best_sentence or content[:max_length] + "..."


def main():
    """Demo usage - Use demo_constitution.py for full example"""
    print("Legal Chatbot Library")
    print("=" * 60)
    print("\nThis is the core library. To run a demo:")
    print("  python demo_constitution.py")
    print("\nOr import and use in your own code:")
    print("  from legal_chatbot import LegalChatbot, LegalKnowledgeBase")
    print("  from us_constitution import load_constitution")


if __name__ == "__main__":
    main()
