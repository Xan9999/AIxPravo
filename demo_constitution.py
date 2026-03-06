"""
Demo: Legal Chatbot with US Constitution
"""
from legal_chatbot import LegalChatbot, LegalKnowledgeBase
from us_constitution import load_constitution


def main():
    print("=" * 70)
    print("US CONSTITUTION LEGAL CHATBOT")
    print("=" * 70)
    print()
    
    # Initialize knowledge base
    kb = LegalKnowledgeBase()
    
    # Load US Constitution
    num_docs = load_constitution(kb)
    print(f"✓ Loaded {num_docs} Constitution documents")
    print()
    print("Ask questions about the US Constitution!")
    print("Type 'quit' or 'exit' to end the session")
    print("=" * 70)
    
    # Create chatbot
    chatbot = LegalChatbot(kb)
    
    # Interactive mode
    while True:
        try:
            question = input("\n💬 Your question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye!")
                break
            
            if not question:
                continue
            
            print("\n🔍 Searching Constitution...")
            response = chatbot.answer(question)
            
            print(f"\n🤖 Answer:\n{response.answer}")
            print(f"\n🧠 Reasoning:\n{response.reasoning}")
            print(f"\n📊 Confidence: {response.confidence:.2f}")
            
            if response.citations:
                print("\n📚 Citations:")
                for i, citation in enumerate(response.citations, 1):
                    print(f"\n  [{i}] {citation.document_title}")
                    print(f"      Relevance: {citation.relevance_score:.2f}")
                    print(f"      Excerpt: \"{citation.excerpt}\"")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
