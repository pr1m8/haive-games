Examples
========

This section provides practical examples of using haive-core in various scenarios.

Basic Examples
--------------

Simple Chatbot
~~~~~~~~~~~~~~

A basic conversational agent:

.. exec_code::
   :hide_code:
   :hide_output:

   # This would actually run if we had the environment set up
   print("Example code block that could execute")

.. code-block:: python

   from haive.core.engine.aug_llm import AugLLMConfig
   from haive.core.schema.prebuilt.messages_state import MessagesState
   from haive.core.graph import StateGraph
   
   # Configure the engine
   engine = AugLLMConfig(
       model="gpt-4",
       temperature=0.7,
       system_message="You are a friendly chatbot"
   )
   
   # Create the workflow
   def chat_node(state: MessagesState):
       # Get the last user message
       last_message = state.messages[-1]
       
       # Generate response
       response = engine.invoke(state.messages)
       
       # Add to conversation
       state.messages.append(response)
       return state
   
   # Build the graph
   workflow = StateGraph(MessagesState)
   workflow.add_node("chat", chat_node)
   workflow.set_entry_point("chat")
   workflow.set_finish_point("chat")
   
   # Compile and use
   app = workflow.compile()
   
   # Run conversation
   state = MessagesState()
   state.messages.append({"role": "user", "content": "Hello!"})
   
   result = app.invoke(state)
   print(result.messages[-1]["content"])

Tool-Using Agent
~~~~~~~~~~~~~~~~

An agent that can use tools:

.. code-block:: python

   from langchain_core.tools import tool
   from haive.core.engine.aug_llm import AugLLMConfig
   import datetime
   import requests
   
   # Define tools
   @tool
   def get_current_time() -> str:
       """Get the current date and time."""
       return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
   @tool
   def get_weather(city: str) -> str:
       """Get weather for a city."""
       # Simplified example
       return f"The weather in {city} is sunny and 72°F"
   
   @tool
   def calculate(expression: str) -> str:
       """Calculate mathematical expressions."""
       try:
           result = eval(expression)
           return str(result)
       except:
           return "Invalid expression"
   
   # Create agent with tools
   engine = AugLLMConfig(
       model="gpt-4",
       temperature=0.3,
       tools=[get_current_time, get_weather, calculate],
       tool_choice="auto"
   )
   
   # Use the agent
   response = engine.invoke([
       {"role": "user", "content": "What's the weather in Paris and what time is it?"}
   ])

Structured Output Agent
~~~~~~~~~~~~~~~~~~~~~~~

An agent that returns typed responses:

.. code-block:: python

   from pydantic import BaseModel, Field
   from typing import List, Optional
   from haive.core.engine.aug_llm import AugLLMConfig
   
   # Define output schema
   class AnalysisResult(BaseModel):
       sentiment: str = Field(description="positive, negative, or neutral")
       confidence: float = Field(ge=0.0, le=1.0)
       key_topics: List[str] = Field(description="Main topics discussed")
       summary: str = Field(max_length=200)
       action_items: Optional[List[str]] = None
   
   # Configure engine with structured output
   engine = AugLLMConfig(
       model="gpt-4",
       temperature=0.3,
       structured_output_model=AnalysisResult,
       system_message="You are a text analysis expert"
   )
   
   # Analyze text
   text = """
   The quarterly meeting went well. Sales are up 15% and the team 
   is motivated. We need to hire two more engineers and update 
   the documentation. Everyone seemed happy with the progress.
   """
   
   result = engine.invoke([
       {"role": "user", "content": f"Analyze this text: {text}"}
   ])
   
   # result is now an AnalysisResult instance
   print(f"Sentiment: {result.sentiment} (confidence: {result.confidence})")
   print(f"Key topics: {', '.join(result.key_topics)}")
   print(f"Action items: {result.action_items}")

Advanced Examples
-----------------

Multi-Step Workflow
~~~~~~~~~~~~~~~~~~~

A complex workflow with multiple processing steps:

