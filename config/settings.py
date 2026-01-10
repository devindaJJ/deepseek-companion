# config/settings.py
import os
from dotenv import load_dotenv
from pathlib import Path
from typing import Optional

class Settings:
    """Configuration settings management"""
    
    def __init__(self, env_file: Optional[str] = ".env"):
        
        if env_file and Path(env_file).exists():
            load_dotenv(env_file)
        
        self.DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
        self.DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
        self.DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")
        self.CODER_MODEL = os.getenv("CODER_MODEL")
        self.DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS"))
        self.DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE"))

        self._validate_settings()
    
    def _validate_settings(self) -> None:
        """Validate required settings"""
        if not self.DEEPSEEK_API_KEY:
            raise ValueError("DEEPSEEK_API_KEY is not set in environment variables")
        
        if not self.DEEPSEEK_API_KEY.startswith("sk-"):
            print("Warning: API key doesn't start with 'sk-', may be invalid")
    
    def get_model_config(self, model_type: str = "chat") -> dict:
        """Get configuration for specific model type"""
        configs = {
            "chat": {
                "model": self.DEFAULT_MODEL,
                "max_tokens": self.DEFAULT_MAX_TOKENS,
                "temperature": self.DEFAULT_TEMPERATURE
            },
            "coder": {
                "model": self.CODER_MODEL,
                "max_tokens": self.DEFAULT_MAX_TOKENS * 2, 
                "temperature": 0.2  
            },
            "creative": {
                "model": self.DEFAULT_MODEL,
                "max_tokens": self.DEFAULT_MAX_TOKENS,
                "temperature": 0.9 
            }
        }
        return configs.get(model_type, configs["chat"])

settings = Settings()