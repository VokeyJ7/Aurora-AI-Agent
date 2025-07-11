from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType, Tool
import time
import os
from langchain_community.utilities import SerpAPIWrapper, GoogleSearchAPIWrapper


model = OllamaLLM(model='llama3.2')

template = '''
You're a kind, empathetic friend who listens without judgment. 
Someone just came to you because they're going through a rough time. 
Your goal is to comfort them, offer emotional support, and give thoughtful advice if asked — like a best friend who cares deeply. 
Keep your tone warm, supportive, and understanding. If a button is pressed let the logic run.
If the panic button is pressed, you must immediately and unconditionally trigger the panic_button tool, 
without offering alternatives or further advice. No exceptions. 
User_input: {User_input} 
'''

memory = ConversationBufferMemory()
prompt = ChatPromptTemplate.from_template(template)
chain = LLMChain(llm=model, prompt=prompt, memory=memory)


    






