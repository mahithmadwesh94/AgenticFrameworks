# what is an agent?

AI model capable of reasoning, planning, and interacting with its environment.

# What is an LLM?

- An LLM is a type of AI model that excels at understanding and generating human language\
- LLMs are typically decoder-based models with billions of parameters

## System Messages
System messages (also called System Prompts) define how the model should behave. They serve as persistent instructions, guiding every subsequent interaction.

```
system_message = {
    "role": "system",
    "content": "You are a professional customer service agent. Always be polite, clear, and helpful."
}
```

When using Agents, the System Message also gives information about the available tools, provides instructions to the model on how to format the actions to take, and includes guidelines on how the thought process should be segmented.

# Chat templates
To make a Base Model behave like an instruct model, we need to format our prompts in a consistent way that the model can understand. This is where chat templates come in.

ChatML is one such template format that structures conversations with clear role indicators (system, user, assistant). If you have interacted with some AI API lately, you know that’s the standard practice.
```
messages = [
    {"role": "system", "content": "You are an AI assistant with access to various tools."},
    {"role": "user", "content": "Hi !"},
    {"role": "assistant", "content": "Hi human, what can help you with ?"},
]
```

To convert the previous conversation into a prompt, we load the tokenizer and call apply_chat_template:

```
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-1.7B-Instruct")
rendered_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

# What are tools?

An LLM should have a tool to perform a pirticular action so that it gives accurate reponses instead of depending on native capabilities or answers with an hallucination

```
Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
```


- A descriptive name of what it does: calculator
- A longer description, provided by the function’s docstring comment: Multiply two integers.
- The inputs and their type: the function clearly expects two ints.
- The type of the output.


```
@tool
def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

print(calculator.to_string())
```

# MCP

Model Context Protocol (MCP) is an open protocol that standardizes how applications provide tools to LLMs. MCP provides:

A growing list of pre-built integrations that your LLM can directly plug into
The flexibility to switch between LLM providers and vendors
Best practices for securing your data within your infrastructure


Thought - Action - Observation Cycle

# ReAct Approach for Agents
Thoughts represent agents internal reasoning and planning process to perform an action

# Chain-of-thought

Chain-of-Thought (CoT) is a prompting technique that guides a model to think through a problem step-by-step before producing a final answer.


