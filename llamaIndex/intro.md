# What Makes LlamaIndex Special?

While LlamaIndex does some things similar to other frameworks like smolagents, it has some key benefits:
### Clear Workflow System: Workflows help break down how agents should make decisions step by step using an event-driven and async-first syntax. This helps you clearly compose and organize your logic.
### Advanced Document Parsing with LlamaParse: LlamaParse was made specifically for LlamaIndex, so the integration is seamless, although it is a paid feature.
### Many Ready-to-Use Components: LlamaIndex has been around for a while, so it works with lots of other frameworks. This means it has many tested and reliable components, like LLMs, retrievers, indexes, and more.
### LlamaHub: is a registry of hundreds of these components, agents, and tools that you can use within LlamaIndex.



### LlamaHub is a registry of hundreds of integrations, agents and tools that you can use within LlamaIndex.


```
pip install llama-index-{component-type}-{framework-name}
```

Query engine is key component for building agentic RAG workflows


# Key stages in creating a RAG pipline using component
- Loading
    - SimpleDirectoryReader
    ```
    from llama_index.core import SimpleDirectoryReader

    reader = SimpleDirectoryReader(input_dir="path/to/directory")
    documents = reader.load_data()
    ```
    - LlamaParse
    - LlamaHub

    After loading data, they need to split into Smalelr Nodes, which is chunk of text with reference to original Document object
    Using IngestionPipeline (chromaDB for storing vectorEmbeddings) it can be done in two ways
    - SentenceSplitter - smaller sentence boundaries
    - HugginFaceEmbedding - vector embedding for LLM to read easily


    ```
    from llama_index.core import Document
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.core.node_parser import SentenceSplitter
    from llama_index.core.ingestion import IngestionPipeline

    # create the pipeline with transformations
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_overlap=0),
            HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5"),
        ]
    )

    nodes = await pipeline.arun(documents=[Document.example()])

    ```
- Indexing
- Storing - chromaDB as vector embedding
- Querying
    - as_retriever - basic document retrieval
    - as_query_engine - single question-answer interaction
    - as_chat_engine - for conversation with conect across multiplem messages with a written chat reeponse

    ## Respone Processing
    - refine
    - compact
    - tree_summarize
- Evaludation
    - FaithfulnessEvaluator
    - AnswerRelevancyEvaluator
    - CorrectnessEvaluator




# Tools in LlamaIndex

- Function Tool
- Search Engine - QueryEngineTool
- Toolspecs - GoogleToolSpec
- Utility Tools
    - OnDemandToolLoader
    - LoadAndSearchToolSpec

# Three main types of reasoning agents in LlamaIndex

- Function Calling
- ReAct framework
- Advanced Custom Agents