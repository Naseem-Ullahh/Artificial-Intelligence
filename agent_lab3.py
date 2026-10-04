import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import initialize_agent, AgentType
from langchain_core.tools import Tool

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

def calculator(expression: str) -> str:
    """Evaluates a basic arithmetic expression."""
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: {e}"


def word_length(word: str) -> str:
    """Returns the number of letters in a word."""
    return str(len(word))


def celsius_to_fahrenheit(celsius: str) -> str:
    """Converts a temperature from Celsius to Fahrenheit."""
    try:
        c = float(celsius)
        return str(c * 9 / 5 + 32)
    except ValueError:
        return "Error: input must be a number like '25'"


tools = [
    Tool(name="Calculator", func=calculator,
         description="Useful for evaluating arithmetic expressions like '23*7+1'"),
    Tool(name="WordLength", func=word_length,
         description="Useful for finding the number of letters in a word"),
    Tool(name="CelsiusToFahrenheit", func=celsius_to_fahrenheit,
         description="Useful for converting a temperature from Celsius to Fahrenheit. Input must be only a number, like '25'."),
]

agent = initialize_agent(
    tools, llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

queries = [
    "What is the length of the word 'Intelligence' multiplied by 12?",
    "What is 23*7+1?",
    "What is 37 degrees Celsius in Fahrenheit?",
    "Convert 100 Celsius to Fahrenheit, then add the length of the word 'Agent' to it.",
]

for q in queries:
    print("\n" + "=" * 60)
    print("QUESTION:", q)
    result = agent.invoke({"input": q})
    print("FINAL:", result["output"])
    time.sleep(10)