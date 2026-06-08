from langchain.agents import load_tools
import os
from smolagents import Tool, CodeAgent,LiteLLMModel,GradioUI


SERP_TOKEN = os.environ.get("SERP_API_KEY")
search_tool = Tool.from_langchain(load_tools(["serpapi"])[0])

model = LiteLLMModel(
        model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
        api_base="http://127.0.0.1:11434",  # Default Ollama local server
        num_ctx=8192,

)

agent = CodeAgent(tools=[search_tool], model=model)



agent.run("What is the name of the new version of God of War games coming up?")

GradioUI(agent).launch()
