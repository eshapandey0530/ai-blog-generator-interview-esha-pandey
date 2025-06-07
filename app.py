from flask import Flask, request, jsonify
from seo_fetcher import fetch_seo_metrics
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import os

app = Flask(__name__)

# Daily blog post generator
def generate_and_save_daily_blog():
    keyword = "wireless earbuds"   # You can change this default keyword
    seo_data = fetch_seo_metrics(keyword)
    blog_post = generate_blog_post(keyword, seo_data)

    today = datetime.date.today()
    filename = f"daily_blog_{today}.md"

    # Save the blog post to a file
    with open(filename, "w") as f:
        f.write(blog_post)

    print(f"✅ Daily blog post for '{keyword}' saved as {filename}.")

# API Route
@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required as a query parameter."}), 400
    
    # Step 1: Mock SEO Research
    seo_data = fetch_seo_metrics(keyword)

    # Step 2: Generate Blog Post
    blog_post = generate_blog_post(keyword, seo_data)

    # Step 3: Return as JSON
    return jsonify({
        "keyword": keyword,
        "seo": seo_data,
        "blog_post": blog_post
    })

if __name__ == '__main__':
    # Setup Scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=generate_and_save_daily_blog, trigger="interval", days=1)
    scheduler.start()

    # Run Flask app
    app.run(debug=True)