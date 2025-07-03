import openai
from abc import ABC,abstractmethod
import loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()
open.api_key = os.getenv('OPENAI_API_KEY')