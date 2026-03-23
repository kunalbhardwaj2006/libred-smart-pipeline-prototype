import requests
from bs4 import BeautifulSoup


def fetch_gfg_questions(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        questions = []

        for item in soup.find_all("div", class_="problem-container"):
            q_text = item.get_text(strip=True)
            questions.append(q_text)

        return questions

    except Exception as e:
        print(f"Error fetching GFG data: {e}")
        return []


if name == "__main__":
    url = "https://www.geeksforgeeks.org/gate-cs-notes-gq/"
    data = fetch_gfg_questions(url)

    print(f"Fetched {len(data)} questions")
