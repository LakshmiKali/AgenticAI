from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent,tool
from langchain_community.tools import TavilySearchResults
import datetime

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S)"):
    """ Return the current date and time in specified format"""
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

load_dotenv()
llm = ChatOpenAI()
search_tool = TavilySearchResults()

agent = initialize_agent(tools=[search_tool,get_system_time],llm=llm,agent="zero-shot-react-description",verbose=True)
agent.invoke("When was SpaceeX's last launch and how many days ago was that from this instant")
# results = llm.invoke("Give me a tweet about today's weather in Salem Tamilnadu")
# print(results)