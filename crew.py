from crewai import Crew,Process

from tasks import blog_researching,bolg_writer
from agents import content_researcher ,content_writer
crew= Crew(tasks =[blog_researching,bolg_writer],
    agents=[content_researcher ,content_writer],
    process=Process.sequential,
    memory=True,
    cache=True,
    share_crew=True,
    max_rpm=100,
)

result= crew.kickoff(inputs={'vedio':'Shaadi Phir Barbaadi '})
print(result)