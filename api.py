import openai
from keys import apikey
import os

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

