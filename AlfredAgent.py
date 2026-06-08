from smolagents import LiteLLMModel,CodeAgent,WebSearchTool,Tool,GradioUI
import os
import yaml
import time
import datetime


model = LiteLLMModel(
        model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
        api_base="http://127.0.0.1:11434",  # Default Ollama local server
        num_ctx=8192,

)




# Get current directory path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

from tools.web_search import DuckDuckGoSearchTool as WebSearch
from tools.visit_webpage import VisitWebpageTool as VisitWebpage
from tools.suggest_menu import SimpleTool as SuggestMenu
from tools.catering_service_tool import SimpleTool as CateringServiceTool
from tools.superhero_party_theme_generator import SuperheroPartyThemeTool as SuperheroPartyThemeGenerator
from tools.final_answer import FinalAnswerTool as FinalAnswer


web_search = WebSearch()
visit_webpage = VisitWebpage()
suggest_menu = SuggestMenu()
catering_service_tool = CateringServiceTool()
superhero_party_theme_generator = SuperheroPartyThemeGenerator()
final_answer = FinalAnswer()

with open(os.path.join(CURRENT_DIR, "prompts.yaml"), 'r') as stream:
    prompt_templates = yaml.safe_load(stream)

agent = CodeAgent(
    model=model,
    tools=[web_search, visit_webpage, suggest_menu, catering_service_tool, superhero_party_theme_generator],
    max_steps=10,
    prompt_templates=prompt_templates,
    additional_authorized_imports=['datetime']

)



GradioUI(agent).launch()