.. code-block:: python

   from haive.core.graph import StateGraph
   from haive.core.schema.state_schema import StateSchema
   from pydantic import Field
   from typing import List, Dict, Any
   
   # Define custom state
   class ResearchState(StateSchema):
       query: str = Field(description="User's research query")
       search_results: List[Dict] = Field(default_factory=list)
       analysis: str = Field(default="")
       summary: str = Field(default="")
       citations: List[str] = Field(default_factory=list)
   
   # Define workflow nodes
   def search_node(state: ResearchState):
       """Search for information."""
       # Simulate search
       state.search_results = [
           {"title": "Result 1", "content": "Information about " + state.query},
           {"title": "Result 2", "content": "More details on " + state.query}
       ]
       return state
   
   def analyze_node(state: ResearchState):
       """Analyze search results."""
       # Use LLM to analyze
       engine = AugLLMConfig(model="gpt-4", temperature=0.3)
       
       analysis_prompt = f"""
       Analyze these search results for the query: {state.query}
       
       Results:
       {state.search_results}
       
       Provide a comprehensive analysis.
       """
       
       response = engine.invoke([{"role": "user", "content": analysis_prompt}])
       state.analysis = response["content"]
       return state
   
   def summarize_node(state: ResearchState):
       """Create final summary."""
       engine = AugLLMConfig(model="gpt-4", temperature=0.5)
       
       summary_prompt = f"""
       Based on this analysis, create a concise summary:
       
       {state.analysis}
       
       Include key findings and recommendations.
       """
       
       response = engine.invoke([{"role": "user", "content": summary_prompt}])
       state.summary = response["content"]
       
       # Extract citations
       state.citations = ["Source 1", "Source 2"]  # Simplified
       return state
   
   # Build the workflow
   workflow = StateGraph(ResearchState)
   workflow.add_node("search", search_node)
   workflow.add_node("analyze", analyze_node)
   workflow.add_node("summarize", summarize_node)
   
   # Define flow
   workflow.set_entry_point("search")
   workflow.add_edge("search", "analyze")
   workflow.add_edge("analyze", "summarize")
   workflow.set_finish_point("summarize")
   
   # Execute
   app = workflow.compile()
   initial_state = ResearchState(query="AI safety research")
   final_state = app.invoke(initial_state)
   
   print(final_state.summary)

Conditional Routing
~~~~~~~~~~~~~~~~~~~

Dynamic workflow based on conditions:

.. code-block:: python

   from haive.core.graph import StateGraph, END
   from typing import Literal
   
   class RouterState(StateSchema):
       user_input: str
       intent: str = ""
       response: str = ""
       needs_clarification: bool = False
   
   def classify_intent(state: RouterState) -> str:
       """Classify user intent and route accordingly."""
       engine = AugLLMConfig(model="gpt-4", temperature=0.1)
       
       classification = engine.invoke([{
           "role": "user",
           "content": f"Classify this intent as 'question', 'command', or 'conversation': {state.user_input}"
       }])
       
       state.intent = classification["content"].lower()
       
       # Route based on intent
       if "question" in state.intent:
           return "answer_question"
       elif "command" in state.intent:
           return "execute_command"
       else:
           return "chat"
   
   def answer_question(state: RouterState):
       """Handle questions with research."""
       # Research and answer logic
       state.response = f"Here's the answer to your question about {state.user_input}"
       return state
   
   def execute_command(state: RouterState):
       """Execute user commands."""
       # Command execution logic
       state.response = f"Executing command: {state.user_input}"
       return state
   
   def chat(state: RouterState):
       """Handle general conversation."""
       # Conversational response
       state.response = f"Let's chat about {state.user_input}"
       return state
   
   def check_clarity(state: RouterState) -> str:
       """Check if response needs clarification."""
       if state.needs_clarification:
           return "clarify"
       return END
   
   def clarify(state: RouterState):
       """Add clarification to response."""
       state.response += "\n\nWould you like me to elaborate on any part?"
       return state
   
   # Build conditional workflow
   workflow = StateGraph(RouterState)
   
   # Add nodes
   workflow.add_node("classify", classify_intent)
   workflow.add_node("answer_question", answer_question)
   workflow.add_node("execute_command", execute_command)
   workflow.add_node("chat", chat)
   workflow.add_node("clarify", clarify)
   
   # Add conditional routing
   workflow.set_entry_point("classify")
   workflow.add_conditional_edges(
       "classify",
       classify_intent,  # This function returns the route
       {
           "answer_question": "answer_question",
           "execute_command": "execute_command",
           "chat": "chat"
       }
   )
   
   # All paths lead to clarity check
   workflow.add_edge("answer_question", "check_clarity")
   workflow.add_edge("execute_command", "check_clarity")
   workflow.add_edge("chat", "check_clarity")
   
   # Conditional finish
   workflow.add_conditional_edges(
       "check_clarity",
       check_clarity,
       {
           "clarify": "clarify",
           END: END
       }
   )

