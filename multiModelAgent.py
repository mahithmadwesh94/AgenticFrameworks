import os
from PIL import Image
from smolagents import CodeAgent, GoogleSearchTool, InferenceClientModel, VisitWebpageTool,DuckDuckGoSearchTool
from tools.cargo_travel_time import calculate_cargo_travel_time

SERP_TOKEN = os.environ.get("SERP_API_KEY")
HF_TOKEN = os.environ.get("HF_TOKEN")
SERPAPI_API_KEY = os.environ.get("SERPAPI_API_KEY")

model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

task = """Find all Batman filming locations in the world, calculate the time to transfer via cargo plane to here (we're in Gotham, 40.7128° N, 74.0060° W), and return them to me as a pandas dataframe.
Also give me some supercar factories with the same cargo plane transfer time."""


agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool(), VisitWebpageTool(), calculate_cargo_travel_time],
    additional_authorized_imports=["pandas"],
    max_steps=20,
)

result = agent.run(task)

print(result)
