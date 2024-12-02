from langchain_openai.chat_models.azure import AzureChatOpenAI
from utils.Config import Config

client = AzureChatOpenAI(
    azure_endpoint = Config.ENDPOINT,
    api_key= Config.KEY,
    api_version=Config.VERSION,
    deployment_name=Config.NAME,
    max_retries=0
    )

def translate_article(text, lang):
  messages = [
      ("system", "Você atua como tradutor de textos"),
      ("user", f"Traduza o {text} para {lang} e responda em markdown")
  ]

  response = client.invoke(messages)
  return response.content