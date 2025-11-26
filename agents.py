from crewai import Agent
from tools import yt_tool
from crewai import LLM
from dotenv import load_dotenv
load_dotenv()
import os
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

os.environ['OPENAI_MODEL_NAME']=os.getenv("OPENAI_MODEL_NAME")

llm = LLM(
    model=os.environ["OPENAI_MODEL_NAME"],
    api_key=os.environ["OPENAI_API_KEY"]
)
#first agent ie. content_researcher
content_researcher=Agent(
    role="A youtube vedio researcher  and  content writer",
    goal="make  research regarding youtube vedio by its name ie.{vedio} and  generate the content used in this vedio ",
    backstory="you are good at finding relative vedio from input given and also content  generation from that particular vedio",
    memory=True,
    verbose=True,
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm,


)
#second agent ie. content_researcher
content_writer=Agent(
    role="A youtube vedio researcher  and  content writer",
    goal="make  research regarding youtube vedio by its name ie.{vedio} and  generate the content used in this vedio ",
    backstory="you are good at finding relative vedio from input given and also content  generation from that particular vedio",
    memory=True,
    verbose=True,
    tools=[yt_tool],
 allow_delegation=False,
 llm=llm,

)