RAG (Retrieval-Augmented Generation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Building a RAG system:

.. code-block:: python

   from haive.core.engine.vectorstore import VectorStoreConfig
   from haive.core.engine.aug_llm import AugLLMConfig
   from langchain_core.documents import Document
   
   # Configure vector store
   vector_config = VectorStoreConfig(
       provider="chroma",
       collection_name="knowledge_base",
       embedding_model="text-embedding-ada-002"
   )
   
   # Create vector store
   vector_store = vector_config.create_store()
   
   # Add documents
   documents = [
       Document(
           page_content="Haive is an AI agent framework for building intelligent systems.",
           metadata={"source": "intro.md", "section": "overview"}
       ),
       Document(
           page_content="Agents in Haive can use tools, maintain state, and work together.",
           metadata={"source": "concepts.md", "section": "agents"}
       ),
       # Add more documents...
   ]
   
   vector_store.add_documents(documents)
   
   # Create RAG chain
   class RAGState(StateSchema):
       question: str
       context: List[str] = Field(default_factory=list)
       answer: str = ""
   
   def retrieve_context(state: RAGState):
       """Retrieve relevant documents."""
       results = vector_store.similarity_search(
           state.question,
           k=3  # Top 3 results
       )
       state.context = [doc.page_content for doc in results]
       return state
   
   def generate_answer(state: RAGState):
       """Generate answer using context."""
       engine = AugLLMConfig(
           model="gpt-4",
           temperature=0.3,
           system_message="Answer questions based on the provided context."
       )
       
       prompt = f"""
       Context:
       {chr(10).join(state.context)}
       
       Question: {state.question}
       
       Answer based on the context provided.
       """
       
       response = engine.invoke([{"role": "user", "content": prompt}])
       state.answer = response["content"]
       return state
   
   # Build RAG workflow
   rag_workflow = StateGraph(RAGState)
   rag_workflow.add_node("retrieve", retrieve_context)
   rag_workflow.add_node("generate", generate_answer)
   rag_workflow.set_entry_point("retrieve")
   rag_workflow.add_edge("retrieve", "generate")
   rag_workflow.set_finish_point("generate")
   
   # Use RAG system
   rag_app = rag_workflow.compile()
   result = rag_app.invoke(RAGState(question="What is Haive?"))
   print(result.answer)

Integration Examples
--------------------

FastAPI Integration
~~~~~~~~~~~~~~~~~~~

Integrate haive-core with FastAPI:

.. code-block:: python

   from fastapi import FastAPI, HTTPException
   from pydantic import BaseModel
   from haive.core.engine.aug_llm import AugLLMConfig
   from haive.core.schema.prebuilt.messages_state import MessagesState
   from typing import List, Dict
   
   app = FastAPI()
   
   # Configure engine
   engine = AugLLMConfig(
       model="gpt-4",
       temperature=0.7,
       system_message="You are a helpful API assistant"
   )
   
   # Request/Response models
   class ChatRequest(BaseModel):
       messages: List[Dict[str, str]]
       temperature: float = 0.7
   
   class ChatResponse(BaseModel):
       response: str
       usage: Dict[str, int]
   
   # Chat endpoint
   @app.post("/chat", response_model=ChatResponse)
   async def chat(request: ChatRequest):
       try:
           # Update temperature if provided
           engine.temperature = request.temperature
           
           # Generate response
           response = engine.invoke(request.messages)
           
           return ChatResponse(
               response=response["content"],
               usage={
                   "prompt_tokens": response.get("usage", {}).get("prompt_tokens", 0),
                   "completion_tokens": response.get("usage", {}).get("completion_tokens", 0)
               }
           )
       except Exception as e:
           raise HTTPException(status_code=500, detail=str(e))
   
   # Streaming endpoint
   @app.post("/chat/stream")
   async def chat_stream(request: ChatRequest):
       async def generate():
           engine.streaming = True
           stream = engine.stream(request.messages)
           
           for chunk in stream:
               yield f"data: {chunk}\n\n"
       
       return StreamingResponse(generate(), media_type="text/event-stream")

Gradio Interface
~~~~~~~~~~~~~~~~

Create a UI with Gradio:

.. code-block:: python

   import gradio as gr
   from haive.core.engine.aug_llm import AugLLMConfig
   from haive.core.schema.prebuilt.messages_state import MessagesState
   
   # Initialize engine
   engine = AugLLMConfig(
       model="gpt-4",
       temperature=0.7,
       system_message="You are a helpful assistant"
   )
   
   # Keep conversation state
   conversation_state = MessagesState()
   
   def chat_interface(message, history):
       """Gradio chat interface."""
       # Add user message
       conversation_state.messages.append({
           "role": "user",
           "content": message
       })
       
       # Generate response
       response = engine.invoke(conversation_state.messages)
       
       # Add assistant response
       conversation_state.messages.append(response)
       
       # Update history for Gradio
       history.append((message, response["content"]))
       
       return "", history
   
   def clear_conversation():
       """Reset conversation."""
       conversation_state.messages.clear()
       return []
   
   # Create Gradio interface
   with gr.Blocks() as demo:
       gr.Markdown("# Haive Chat Interface")
       
       chatbot = gr.Chatbot()
       msg = gr.Textbox(
           label="Your message",
           placeholder="Type your message here..."
       )
       
       with gr.Row():
           submit = gr.Button("Send")
           clear = gr.Button("Clear")
       
       # Event handlers
       submit.click(
           chat_interface,
           inputs=[msg, chatbot],
           outputs=[msg, chatbot]
       )
       
       msg.submit(
           chat_interface,
           inputs=[msg, chatbot],
           outputs=[msg, chatbot]
       )
       
       clear.click(
           clear_conversation,
           outputs=[chatbot]
       )
   
   demo.launch()

Testing Examples
----------------

Unit Testing Agents
~~~~~~~~~~~~~~~~~~~

Test agents with real components:

.. code-block:: python

   import pytest
   from haive.core.engine.aug_llm import AugLLMConfig
   from haive.core.schema.prebuilt.messages_state import MessagesState
   
   class TestChatAgent:
       @pytest.fixture
       def engine(self):
           """Create test engine."""
           return AugLLMConfig(
               model="gpt-4",
               temperature=0.1,  # Low for consistency
               max_tokens=100
           )
       
       @pytest.fixture
       def state(self):
           """Create test state."""
           return MessagesState()
       
       def test_agent_responds_to_greeting(self, engine, state):
           """Test agent handles greetings."""
           state.messages.append({
               "role": "user",
               "content": "Hello!"
           })
           
           response = engine.invoke(state.messages)
           
           assert response["role"] == "assistant"
           assert len(response["content"]) > 0
           assert any(word in response["content"].lower() 
                     for word in ["hello", "hi", "greetings"])
       
       def test_agent_maintains_context(self, engine, state):
           """Test conversation context."""
           # First message
           state.messages.append({
               "role": "user",
               "content": "My name is Alice"
           })
           
           response1 = engine.invoke(state.messages)
           state.messages.append(response1)
           
           # Second message
           state.messages.append({
               "role": "user",
               "content": "What's my name?"
           })
           
           response2 = engine.invoke(state.messages)
           
           assert "alice" in response2["content"].lower()
       
       def test_agent_uses_tools(self):
           """Test tool usage."""
           from langchain_core.tools import tool
           
           @tool
           def get_time() -> str:
               """Get current time."""
               return "2024-01-15 10:30:00"
           
           engine = AugLLMConfig(
               model="gpt-4",
               temperature=0.1,
               tools=[get_time]
           )
           
           response = engine.invoke([{
               "role": "user",
               "content": "What time is it?"
           }])
           
           assert "10:30" in response["content"]

Performance Testing
~~~~~~~~~~~~~~~~~~~

Test performance characteristics:

.. code-block:: python

   import time
   import asyncio
   from haive.core.engine.aug_llm import AugLLMConfig
   
   async def test_concurrent_requests():
       """Test concurrent request handling."""
       engine = AugLLMConfig(
           model="gpt-4",
           temperature=0.7,
           max_tokens=50
       )
       
       async def make_request(index: int):
           start = time.time()
           response = await engine.ainvoke([{
               "role": "user",
               "content": f"Count to {index}"
           }])
           duration = time.time() - start
           return duration
       
       # Make 10 concurrent requests
       tasks = [make_request(i) for i in range(1, 11)]
       durations = await asyncio.gather(*tasks)
       
       print(f"Average response time: {sum(durations) / len(durations):.2f}s")
       print(f"Total time for 10 requests: {max(durations):.2f}s")

Next Steps
----------

- Explore more in the :doc:`API Reference <autoapi/haive/index>`
- Check the `examples/` directory in the repository
- Join our community for more examples and support