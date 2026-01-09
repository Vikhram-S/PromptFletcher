"""
PromptForge: An Auto-Prompt Engineering Library for LLMs
=========================================================

PromptForge helps refine and optimize prompts for large language models (LLMs) 
by iteratively improving query clarity, relevance, and effectiveness.

Features:
---------
- Context-aware prompt refinement
- Automated heuristic evaluation
- Open-source LLM integration for response analysis

Usage:
------
>>> from promptfletcher import AutoPromptEngineer
>>> engineer = AutoPromptEngineer()
>>> refined_prompt = engineer.refine_prompt("How can I optimize my LLM prompts?", context="AI research")
>>> print(refined_prompt)
"""

from .auto_prompt import AutoPromptEngineer

__version__ = "0.1.2"
__author__ = "Vikhram S"
__license__ = "MIT"
__all__ = ["AutoPromptEngineer"]
