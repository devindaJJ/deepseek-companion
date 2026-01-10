import time
from typing import Dict, List, Optional, Generator
from openai import OpenAI
from config.settings import settings
from src.utils.logger import logger
from src.utils.helpers import HelperFunctions

class DeepSeekClient:
    """Main DeepSeek API Client Class"""
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """Initialize DeepSeek client
        
        Args:
            api_key: DeepSeek API key (uses settings if None)
            base_url: API base URL (uses settings if None)
        """
        self.api_key = api_key or settings.DEEPSEEK_API_KEY
        self.base_url = base_url or settings.DEEPSEEK_BASE_URL
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
        
        self.helper = HelperFunctions()
        self.conversation_history = []
        
        logger.get_logger().info(f"DeepSeekClient initialized with base URL: {self.base_url}")
    
    def chat(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        model_type: str = "chat",
        stream: bool = False,
        **kwargs
    ) -> str:
        """Send a chat message to DeepSeek
        
        Args:
            message: User message
            system_prompt: System role definition
            model_type: Type of model ('chat', 'coder', 'creative')
            stream: Whether to stream response
            **kwargs: Additional API parameters
        
        Returns:
            AI response as string
        """
        start_time = time.time()
        
        config = settings.get_model_config(model_type)
        
        system_content = system_prompt or "You are a helpful AI assistant."
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": message}
        ]
        
        params = {
            "model": config["model"],
            "messages": messages,
            "max_tokens": kwargs.get("max_tokens", config["max_tokens"]),
            "temperature": kwargs.get("temperature", config["temperature"]),
            "stream": stream
        }
        
        optional_params = ["top_p", "frequency_penalty", "presence_penalty"]
        for param in optional_params:
            if param in kwargs:
                params[param] = kwargs[param]
        
        try:
            logger.log_request(config["model"], len(message))
            
            if stream:
                return self._handle_streaming_response(params)
            else:
                response = self.client.chat.completions.create(**params)
                response_text = response.choices[0].message.content
                response_time = time.time() - start_time
                logger.log_response(len(response_text), response_time)
                self._save_to_history(messages[0], messages[1], response_text)
                
                return response_text
                
        except Exception as e:
            logger.log_error(e)
            raise Exception(f"API Error: {str(e)}")
    
    def _handle_streaming_response(self, params: Dict) -> Generator[str, None, None]:
        """Handle streaming response"""
        response = self.client.chat.completions.create(**params)
        
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
                yield content
        
        # Save complete response to history
        if len(params["messages"]) >= 2:
            self._save_to_history(
                params["messages"][0],
                params["messages"][1],
                full_response
            )
    
    def _save_to_history(
        self,
        system_message: Dict,
        user_message: Dict,
        assistant_response: str
    ) -> None:
        """Save conversation to history"""
        self.conversation_history.extend([
            system_message,
            user_message,
            {"role": "assistant", "content": assistant_response}
        ])
    
    def get_conversation_history(self) -> List[Dict]:
        """Get complete conversation history"""
        return self.conversation_history.copy()
    
    def clear_history(self) -> None:
        """Clear conversation history"""
        self.conversation_history.clear()
        logger.get_logger().info("Conversation history cleared")
    
    def continue_conversation(
        self,
        message: str,
        history: Optional[List[Dict]] = None,
        **kwargs
    ) -> str:
        """Continue conversation with existing history
        
        Args:
            message: New user message
            history: Previous conversation history
            **kwargs: Additional API parameters
        
        Returns:
            AI response
        """

        messages = history or self.conversation_history
        messages.append({"role": "user", "content": message})
        
        config = settings.get_model_config("chat")
        params = {
            "model": config["model"],
            "messages": messages,
            "max_tokens": kwargs.get("max_tokens", config["max_tokens"]),
            "temperature": kwargs.get("temperature", config["temperature"])
        }
        
        try:
            response = self.client.chat.completions.create(**params)
            response_text = response.choices[0].message.content
            
            # Update history
            messages.append({"role": "assistant", "content": response_text})
            if not history:  # Only update internal history if using it
                self.conversation_history = messages
            
            return response_text
            
        except Exception as e:
            logger.log_error(e)
            raise Exception(f"API Error: {str(e)}")