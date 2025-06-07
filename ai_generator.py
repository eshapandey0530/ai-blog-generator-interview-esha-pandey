import openai
import os

# Load API key
from dotenv import load_dotenv
load_dotenv()
print("🔑 Loaded API key:", os.getenv("OPENAI_API_KEY")[:8])

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(keyword, seo_data):
    """
    Generates a blog post for the given keyword using OpenAI API (new 1.x style).
    Returns Markdown text.
    """
    prompt = f"""
Write a detailed, SEO-optimized blog post about "{keyword}".
Incorporate:
- Search Volume: {seo_data['search_volume']}
- Keyword Difficulty: {seo_data['keyword_difficulty']}
- Average CPC: ${seo_data['avg_cpc']}

Include:
- Introduction
- 3-5 Subheadings
- Conclusion
- Insert affiliate placeholders like {{AFF_LINK_1}}, {{AFF_LINK_2}}.
Format in Markdown.
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Or gpt-4 if you have access
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    blog_post = response.choices[0].message.content
    return blog_post