import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.models.deepseek_client import DeepSeekClient
from src.utils.helpers import HelperFunctions
import time

class DeepSeekExamples:
    """Example usage of DeepSeek API Client"""
    
    def __init__(self):
        self.client = DeepSeekClient()
        self.helper = HelperFunctions()
    
    def example_simple_chat(self):
        """Example: Simple chat conversation"""
        print("=== Simple Chat Example ===")
        
        response = self.client.chat(
            "What is the capital of France?",
            system_prompt="You are a geography expert."
        )
        
        print(f"Question: What is the capital of France?")
        print(f"Response: {response}\n")
        
        return response
    
    def example_coding_assistance(self):
        """Example: Get coding help"""
        print("=== Coding Assistance Example ===")
        
        response = self.client.chat(
            "Write a Python function to check if a number is prime",
            model_type="coder"
        )
        
        print(f"Request: Write a prime number checker")
        print(f"Response:\n{response}\n")
        
        return response
    
    def example_streaming_response(self):
        """Example: Streaming response"""
        print("=== Streaming Response Example ===")
        print("Explain quantum computing in simple terms:\n")
        
        stream = self.client.chat(
            "Explain quantum computing in simple terms",
            stream=True
        )
        
        full_response = ""
        for chunk in stream:
            print(chunk, end="", flush=True)
            full_response += chunk
        
        print("\n")
        return full_response
    
    def example_conversation_history(self):
        """Example: Maintaining conversation context"""
        print("=== Conversation History Example ===")
        
        # First message
        response1 = self.client.chat(
            "My name is John. I like programming.",
            system_prompt="Remember details about the user."
        )
        print(f"AI: {response1}")
        
        # Second message (should remember context)
        response2 = self.client.continue_conversation(
            "What's my name and what do I like?"
        )
        print(f"AI: {response2}")
        
        # Show history
        print(f"\nConversation History:")
        for i, msg in enumerate(self.client.get_conversation_history()):
            role = msg["role"]
            content = msg["content"][:50] + "..." if len(msg["content"]) > 50 else msg["content"]
            print(f"{i+1}. [{role.upper()}]: {content}")
        
        return response2
    
    def example_save_conversation(self):
        """Example: Save conversation to file"""
        print("=== Save Conversation Example ===")
        
        # Have a conversation
        self.client.chat("Hello, how are you?")
        self.client.continue_conversation("Tell me a joke")
        
        # Save to file
        filename = self.helper.save_conversation(self.client.get_conversation_history())
        print(f"Conversation saved to: {filename}")
        
        return filename

def run_all_examples():
    """Run all examples"""
    examples = DeepSeekExamples()
    
    print("=" * 50)
    print("DeepSeek API Examples")
    print("=" * 50 + "\n")
    
    # Run examples
    examples.example_simple_chat()
    time.sleep(1)
    
    examples.example_coding_assistance()
    time.sleep(1)
    
    print("Streaming example (press Ctrl+C to skip)...")
    try:
        examples.example_streaming_response()
    except KeyboardInterrupt:
        print("\nSkipping streaming example...")
    
    time.sleep(1)
    
    examples.example_conversation_history()
    time.sleep(1)
    
    examples.example_save_conversation()
    
    print("\n" + "=" * 50)
    print("All examples completed!")
    print("=" * 50)

if __name__ == "__main__":
    run_all_examples()