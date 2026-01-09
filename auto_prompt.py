"""
Auto-Prompt Engineering Package with NLTK
==========================================

This module replaces the LLM-based prompt optimization with NLTK-based NLP techniques 
for faster execution and lightweight processing.
"""

import os
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from typing import List

# Global flag to ensure that NLTK's 'punkt' is downloaded only once.
_punkt_ready = False

def ensure_punkt():
    """
    Ensure that the NLTK 'punkt' tokenizer data is available.
    If not, attempt to download it.
    """
    global _punkt_ready
    if not _punkt_ready:
        try:
            nltk.data.find("tokenizers/punkt")
        except LookupError:
            print("NLTK 'punkt' tokenizer not found. Downloading...")
            nltk.download("punkt", quiet=True)
        _punkt_ready = True

class AutoPromptEngineer:
    """
    A class for refining prompts using NLTK heuristics.
    """
    def __init__(self):
        """
        Initialize the AutoPromptEngineer.
        Ensures that the required NLTK data is available.
        """
        ensure_punkt()

    def evaluate_prompt(self, prompt: str, context: str) -> float:
        """
        Evaluate the effectiveness of a prompt using heuristic measures.

        Heuristics:
            1. Length factor: Prompts too short or too long are penalized.
            2. Clarity: Prompts ending with a question mark are rewarded.
            3. Relevance: Prompts containing context keywords are rewarded.

        Parameters:
            prompt (str): The prompt to evaluate.
            context (str): The relevant context for the prompt.

        Returns:
            float: A heuristic score representing prompt quality.
        """
        ensure_punkt()
        score = 0

        # Heuristic 1: Length factor
        word_count = len(word_tokenize(prompt))
        if word_count < 5:
            score -= 1
        elif word_count > 50:
            score -= 1
        else:
            score += 1

        # Heuristic 2: Clarity - check if prompt ends with a question mark
        if prompt.strip().endswith("?"):
            score += 1
        else:
            score -= 0.5

        # Heuristic 3: Presence of context keywords in the prompt
        context_keywords = set(word_tokenize(context.lower()))
        prompt_keywords = set(word_tokenize(prompt.lower()))
        common_keywords = context_keywords.intersection(prompt_keywords)
        if common_keywords:
            score += 1
        else:
            score -= 1

        return score

    def generate_candidate_prompts(self, prompt: str, context: str) -> List[str]:
        """
        Generate a list of candidate prompts by applying small modifications.

        Parameters:
            prompt (str): The current prompt.
            context (str): The relevant context.

        Returns:
            List[str]: A list of improved prompt variations.
        """
        ensure_punkt()
        candidates = [
            prompt.strip() + " Please provide a detailed explanation.",
            f"Based on the context '{context}', {prompt.strip()}",
            prompt.strip() + " Explain step by step."
        ]

        # If the prompt does not already end with a question mark, add one.
        if not prompt.strip().endswith("?"):
            candidates.append(prompt.strip() + "?")

        return candidates

    def refine_prompt(self, prompt: str, context: str, iterations: int = 3) -> str:
        """
        Refine the given prompt by iteratively generating candidate variations,
        evaluating them, and selecting the best candidate.

        Parameters:
            prompt (str): The initial prompt.
            context (str): The relevant context.
            iterations (int): Number of refinement iterations.

        Returns:
            str: The optimized prompt.
        """
        current_prompt = prompt
        best_score = self.evaluate_prompt(current_prompt, context)

        for _ in range(iterations):
            candidates = self.generate_candidate_prompts(current_prompt, context)
            # Evaluate all candidate prompts
            candidate_scores = [(cand, self.evaluate_prompt(cand, context)) for cand in candidates]
            # Sort candidates based on their score in descending order
            candidate_scores.sort(key=lambda x: x[1], reverse=True)
            best_candidate, candidate_score = candidate_scores[0]

            # Update the prompt only if the candidate's score improves
            if candidate_score > best_score:
                current_prompt = best_candidate
                best_score = candidate_score
            else:
                break

        return current_prompt

# Example usage
if __name__ == "__main__":
    context = "We are discussing ways to optimize prompt performance for NLP models."
    initial_prompt = "How can we improve prompt clarity?"

    engineer = AutoPromptEngineer()
    refined_prompt = engineer.refine_prompt(initial_prompt, context)

    print("Initial Prompt:", initial_prompt)
    print("Refined Prompt:", refined_prompt)
