from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import initialize_agent, AgentType
from langchain_core.tools import Tool


load_dotenv()

llm =  ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

def calculator(expression:str) ->str:
    """Evaluates a mathematical expression and returns the result as a string."""
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error evaluating expression: {e}"

def word_length(word:str) -> str:
    """Return the number of letters  in a word."""
    return str(len(word))

tools = [
    Tool(name="Calculator", func=calculator,
         description="Useful for evaluating arithmetic expressions like '23*7+1'"),
    Tool(name="WordLength", func=word_length,
         description="Useful for finding the number of letters in a word"),
]
agent = initialize_agent(
    tools, llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
result = agent.invoke({"input": "What is the length of the word 'Intelligence' multiplied by 12?"})
print(result["output"])