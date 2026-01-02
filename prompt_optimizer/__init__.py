"""
Prompt Optimizer Loop - A system for automatically improving prompts through iterative refinement.

This package provides tools for optimizing prompts using a Manager LLM before executing them
with an Executor LLM to achieve better results.
"""

from .core import PromptOptimizer
from .config import OptimizationConfig, LLMConfig
from .models import OptimizationResult, PromptAnalysis, ExecutionMetrics

__version__ = "0.1.0"
__all__ = [
    "PromptOptimizer",
    "OptimizationConfig", 
    "LLMConfig",
    "OptimizationResult",
    "PromptAnalysis", 
    "ExecutionMetrics"
]