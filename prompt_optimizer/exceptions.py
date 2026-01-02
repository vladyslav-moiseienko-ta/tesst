"""
Custom exceptions for the Prompt Optimizer Loop.

This module defines all custom exceptions used throughout the system
for better error handling and debugging.
"""


class PromptOptimizerError(Exception):
    """Base exception for all prompt optimizer errors."""
    pass


class ConfigurationError(PromptOptimizerError):
    """Raised when there are configuration-related errors."""
    pass


class ValidationError(PromptOptimizerError):
    """Raised when input validation fails."""
    pass


class LLMError(PromptOptimizerError):
    """Raised when LLM operations fail."""
    pass


class OptimizationError(PromptOptimizerError):
    """Raised when prompt optimization fails."""
    pass


class ExecutionError(PromptOptimizerError):
    """Raised when prompt execution fails."""
    pass


class RetryExhaustedError(PromptOptimizerError):
    """Raised when all retry attempts are exhausted."""
    pass