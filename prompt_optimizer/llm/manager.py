"""
Manager LLM implementation for prompt optimization.

This module provides the ManagerLLM class that specializes in analyzing and
improving input prompts before execution.
"""

from typing import Dict, Any
from .base import BaseLLM


class ManagerLLM(BaseLLM):
    """LLM specialized for prompt optimization and improvement."""
    
    def __init__(self, config):
        """Initialize the Manager LLM.
        
        Args:
            config: LLM configuration for the manager
        """
        super().__init__(config)
        self.optimization_instructions = getattr(config, 'optimization_instructions', 
                                               self._get_default_instructions())
    
    def optimize_prompt(self, original_prompt: str) -> str:
        """Optimize a prompt by analyzing and improving it.
        
        Args:
            original_prompt: The original prompt to optimize
            
        Returns:
            The optimized prompt
            
        Raises:
            LLMError: If optimization fails
        """
        optimization_prompt = self._build_optimization_prompt(original_prompt)
        return self.generate(optimization_prompt)
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response from the Manager LLM.
        
        Args:
            prompt: The input prompt
            **kwargs: Additional parameters
            
        Returns:
            The generated response
        """
        # This will be implemented in later tasks
        raise NotImplementedError("Manager LLM generation not yet implemented")
    
    def _create_client(self) -> Any:
        """Create the API client for the Manager LLM.
        
        Returns:
            The configured client
        """
        # This will be implemented in later tasks
        raise NotImplementedError("Client creation not yet implemented")
    
    def _build_optimization_prompt(self, original_prompt: str) -> str:
        """Build the prompt for optimization instructions.
        
        Args:
            original_prompt: The prompt to optimize
            
        Returns:
            The complete optimization prompt
        """
        return f"""
{self.optimization_instructions}

Original prompt to optimize:
{original_prompt}

Please provide an improved version of this prompt that is clearer, more specific, and more likely to produce better results.
"""
    
    def _get_default_instructions(self) -> str:
        """Get default optimization instructions.
        
        Returns:
            Default instructions for prompt optimization
        """
        return """
You are an expert prompt engineer. Your task is to analyze and improve prompts to make them more effective.

When optimizing a prompt, consider:
1. Clarity: Make the instructions clear and unambiguous
2. Specificity: Add specific details about desired output format
3. Context: Provide necessary background information
4. Structure: Organize the prompt logically
5. Examples: Include examples when helpful

Provide only the improved prompt without additional commentary.
"""