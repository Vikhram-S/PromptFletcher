from setuptools import setup, find_packages

# Read the contents of your README file with UTF-8 encoding
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="promptfletcher",
    version="0.1.2",
    author="Vikhram S",
    author_email="vikhrams@saveetha.ac.in",
    description="A Python library for auto-prompt engineering and optimization for LLMs.",
    status="beta",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vikhram-S/PromptFletcher",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
       "nltk>=3.6.0",
       "numpy>=1.21.0",
       "regex>=2023.3.23"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7, <3.14",
    project_urls={
        "Bug Tracker": "https://github.com/Vikhram-S/PromptFletcher/issues",
        "Documentation": "https://github.com/Vikhram-S/PromptFletcher#readme",
        "Source Code": "https://github.com/Vikhram-S/PromptFletcher",
    },
)
