"""
Abstract base class for LLM interfaces.

This module defines the common interface that all LLM implementations must follow,
providing a consistent API for different providers.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from ..config import LLMConfig


class BaseLLM(ABC):
    """Abstract base class for all LLM implementations."""
    
    def __init__(self, config: LLMConfig):
        """Initialize the LLM with configuration.
        
        Args:
            config: LLM configuration containing provider details, API keys, etc.
        """
        self.config = config
        self.client = self._create_client()
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response from the LLM.
        
        Args:
            prompt: The input prompt to send to the LLM
            **kwargs: Additional parameters for the LLM call
            
        Returns:
            The generated response as a string
            
        Raises:
            LLMError: If the LLM call fails
        """
        pass
    
    @abstractmethod
    def _create_client(self) -> Any:
        """Create and configure the API client for this LLM provider.
        
        Returns:
            The configured client object for making API calls
            
        Raises:
            ConfigurationError: If the configuration is invalid
        """
        pass
    
    def validate_config(self) -> bool:
        """Validate that the LLM configuration is correct.
        
        Returns:
            True if configuration is valid, False otherwise
        """
        required_fields = ['provider', 'model', 'api_key']
        return all(hasattr(self.config, field) and getattr(self.config, field) 
                  for field in required_fields)