# LLM Course

This repository contains tutorials and scripts for working with Large Language Models (LLMs), natural language processing, and text analysis.



## Tutorials (Jupyter Notebooks)

### 🔒 `deidentification.py`
**Text De-identification using Presidio**
- Remove personally identifiable information (PII) from text
- Uses Microsoft Presidio Analyzer and Anonymizer
- Detects and anonymizes names, phone numbers, and other sensitive data
- Leverages spaCy's NLP models for entity recognition
- Batch processing support with progress tracking using tqdm

### 📊 `openrouter_api.ipynb`
**Measure constructs using LLMs**
- Learn how to use the OpenRouter API to access various LLM models
- Process API outputs and extract structured data from LLM responses
- Measure psychological and social constructs using LLMs
- Save results to CSV for further analysis
- Includes error handling and batch processing examples

### 🔗 `embeddings_tutorial.ipynb`
- Generate text embeddings using Spanish transformer models (sentence-transformers)
- Apply UMAP for dimensionality reduction to visualize in 2D
- Perform clustering on vector representations
- Visualize semantic relationships with interactive plots using Plotly
- Demonstrates how embeddings capture semantic meaning across different social constructs

### 📝 `linguistic_properties.ipynb`
**English Linguistic Features with spaCy + TextDescriptives**
- Extract comprehensive linguistic and readability features from English text
- Use spaCy and TextDescriptives library for text analysis
- Integrate TextDescriptives as a spaCy pipeline component
- Process multiple texts and export metrics to DataFrame
- Includes tokenization, POS tagging, dependency parsing, and readability scores

### 📝 `propiedades_linguisticas_spacy_es.ipynb`
**Propiedades Lingüísticas en Español**
- Extract linguistic features from Spanish text using spaCy
- Analyze tokens, lemmas, part-of-speech tags, and morphology
- Parse syntactic dependencies and named entities
- Traditional NLP approach without requiring API keys
- Demonstrates when to use spaCy vs. LLMs for linguistic analysis

### 🎭 `sentiment_analysis_emotion_recognition.ipynb`
**Sentiment Analysis and Emotion Classification (Pre-trained)**
- Use pre-trained transformer models for sentiment analysis
- Classify emotions in text using RoBERTa-based models
- Leverage Hugging Face transformers library and pipelines
- GPU acceleration support for faster processing
- Apply models to analyze emotional content in text data

### 🌐 `reddit_download.ipynb`
**Reddit Data Collection**
- Download posts and comments from Reddit using the PRAW library
- Search and filter subreddits based on topics
- Extract metadata including timestamps, scores, and author information
- Save Reddit data to structured formats for analysis
- Includes rate limiting and error handling

### 🔑 `api_keys.py`
**API Key Configuration**
- Stores API keys for various services (OpenRouter, Reddit, etc.)
- **Note**: Keep this file private and never commit it to public repositories
- Add to `.gitignore` to prevent accidental exposure

## Data

### `data/output/`
- `openrouter_results.csv` - Results from LLM API calls

## Getting Started running on your local computer

1. Open terminal, create and activate the virtual environment:
```bash
python -m venv llm_course
source llm_course/bin/activate  # On macOS/Linux
# or
llm_course\Scripts\activate  # On Windows
```

2. Install required dependencies:
```bash
pip install sentence-transformers umap-learn plotly pandas
pip install spacy textdescriptives
pip install transformers torch
pip install praw
pip install presidio-analyzer presidio-anonymizer
python -m spacy download en_core_web_lg
python -m spacy download es_core_news_sm
```

3. Configure API keys in `api_keys.py` (if needed)

4. Open Jupyter notebooks



