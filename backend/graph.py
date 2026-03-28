from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

class State(TypedDict):
    input: str
    summary: str
    hooks: str
    post: str
    image_prompt: str

def summarize(state):
    text = state.get("input", "")
    
    if not text:
        raise ValueError(f"Input manquant dans state: {state}")

    res = llm.invoke(f"Résume:\n{text}")
    return {"summary": res.content}

def hooks(state):
    summary = state.get("summary", "")
    
    if not summary:
        raise ValueError(f"Summary manquante dans state: {state}")

    res = llm.invoke(f"3 hooks viraux:\n{summary}")
    return {"hooks": res.content}

def post(state):
    hooks = state.get("hooks", "")
    
    if not hooks:
        raise ValueError(f"Hooks manquants dans state: {state}")

    res = llm.invoke(f"Post LinkedIn:\n{hooks}")
    return {"post": res.content}

def og(state):
    post = state.get("post", "")
    
    if not post:
        raise ValueError(f"Post manquant dans state: {state}")

    res = llm.invoke(f"Prompt image OG:\n{post}")
    return {"image_prompt": res.content}

builder = StateGraph(State)
builder.add_node("summarize", summarize)
builder.add_node("hooks", hooks)
builder.add_node("post", post)
builder.add_node("og", og)

builder.set_entry_point("summarize")
builder.add_edge("summarize", "hooks")
builder.add_edge("hooks", "post")
builder.add_edge("post", "og")

graph = builder.compile()