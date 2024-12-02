import os
from dotenv import load_dotenv
load_dotenv()

class Config:
  ENDPOINT = os.getenv("ENDPOINT")
  KEY = os.getenv("SUBSCRIPTION_KEY")
  VERSION = os.getenv("VERSION")
  NAME = os.getenv("NAME")