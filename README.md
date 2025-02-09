# **PromptFletcher** 🚀  
**A Python library for auto-prompt engineering and optimization for LLMs.**  

[![Python Versions](https://img.shields.io/pypi/pyversions/promptfletcher)](https://pypi.org/project/promptfletcher/)  
[![License](https://img.shields.io/github/license/Vikhram-S/PromptFletcher)](LICENSE)  
[![Issues](https://img.shields.io/github/issues/Vikhram-S/PromptFletcher)](https://github.com/Vikhram-S/PromptFletcher/issues)  
[![Stars](https://img.shields.io/github/stars/Vikhram-S/PromptFletcher?style=social)](https://github.com/Vikhram-S/PromptFletcher/stargazers)  

---

## **🚀 What is PromptFletcher?**  
**PromptFletcher** is a **lightweight** and **powerful** Python library designed for:  
✅ **Refining & optimizing prompts** for LLMs  
✅ **Context-aware prompt tuning** for better responses  
✅ **Heuristic-based evaluation** to rank prompts  
✅ **Integrating with open-source LLMs** (GPT-Neo, GPT-J, BLOOM)  

---

## **🛠️ Installation**  
### **From PyPI** (Coming Soon)
```bash
pip install promptfletcher
```
### **From GitHub**
```bash
pip install git+https://github.com/Vikhram-S/PromptFletcher.git
```

---

## **📌 Quick Start**  
### **1️⃣ Import & Initialize**  
```python
from promptfletcher import AutoPromptEngineer

engineer = AutoPromptEngineer()
```

### **2️⃣ Define Context & Prompt**  
```python
context = "We are exploring ways to enhance prompt engineering for LLMs."
initial_prompt = "How can I improve my AI-generated responses?"
```

### **3️⃣ Optimize the Prompt**  
```python
refined_prompt = engineer.refine_prompt(initial_prompt, context)
print("Refined Prompt:", refined_prompt)
```

---

## **⚡ Features**  
✅ **Automated Prompt Refinement** – Uses NLP techniques to improve prompt clarity.  
✅ **LLM Response Evaluation** – Integrates with open-source models like GPT-Neo & BLOOM.  
✅ **Contextual Understanding** – Ensures prompts align with relevant topics.  
✅ **Lightweight & Fast** – Minimal dependencies, designed for efficiency.  

---

## **📚 API Reference**  
### **`AutoPromptEngineer` Class**
#### `refine_prompt(prompt: str, context: str, iterations: int = 3) -> str`  
🔹 **Refines a given prompt based on context and heuristic scoring.**  
```python
engineer.refine_prompt("How do I make my AI-generated text more accurate?", "LLM optimization")
```

#### `evaluate_prompt(prompt: str, context: str) -> float`  
🔹 **Assigns a heuristic score to a prompt based on clarity and relevance.**  
```python
score = engineer.evaluate_prompt("Tell me about AI safety?", "Machine Learning Ethics")
print("Prompt Score:", score)
```

---

## **📦 Dependencies**
- `transformers>=4.30.0`
- `torch>=2.0.0`
- `numpy>=1.21.0`
- `regex>=2023.3.23`

Install dependencies manually:
```bash
pip install -r requirements.txt
```

---

## **📜 License**  
**PromptFletcher** is licensed under the **MIT License** – free to use, modify, and distribute.  

---

## **🤝 Contributing**  
We welcome contributions!  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-new`)  
3. Commit changes & push (`git push origin feature-new`)  
4. Open a **Pull Request**  

---

## **📬 Contact & Support**  
- **GitHub Issues:** [Report Bugs](https://github.com/Vikhram-S/PromptFletcher/issues)  
- **Email:** vikhrams@saveetha.ac.in  

⭐ **If you find this useful, give us a star on GitHub!** ⭐  

---
