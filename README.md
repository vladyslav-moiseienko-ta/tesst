# Prompt Optimizer Loop

A Python system for automatically improving prompts through iterative refinement using Language Learning Models (LLMs).

## Overview

The Prompt Optimizer Loop uses a two-LLM architecture where a Manager LLM analyzes and optimizes input prompts, and an Executor LLM runs the improved prompts to generate final results.

## Features

- Automatic prompt optimization using specialized LLMs
- Support for multiple LLM providers (OpenAI, Anthropic, Azure)
- Comprehensive error handling and retry logic
- Structured response formatting with improvement analysis
- Property-based testing for correctness validation

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Install with test dependencies
uv sync --group test

# Install with development dependencies  
uv sync --group dev
```

## Usage

```python
from prompt_optimizer import PromptOptimizer, OptimizationConfig, LLMConfig

# Configure LLMs
manager_config = LLMConfig(
    provider="openai",
    model="gpt-4",
    api_key="your-api-key"
)

executor_config = LLMConfig(
    provider="openai", 
    model="gpt-3.5-turbo",
    api_key="your-api-key"
)

# Create optimizer
config = OptimizationConfig(
    manager_config=manager_config,
    executor_config=executor_config
)
optimizer = PromptOptimizer(config)

# Optimize and execute a prompt
result = optimizer.optimize_and_execute("Your original prompt here")
print(result.execution_result)
```

## Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=prompt_optimizer

# Run property-based tests only
uv run pytest -m property
```

## Development

This project follows spec-driven development with comprehensive testing including property-based tests for correctness validation.

## License

MIT License