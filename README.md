# Legal Chatbot with Reasoning and Citations

A chatbot that answers legal questions using context from legal documents, with AI-powered reasoning chains and evidence citation.

## Features

- **Vector-Based Semantic Search**: Uses sentence transformers for intelligent document retrieval
- **AI-Powered Understanding**: Uses OpenAI API to parse questions and generate intelligent responses
- **Context-Aware Answers**: Retrieves relevant legal documents to answer questions
- **Reasoning Chain**: Explains the logic behind each answer
- **Evidence Citation**: Points to specific documents and excerpts with similarity scores
- **Confidence Scoring**: Indicates reliability of answers
- **Extensible Architecture**: Easy to add more documents or switch embedding models

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

## Quick Start

Basic demo:
```bash
python legal_chatbot.py
```

US Constitution demo:
```bash
python demo_constitution.py
```

## Architecture

- `LegalDocument`: Represents legal documents with metadata
- `LegalKnowledgeBase`: Manages document storage and retrieval
- `LegalChatbot`: Generates answers with AI-powered reasoning and citations
- `Citation`: Links answers to source documents with excerpts

## Usage

```python
from legal_chatbot import LegalChatbot, LegalKnowledgeBase, LegalDocument

# Setup
kb = LegalKnowledgeBase()
kb.add_document(LegalDocument(
    id="doc1",
    title="Contract Law",
    content="A contract requires...",
    source="Legal Code Section 123"
))

chatbot = LegalChatbot(kb)

# Ask questions
response = chatbot.answer("What makes a contract valid?")
print(response.answer)
print(response.reasoning)
for citation in response.citations:
    print(f"Source: {citation.document_title}")
```

## How It Works

1. **Document Embedding**: Each legal document is converted to a vector embedding using sentence transformers
2. **Question Parsing**: AI extracts key legal concepts from user questions
3. **Vector Search**: Finds most semantically similar documents using cosine similarity
4. **AI Reasoning**: Generates logical reasoning chain from retrieved context
5. **Answer Generation**: Produces accurate answer with citations
6. **Confidence Scoring**: Evaluates answer reliability based on semantic similarity

## Enhancements

To add advanced capabilities:

1. **Persistent Vector Database**: Use ChromaDB for scalable storage
2. **Multi-hop Reasoning**: Chain multiple documents for complex queries
3. **Alternative AI Providers**: Support Anthropic, Google, or local models
4. **Custom Embedding Models**: Use domain-specific legal embeddings
