from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

app = FastAPI()

wiki_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
prompt = ChatPromptTemplate.from_messages([
    ("system", "Share Family details, Do not share any other details"),
    ("human", "{context}")
])
llm = ChatOllama(model="ministral-3:3b", temperature=0.1)

class FamilyRequest(BaseModel):
    name: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/warm")
def warm():
    wiki_tool.run("Albert Einstein")
    formatted = prompt.format_prompt(context="Warm up")
    llm.invoke(formatted.to_string())
    return {"status": "warmed"}

@app.post("/family")
def family(req: FamilyRequest):
    context = wiki_tool.run(req.name)
    formatted = prompt.format_prompt(context=context).to_string()
    resp = llm.invoke(formatted)
    return {"name": req.name, "family": resp.content}
