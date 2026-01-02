"""
LLM interface classes for the Prompt Optimizer Loop.

This module provides abstract base classes and concrete implementations for
interacting with different LLM providers.
"""

from .base import BaseLLM
from .manager import ManagerLLM
from .executor import ExecutorLLM

__all__ = ["BaseLLM", "ManagerLLM", "ExecutorLLM"]