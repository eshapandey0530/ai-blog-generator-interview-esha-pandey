# AI Blog Generator

A Flask-based application that generates AI-powered blog posts with mock SEO research, plus a daily scheduled blog generation.

## 🚀 Features
- Generate blog posts for any keyword using OpenAI.
- Mock SEO research data: search volume, keyword difficulty, CPC.
- Daily automated blog post generation using APScheduler.

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ai-blog-generator-interview-esha-pandey.git
   cd ai-blog-generator-interview-esha-pandey

2.	**Create and activate a virtual environment**
    python3 -m venv venv
    source venv/bin/activate     # For Mac/Linux
    # OR
    venv\Scripts\activate        # For Windows

3. **Install dependencies**
    pip install -r requirements.txt

4. **Set up environment variable**
    Create a .env file in the project root with: OPENAI_API_KEY=your_openai_api_key_here

5. **Run the app**
    python app.py

6. **Access the API**
    # example: wireless earbuds
    Open in your browser: http://localhost:5000/generate?keyword=wireless+earbuds 