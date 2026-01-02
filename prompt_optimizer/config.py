"""
Configuration data classes for the Prompt Optimizer Loop.

This module defines the configuration structures needed to set up and customize
the behavior of the prompt optimization system.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class LLMConfig:
    """Configuration for an individual LLM provider."""
    
    provider: str  # "openai", "anthropic", "azure", etc.
    model: str
    api_key: str
    base_url: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 2048
    timeout: int = 30
    optimization_instructions: Optional[str] = None
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if not self.provider:
            raise ValueError("Provider must be specified")
        if not self.model:
            raise ValueError("Model must be specified")
        if not self.api_key:
            raise ValueError("API key must be specified")
        if self.temperature < 0 or self.temperature > 2:
            raise ValueError("Temperature must be between 0 and 2")
        if self.max_tokens <= 0:
            raise ValueError("Max tokens must be positive")
        if self.timeout <= 0:
            raise ValueError("Timeout must be positive")


@dataclass
class OptimizationConfig:
    """Main configuration for the prompt optimization system."""
    
    manager_config: LLMConfig
    executor_config: LLMConfig
    optimization_instructions: Optional[str] = None
    max_retries: int = 3
    retry_delay: float = 1.0
    enable_fallback: bool = True
    max_prompt_length: int = 10000
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if self.max_retries < 0:
            raise ValueError("Max retries must be non-negative")
        if self.retry_delay < 0:
            raise ValueError("Retry delay must be non-negative")
        if self.max_prompt_length <= 0:
            raise ValueError("Max prompt length must be positive")
        
        # Validate that both LLM configs are provided
        if not isinstance(self.manager_config, LLMConfig):
            raise ValueError("Manager config must be an LLMConfig instance")
        if not isinstance(self.executor_config, LLMConfig):
            raise ValueError("Executor config must be an LLMConfig instance")