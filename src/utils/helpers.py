import json
from typing import Any, Dict, List, Optional
from datetime import datetime

class HelperFunctions:
    """Utility functions for the DeepSeek API"""
    
    @staticmethod
    def format_messages(system_prompt: str, user_messages: List[str]) -> List[Dict[str, str]]:
        """Format messages for API request"""
        messages = [{"role": "system", "content": system_prompt}]
        
        for i, message in enumerate(user_messages):
            role = "user" if i % 2 == 0 else "assistant"
            messages.append({"role": role, "content": message})
        
        return messages
    
    @staticmethod
    def estimate_tokens(text: str) -> int:
        """Rough token estimation (1 token ≈ 4 chars for English)"""
        return len(text) // 4
    
    @staticmethod
    def save_conversation(conversation: List[Dict], filename: Optional[str] = None) -> str:
        """Save conversation to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversation_{timestamp}.json"
        
        data = {
            "timestamp": datetime.now().isoformat(),
            "conversation": conversation
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        return filename
    
    @staticmethod
    def load_conversation(filename: str) -> List[Dict]:
        """Load conversation from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
        return data.get("conversation", [])
    
    @staticmethod
    def truncate_text(text: str, max_tokens: int) -> str:
        """Truncate text to estimated token limit"""
        estimated_tokens = HelperFunctions.estimate_tokens(text)
        if estimated_tokens <= max_tokens:
            return text
        
        max_chars = max_tokens * 4
        return text[:max_chars] + "... [truncated]"