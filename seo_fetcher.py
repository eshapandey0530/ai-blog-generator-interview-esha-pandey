import random

def fetch_seo_metrics(keyword):
    """
    Simulates SEO research by returning random SEO metrics for a given keyword.
    """
    seo_data = {
        "search_volume": random.randint(1000, 50000),          # Random search volume between 1K and 50K
        "keyword_difficulty": round(random.uniform(10.0, 80.0), 2),  # Difficulty score between 10 and 80
        "avg_cpc": round(random.uniform(0.5, 10.0), 2)          # CPC between $0.5 and $10
    }
    return seo_data