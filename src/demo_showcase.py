"""
Demo/Showcase mode for LinkedIn portfolio presentation
Shows capabilities without requiring API credentials
"""
import time
import json
from typing import Dict, Any

class DemoShowcase:
    """Professional demo showcasing DeepSeek Companion capabilities"""
    
    def __init__(self):
        self.demo_data = self._load_demo_data()
    
    def _load_demo_data(self) -> Dict[str, Any]:
        """Load sample responses"""
        return {
            "geography": {
                "query": "What is the capital of France?",
                "system_prompt": "You are a geography expert.",
                "response": "Paris is the capital of France. It's located in north-central France and serves as the country's political, cultural, and economic center. The city has been a major hub since the Roman period and is home to iconic landmarks like the Eiffel Tower, Notre-Dame Cathedral, and the Louvre Museum."
            },
            "code": {
                "query": "Write a Python function to check if a number is prime",
                "model_type": "coder",
                "response": '''def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(17))  # True
print(is_prime(20))  # False
print(is_prime(2))   # True'''
            },
            "creative": {
                "query": "Write a haiku about artificial intelligence",
                "model_type": "creative",
                "response": "Neural pathways glow,\nThoughts that flow through silicon,\nMind meets machine here."
            }
        }
    
    def run_demo(self):
        """Run full demo showcase"""
        self._print_header()
        time.sleep(0.5)
        
        self._demo_simple_chat()
        time.sleep(1)
        
        self._demo_coding()
        time.sleep(1)
        
        self._demo_creative()
        time.sleep(1)
        
        self._demo_features()
        time.sleep(0.5)
        
        self._print_footer()
    
    def _print_header(self):
        """Print demo header"""
        print("\n" + "=" * 70)
        print("🤖  DEEPSEEK AI COMPANION - DEMO SHOWCASE")
        print("=" * 70)
        print("📌 [MOCK DATA - For Portfolio/LinkedIn Presentation]")
        print("=" * 70 + "\n")
    
    def _demo_simple_chat(self):
        """Demo: Simple chat"""
        print("📚 DEMO 1: Geography Expert Chat")
        print("-" * 70)
        
        data = self.demo_data["geography"]
        print(f"Query: {data['query']}")
        print(f"System Prompt: {data['system_prompt']}")
        print("\n✓ DeepSeek Client initialized with base URL: https://api.deepseek.com")
        print("⏳ Processing request...\n")
        
        time.sleep(0.8)
        
        print(f"Response:\n{data['response']}")
        print("\n")
    
    def _demo_coding(self):
        """Demo: Coding assistance"""
        print("💻 DEMO 2: Coding Assistance (Coder Model)")
        print("-" * 70)
        
        data = self.demo_data["code"]
        print(f"Query: {data['query']}")
        print(f"Model: {data['model_type']}")
        print("\n✓ DeepSeek Client initialized with base URL: https://api.deepseek.com")
        print("⏳ Processing request...\n")
        
        time.sleep(0.8)
        
        print(f"Response:\n```python\n{data['response']}\n```")
        print("\n")
    
    def _demo_creative(self):
        """Demo: Creative mode"""
        print("✨ DEMO 3: Creative Writing (Creative Model)")
        print("-" * 70)
        
        data = self.demo_data["creative"]
        print(f"Query: {data['query']}")
        print(f"Model: {data['model_type']}")
        print("\n✓ DeepSeek Client initialized with base URL: https://api.deepseek.com")
        print("⏳ Processing request...\n")
        
        time.sleep(0.8)
        
        print(f"Response:\n{data['response']}")
        print("\n")
    
    def _demo_features(self):
        """Demo: Feature showcase"""
        print("🎯 KEY FEATURES")
        print("-" * 70)
        
        features = [
            ("✓", "Multi-Model Support", "Chat, Coder, Creative models"),
            ("✓", "Conversation History", "Maintains context across turns"),
            ("✓", "Streaming Support", "Real-time response streaming"),
            ("✓", "System Prompts", "Customizable AI behavior"),
            ("✓", "CLI Interface", "Multiple modes: chat, query, examples"),
            ("✓", "Configuration Management", "Environment-based settings"),
            ("✓", "Error Handling", "Robust exception management"),
            ("✓", "Logging System", "Debug-level logging available"),
        ]
        
        for check, feature, description in features:
            print(f"  {check} {feature:<25} → {description}")
        
        print("\n")
    
    def _print_footer(self):
        """Print demo footer"""
        print("=" * 70)
        print("📊 TECH STACK")
        print("-" * 70)
        print("  • Language:        Python 3.8+")
        print("  • API Client:      OpenAI SDK (compatible with DeepSeek)")
        print("  • Architecture:    Class-based with separation of concerns")
        print("  • Configuration:   Environment variables via python-dotenv")
        print("\n")
        print("=" * 70)
        print("🚀 QUICK START COMMANDS")
        print("-" * 70)
        print("  python main.py --chat          # Interactive chat mode")
        print("  python main.py --query \"text\"  # Single query")
        print("  python main.py --example       # Run examples (requires API key)")
        print("  python main.py --demo          # View this showcase")
        print("=" * 70 + "\n")


def run_demo_showcase():
    """Entry point for demo showcase"""
    demo = DemoShowcase()
    demo.run_demo()
