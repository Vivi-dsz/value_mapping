# Brand Strategy AI Assistant

A multi-page AI-powered app for analyzing customer perception, brand communication and comptetion, strategic alignment — built with Streamlit, Transformers, ML Technics, and LLM APIs (OpenAI).

Currently, the app is a brand strategy AI assistant advising brand 'Klarna' on marketing, advertising, and brand management.

---

## Features
- Welcome page
- Brand Analysis
- Customer Analysis
- Compterirors Analysis
- AI-Powered Chatbot

### Agent Chatbot
- Ask brand strategy questions like:
  - "We see decline in new users, can you please tell us what is the current brand strategy and gaps in user perception for Klarna?"
  - "How can Klarna differentiate itself from Bunq to acquire more users?"
  - "We are planning a new brand marketing campaign for autumn and we would like to have a strategic direction and a breakdown on main    channels and messaging"
- Responses are generated using LLMs + preprocessed insights.

### Customer Review Analysis Pipeline
- Customer reviews are scraped from google_play_scraper
- Extracts:
  - Main topics from user reviews:
    Derived by OpenAI for a 1000 uniform sample of reviews, modeled (utilizing XGBoost Classifier) for the rest
  - Sentiment classification (multilingual, model = 'tabularisai/multilingual-sentiment-analysis' from Hugging Face, for further information check https://huggingface.co/tabularisai/multilingual-sentiment-analysis)
- Maps reviews to psychological value categories (e.g., *trust*, *freedom*, *simplicity*, etc.)

### Brand Value Mapping
- Analyzes company brand content (extracted e.g. from their “About Us” page)
- Matches against value keywords (for further information, contact our specialists) to detect the brand positioning
- Compares against how users perceive the brand
- Compares against Klarna's competitors:
  supported_brands = ["Klarna", "N26", "Revolut", "Trade Republic", "Bunq"]

### Visual Insights
- Polar/radar charts for value alignment for each brand based on their positioning
- Polar/radar charts for value alignment for each brand based on user perception
- Heatmaps of sentiment vs topic per brand

### Persistent Memory
- Chatbot remembers conversation across a session

---

## Project Structure
.
├── backend
│   ├── models
│   │   ├── agent.py
│   │   ├── mvpsimplemodel.pkl
│   │   └── xgb_classifier.pkl
│   ├── package
│   │   ├── api_file.py
│   │   ├── dummy.py
│   │   ├── __init__.py
│   │   ├── model_sentiment.py
│   │   ├── predict_topic.py
│   │   └── sentiment_trends.py
│   ├── preprocess
│   │   ├── alignment_score.py
│   │   ├── brand_count_function.py
│   │   ├── build_kw_tables.py
│   │   ├── data_prep.py
│   │   ├── __init__.py
│   │   ├── lem_counter.py
│   │   ├── lemmatizer.py
│   │   ├── openai.py
│   │   ├── params.py
│   │   ├── review_count_function.py
│   │   └── score_sentiment.py
│   ├── scrape
│   │   ├── app_details.py
│   │   └── user_reviews.py
│   └── visualization
│       ├── get_kw_count_df.py
│       ├── kw_2d_reduction.py
│       ├── kw_cat_plot.py
│       ├── kw_count_bubble_plot.py
│       ├── kw_count_polar_plot.py
│       ├── monthly_sentiment_plot.py
│       └── sentiment_heatmap.py
├── data
│   ├── preprocessed
│   │   ├── dataframes.py
│   │   ├── final_reviews_with_topics_and_sentiment.csv
│   │   ├── kw_counted_user_reviews_v01.csv
│   │   ├── merged_review_topics_v01.csv
│   │   ├── openai_topics.csv
│   │   ├── README.md
│   │   └── user_reviews.csv
│   └── raw
│       ├── analysis_results.py
│       ├── bank_details_v01.csv
│       ├── brandcompareinfo.py
│       ├── brands_about_us.py
│       ├── kw_topics_v1.py
│       ├── user_reviews_10k_v01.csv
│       ├── user_reviews_10k_v02.csv
│       └── user_reviews_v01.csv
├── frontend
│   ├── agentapp.py
│   ├── app.py
│   ├── modules
│   │   ├── brandcompareinfo.py
│   │   ├── brandinfo.py
│   │   ├── companydesc.py
│   │   └── navbar.py
│   ├── pages
│   │   ├── brandanalysis.py
│   │   ├── chatbot.py
│   │   ├── companalysis.py
│   │   ├── customeranalysis.py
│   │   └── welcome.py
│   ├── .streamlit
│   │   └── config.toml
│   └── ValueMapApp.py
├── README.md
└── requirements.txt

---

## Setup Instructions

### 1. Clone the Repo

git clone https://github.com/Vivi-dsz/value_mapping.git
cd value_mapping

## Install Dependencies

pip install -r requirements.txt

## Set Up Environment Variables

Create a .env file in the root directory and add your API keys:
OPENAI_API_KEY=openai-key

Attention: Never commit your .env file to version control.

## Run the App

cd frontend
streamlit run app.py

## Team

Frontend:
- Vivien Daszkowski
- Ibrahim Eksi

Backend:
- Liana Gilmanova
- Elnaz Roshan
