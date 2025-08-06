#import os
#from pydantic import BaseModel, Field
#from langchain_openai import ChatOpenAI


#class EmailMessage(BaseModel):
#    subject: str
#    contents: str
#    invalid_request: bool | None = Field(default=False)


#OPENAI_BASE_URL = os.environ.get('OPENAI_BASE_URL') or None
#OPENAI_MODEL_NAME = os.environ.get('OPENAI_MODEL_NAME') or 'gpt-4o-mini'
#if not OPEN_API_KEY:
#    raise NotImplementedError("'OPEN_API_KEY' is required !")

#openai_params = {"model": OPENAI_MODEL_NAME, "api_key":OPEN_API_KEY}
#if OPENAI_BASE_URL:
#   openai_params['base_url'] = OPENAI_BASE_URL


#llm_base = ChatOpenAI(**openai_params)

#llm = llm_base.with_structured_output(EmailMessage)
#messages = [
#    (
#        "system",
#       "You are a helpful assistant for research & composing plaintext emails !"
#   ),
#    ("human","Create an email about the benefits of coffee. Do not use Markdown in your response only plaintext")
#]
#response = llm.invoke(messages)
#print(response)