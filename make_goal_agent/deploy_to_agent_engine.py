import os
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv

from agent import root_agent

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    staging_bucket="gs://" + os.getenv("GOOGLE_CLOUD_PROJECT")+"-bucket",
)

# remote_app = agent_engines.create(
#     display_name=os.getenv("APP_NAME", "Agent App"),
#     agent_engine=root_agent,
#     requirements=[
#         "google-cloud-aiplatform[adk,agent_engines]"
#     ]
# )

agent_engines.update(
    resource_name="7560110011192442880",    # Required.
    description="Break down a big goal into small steps",      # Optional.
    display_name="Make Goal Agent",
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]"
    ]
)