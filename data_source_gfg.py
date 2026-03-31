import requests
from bs4 import BeautifulSoup
import time


class GFGDataSource:
    """
    Data source for extracting questions from GeeksforGeeks.
    This is a prototype implementation for demonstration.
    """

    BASE_URL = "https://www.geeksforgeeks.org"

    def __init__(self, delay=1.0):
        self.delay = delay  # polite delay to avoid rate limits

    def fetch_article(self, url):
        """Fetch HTML content from GFG article"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"[ERROR] Failed to fetch URL: {url}")
            print(e)
            return None

    def parse_questions(self, html):
        """Parse questions from GFG article HTML"""
        soup = BeautifulSoup(html, "html.parser")

        questions = []

        # GFG articles often use <li> or <p> for questions
        elements = soup.find_all(["p", "li"])

        for idx, el in enumerate(elements):
            text = el.get_text(strip=True)

            # Basic filtering (avoid junk text)
            if len(text) > 40 and "?" in text:
                questions.append({
                    "id": f"gfg_{idx}",
                    "question": text,
                    "source": "geeksforgeeks"
                })

        return questions

    def get_questions_from_url(self, url):
        """Full pipeline: fetch + parse"""
        html = self.fetch_article(url)
        if not html:
            return []

        time.sleep(self.delay)  # avoid aggressive scraping

        return self.parse_questions(html)


# 🔥 DEMO USAGE
if __name__ == "__main__":
    gfg = GFGDataSource()

    test_url = "https://www.geeksforgeeks.org/data-structures/"
    questions = gfg.get_questions_from_url(test_url)

    print(f"\nExtracted {len(questions)} questions:\n")

    for q in questions[:5]:
        print("-", q["question"])
