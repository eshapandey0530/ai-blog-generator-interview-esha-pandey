from seo_fetcher import fetch_seo_metrics
from ai_generator import generate_blog_post

# Example keyword
keyword = "wireless earbuds"

# Step 1: Fetch mock SEO metrics
seo_data = fetch_seo_metrics(keyword)
print("SEO Data:", seo_data)

# Step 2: Generate blog post
blog_post = generate_blog_post(keyword, seo_data)
print("\nGenerated Blog Post:\n")
print(blog_post)