# Semantic Book Recommender

AI-driven application that recommends books based on **emotions** detected in user input and whether the user prefers **fiction** or **non-fiction**. This project leverages both OpenAI and Hugging Face APIs to perform text classification and zero-shot classification, respectively. 

![Semantic Book Recommender Screenshot](https://cdn.discordapp.com/attachments/1299155448959598595/1343141855709237288/Screenshot_2025-02-23_004601.png?ex=67bc31d4&is=67bae054&hm=f6e4841ed81406813c22b08d0126c63cc476650d44306866a02bf2090cba4017&)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Contact](#contact)

---

## Overview

The **Semantic Book Recommender** uses **Natural Language Processing (NLP)** techniques to analyze user input and suggest books. It relies on:
1. **Emotion Detection**: Determines the emotional tone (e.g., joy, sadness) of the user’s input.
2. **Genre Classification**: Uses zero-shot classification to categorize the user's query into "Fiction" or "Nonfiction."

By combining these insights, the application surfaces a curated list of book recommendations.

---

## Features

- **Emotion Analysis**: Powered by `j-hartmann/emotion-english-distilroberta-base` for robust emotion classification.
- **Zero-Shot Classification**: Uses `facebook/bart-large-mnli` to distinguish between Fiction and Nonfiction.
- **Interactive Dashboard**: Built with [Gradio](https://gradio.app/) for a user-friendly interface.
- **CSV-based Book Data**: Pre-processed and stored in `books_with_emotions.csv` and `books_with_categories.csv`.

---

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/YourUsername/Book-Recommender.git
   cd Book-Recommender/book_recommender
2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Set Up API Keys**
   - **OpenAI:** Create a ```.env``` file or export your API key as an environment variable:
   ```bash
   OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
   ```
   - **Hugging Face:** If required, configure your token similarly:
   ```bash
   HUGGINGFACEHUB_API_TOKEN="YOUR_HF_API_KEY"

---

## Usage
1. **Run the Gradio Dashboard**
   ```bash
   python3 gradio-dashboard.py
2. **Access the Application**
   - Copy the URL printed in the console (something like ```http://127.0.0.1:7860```).
   - Open it in your browser.
3. **Interact with the Dashboard**
   - Provide a short description of a book you’re looking for, or a phrase that captures your mood.
   - Choose optional categories or let the model handle them automatically.
   - View the recommendations and explore the listed books.

---

## Project Structure
```bash
book_recommender/
├── books_cleaned.csv
├── books_with_categories.csv
├── books_with_emotions.csv
├── cover-not-found.jpg
├── data-exploration.ipynb
├── gradio-dashboard.py
├── requirements.txt
├── sentiment-analysis.ipynb
├── tagged_description.txt
├── text-classification.ipynb
├── vector-search.ipynb
└── ...
```
- ```gradio-dashboard.py:``` Main file to launch the Gradio interface.
- ```books_with_emotions.csv``` and ```books_with_categories.csv:``` Data files used for recommendations.
- ```.ipynb``` **notebook:** Exploratory notebooks showcasing data cleaning, text classification, sentiment analysis, and vector search.

---

## Technical Details
1. **Emotion Classification**
   ```python
   from transformers import pipeline
   classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base")
   # Analyzes the user's text and infers the dominant emotion.
   ```
2. **Zero-Shot Classification**
   ```python
   from transformers import pipeline

   fiction_categories = ["Fiction", "Nonfiction"]
   pipe = pipeline("zero-shot-classification",
                model="facebook/bart-large-mnli")
   # Classifies user input to decide whether they want Fiction or Nonfiction.
   ```
3. **Integration with OpenAI**
   - **OpenAI** is used for any language model queries or text embeddings (depending on your configuration with ```langchain```).
4. **Gradio Frontend**
   - Provides a **web interface** for user input and displays the recommended books.
5. **Data**
   - The CSV files contain pre-labeled or pre-processed metadata about books (title, author, categories, etc.).

---

## Contact
- **Email:** kennygarcia15@yahoo.com
- **LinkedIn:** linkedin.com/in/kennygarcia15
  Feel free to reach out if you have questions, suggestions, or feedback!

---

Thank you for checking out the Semantic Book Recommender. Enjoy exploring new reads tailored to your mood and preferences!
