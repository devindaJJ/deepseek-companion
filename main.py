import sys
from pathlib import Path

src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))

from src.models.deepseek_client import DeepSeekClient
from src.examples.usage_examples import run_all_examples
from src.demo_showcase import run_demo_showcase
import argparse

def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(description="DeepSeek API Client")
    parser.add_argument("--example", action="store_true", help="Run examples")
    parser.add_argument("--chat", action="store_true", help="Start interactive chat")
    parser.add_argument("--query", type=str, help="Single query to send")
    parser.add_argument("--demo", action="store_true", help="Run demo showcase (no API key needed)")
    parser.add_argument("--model", type=str, default="chat", 
                       choices=["chat", "coder", "creative"],
                       help="Model type to use")
    
    args = parser.parse_args()
    
    # Demo mode - doesn't require API key
    if args.demo:
        run_demo_showcase()
        return
    
    # Initialize client
    try:
        client = DeepSeekClient()
        print("✓ DeepSeek Client initialized successfully")
    except Exception as e:
        print(f"✗ Failed to initialize client: {e}")
        return
    
    if args.example:
        # Run examples
        run_all_examples()
    
    elif args.query:
        # Single query mode
        print(f"\nQuery: {args.query}")
        print(f"Model: {args.model}")
        print("-" * 50)
        
        response = client.chat(args.query, model_type=args.model)
        print(f"\nResponse:\n{response}")
    
    elif args.chat or not any(vars(args).values()):
        # Interactive chat mode
        print("\n" + "=" * 50)
        print("DeepSeek Interactive Chat")
        print("Type 'quit' or 'exit' to end, 'clear' to clear history")
        print("=" * 50 + "\n")
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                elif user_input.lower() == 'clear':
                    client.clear_history()
                    print("Conversation history cleared")
                    continue
                elif not user_input:
                    continue
                
                # Send to DeepSeek
                response = client.continue_conversation(user_input)
                print(f"\nAssistant: {response}")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"\nError: {e}")

if __name__ == "__main__":
    main()