import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
      text = soup.get_text(separator= ' ')
      lines = (line.strip() for line in text.splitlines())
      chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
      text = '\n'.join(chunk for chunk in chunks if chunk)
      return text
    else:
      print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
      return None