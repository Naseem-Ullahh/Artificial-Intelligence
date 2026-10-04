from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

template = PromptTemplate.from_template(
    "You are an assistant for an AI course. Answer the following question in 2 sentences: {question}"
)
prompt = template.format(question="What is the difference between supervised and unsupervised learning?")    
print(prompt)
response = llm.invoke(prompt)
print(response.text)
print(response.content[0]["text"])