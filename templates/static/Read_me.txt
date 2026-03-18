AI News Headline Hub
Problem Statement

In today’s digital world, users are overwhelmed with massive amounts of news data from multiple sources. Traditional keyword-based search systems often fail to deliver relevant results because they rely on exact word matching instead of understanding user intent.

There is a need for an intelligent system that:

Provides relevant and meaningful news results

Supports natural language search

Efficiently handles large-scale news data

This project solves the problem by using AI-powered semantic search with a vector database (Endee.io) to improve the accuracy and relevance of news retrieval.

 Workflow
 Step-by-Step Working
Technologies Used

Python (FastAPI)

HTML, CSS

Endee.io (Vector Database)

Uvicorn

News API

▶ How to Run the Project
🔹 Step 1: Clone Repository
git clone https://github.com/YOUR-USERNAME/endee.git
cd endee/ai-news-hub
🔹 Step 2: Create Virtual Environment
Windows:
python -m venv venv
venv\Scripts\activate
Linux/Mac:
python3 -m venv venv
source venv/bin/activate

Data Collection

News is fetched using a News API (India-based headlines).

Preprocessing

Extract headlines, descriptions, and URLs.

Embedding Generation

Convert news text into numerical vectors using AI models.

Vector Storage (Endee.io)

Store embeddings in the vector database.

User Query Input

User enters search query in the website.

Query Embedding

Convert user query into vector format.

Similarity Search

Compare query vector with stored vectors.

Retrieve most relevant news articles.

Display Results

Show results on UI with title, description, and link.

 System Architecture (Simple)
User → Frontend (HTML/CSS)
        ↓
     FastAPI Backend
        ↓
  Endee.io Vector DB
        ↓
   News API (Data Source)
 Features

AI-based semantic search

Real-time Indian news fetching

Fast and efficient backend using FastAPI

Vector similarity search using Endee.io

Clean and colorful user interface

 Advantages / Pros

 Better Search Accuracy
Understands meaning, not just keywords.

 Fast Retrieval
Vector search is highly efficient.

 AI Integration
Uses embeddings for smarter results.

 Scalable
Can handle large datasets.

🇮🇳 Localized Content
Focus on Indian news.
pip install fastapi uvicorn requests jinja2
🔹 Step 4: Set API Keys

In your app.py, add:

NEWS_API_KEY = "your_api_key_here"
ENDEE_API_KEY = "your_endee_api_key"
🔹 Step 5: Run the Server
uvicorn app:app --reload
🔹 Step 6: Open in Browser
http://127.0.0.1:8000
 Project Structure
ai-news-hub/
│
├── app.py
├── vector_store.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
 Conclusion

The AI News Headline Hub demonstrates how AI and vector databases can significantly improve search systems by delivering context-aware and relevant results. This project highlights the practical implementation of semantic search in real-world applications.