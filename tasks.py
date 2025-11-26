from crewai import Task
from tools import yt_tool
from agents import content_researcher,content_writer

#RESERCHING TASK
blog_researching=Task(
    description="research the vedio {vedio} content",
    expected_output="containing the matching {vedio} research",
    tools=[yt_tool],
    agent=content_researcher,
)

#content wriitng task
bolg_writer=Task(

 description="write the vedio {vedio} content",
    expected_output="refined  {vedio} research content and add it in blog file ",
    tools=[yt_tool],
    agent=content_writer,
    async_execution=False,
    output_file='new-blog.md',
)