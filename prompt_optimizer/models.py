"""
Data models for the Prompt Optimizer Loop.

This module defines the core data structures used throughout the system
for representing optimization results, analysis data, and execution metrics.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional


@dataclass
class OptimizationResult:
    """Result of a complete prompt optimization and execution cycle."""
    
    original_prompt: str
    optimized_prompt: str
    execution_result: str
    optimization_time: float
    execution_time: float
    improvements: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    success: bool = True
    error_message: Optional[str] = None
    
    def __post_init__(self):
        """Validate the optimization result after initialization."""
        if self.optimization_time < 0:
            raise ValueError("Optimization time must be non-negative")
        if self.execution_time < 0:
            raise ValueError("Execution time must be non-negative")


@dataclass
class PromptAnalysis:
    """Analysis of a prompt's quality and suggested improvements."""
    
    clarity_score: float
    specificity_score: float
    structure_improvements: List[str] = field(default_factory=list)
    suggested_changes: List[str] = field(default_factory=list)
    confidence: float = 0.0
    
    def __post_init__(self):
        """Validate the prompt analysis after initialization."""
        if not (0 <= self.clarity_score <= 1):
            raise ValueError("Clarity score must be between 0 and 1")
        if not (0 <= self.specificity_score <= 1):
            raise ValueError("Specificity score must be between 0 and 1")
        if not (0 <= self.confidence <= 1):
            raise ValueError("Confidence must be between 0 and 1")


@dataclass
class ExecutionMetrics:
    """Metrics collected during prompt execution."""
    
    start_time: datetime
    end_time: datetime
    token_usage: Dict[str, int] = field(default_factory=dict)
    cost_estimate: Optional[float] = None
    provider_metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate the execution metrics after initialization."""
        if self.end_time < self.start_time:
            raise ValueError("End time must be after start time")
        if self.cost_estimate is not None and self.cost_estimate < 0:
            raise ValueError("Cost estimate must be non-negative")
    
    @property
    def duration(self) -> float:
        """Calculate the execution duration in seconds."""
        return (self.end_time - self.start_time).total_seconds()