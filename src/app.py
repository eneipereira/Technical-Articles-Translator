from services import extract_text_from_url
from services import article_translator

def main(url):
    text = extract_text_from_url(url)
    article = article_translator(text, "pt-br")
    return article

if __name__ == "__main__":
    url = "https://dev.to/aniruddhaadak/typescript-a-strongly-typed-superset-of-javascript-5fl7"
    print(main(url))