# src/utils/logger.py
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional

class Logger:
    """Custom logger for DeepSeek API"""
    
    def __init__(self, name: str = "DeepSeekAPI", log_file: Optional[str] = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        if log_file:
            log_path = Path(log_file).parent
            log_path.mkdir(parents=True, exist_ok=True)
        
        detailed_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        simple_formatter = logging.Formatter('%(levelname)s: %(message)s')
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(simple_formatter)
        
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(detailed_formatter)
            self.logger.addHandler(file_handler)
        
        self.logger.addHandler(console_handler)
    
    def log_request(self, model: str, prompt_length: int) -> None:
        """Log API request details"""
        self.logger.info(f"Request to {model} with {prompt_length} chars")
    
    def log_response(self, response_length: int, response_time: float) -> None:
        """Log API response details"""
        self.logger.info(f"Response: {response_length} chars in {response_time:.2f}s")
    
    def log_error(self, error: Exception) -> None:
        """Log errors"""
        self.logger.error(f"API Error: {str(error)}")
    
    def get_logger(self) -> logging.Logger:
        """Get the underlying logger"""
        return self.logger

logger = Logger()