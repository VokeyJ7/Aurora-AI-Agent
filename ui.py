import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import customtkinter as ctk 
import time
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType, Tool
import time
import os
from langchain_community.utilities import SerpAPIWrapper, GoogleSearchAPIWrapper
from ai import chain
from serpapi import GoogleSearch
from dotenv import SERPAPI_API_KEY
searcher = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)


window = ctk.CTk()

window.title('Aurora')
window.geometry("700x700")
window.configure(bg='#FA8072')
ctk.set_appearance_mode('Dark')


window.resizable(True, True)
frame = ctk.CTkFrame(window, width=700, height=700) 
frame.pack(expand=True) 
frame.pack_propagate(True)


label = ctk.CTkLabel(frame, text='Hello there!') 
label.pack(padx=10, pady=10, expand=True, fill='both', side='top')

def panic():
    start_str = tk.StringVar()
    start_str.set('Okay take deep breaths with me')
    final.insert("1.0", start_str.get())
    
    breathe_str = tk.StringVar()
    breathe_str.set('Breathe in...')
    breathe2_str = tk.StringVar()
    breathe2_str.set('Breathe out...')
    final.delete("1.0", 'end')
    final.insert("1.0", breathe_str.get())
    frame.after(3000, lambda: final.delete("1.0", 'end')) 

    frame.after(6000, lambda: final.insert('1.0', breathe2_str.get()))
    frame.after(9000, lambda: final.delete("1.0", 'end'))               
    
    frame.after(12000, lambda: final.insert('1.0', breathe_str.get()))
    frame.after(15000, lambda: final.delete("1.0", 'end'))

    frame.after(18000, lambda: final.insert('1.0', breathe2_str.get())) 
    frame.after(21000, lambda: final.delete("1.0", 'end'))

    frame.after(24000, lambda: final.insert('1.0', breathe_str.get())) 
    frame.after(27000, lambda: final.delete("1.0", 'end'))
    
    frame.after(30000, lambda: final.insert('1.0', breathe2_str.get())) 
    frame.after(33000, lambda: final.delete("1.0", 'end'))

    frame.after(36000, lambda: final.insert('1.0', breathe_str.get())) 
    frame.after(39000, lambda: final.delete("1.0", 'end'))

    frame.after(42000, lambda: final.insert('1.0', breathe2_str.get())) 
    frame.after(45000, lambda: final.delete("1.0", 'end'))

    frame.after(48000, lambda: final.delete("1.0", 'end'))
    end = tk.StringVar()
    end.set('Ground yourself in this moment.\n Despite the feelings you feel, \n You are in a safe place')
    frame.after(51000, lambda: final.insert("1.0", end.get()))


final = ctk.CTkTextbox(frame, corner_radius=.5, width=500, height=100, activate_scrollbars=True)
final.pack(padx=10, pady=10, expand=True, fill='both', side='bottom')



query = ctk.CTkEntry(frame, placeholder_text="Search Google ")
query.pack(padx=10, pady=10, expand=True, fill='both')

pnc_btn = ctk.CTkButton(frame, text='Panic Button', command=panic)
pnc_btn.pack(padx=10, pady=10, expand=True, fill='both')


def search(event=None):
    final.delete('1.0', 'end') 
    
    user_input = query.get()
    params = {
    'engine':'google',
    'q':user_input,
    "api_key":SERPAPI_API_KEY,
    'link':'google.com'
    
}
    search = GoogleSearch(params_dict=params)
    results = search.get_dict()
    organic_results = results['organic_results']

    if len(organic_results) == 1:
        snip = organic_results[0]

    elif len(organic_results) > 1:
        snip = organic_results[0]
    snip_down = snip['snippet']
    
    s_results = tk.StringVar()
    s_results.set(snip_down) 
    s_results_str = s_results.get() 
    if final.get('1.0').strip() == '':
        final.insert('1.0','Generating output...')
        frame.after(5000, lambda: (final.delete('1.0', 'end'), 
                                   final.insert('1.0',s_results_str)))

query.bind('<Return>', search)

search_btn = ctk.CTkButton(frame, text='Enter', command=search)
search_btn.pack(padx=10, pady=10, expand=True, fill='both')

final.insert('1.0', "Tap the 'Talk to Aurora' button to send all text in this box to Aurora. \n Aurora's messages dissappear after 1 minute so read fast! ")
final.bind("<FocusIn>", lambda event: final.delete('1.0','end')) 
final.bind("<FocusOut>", lambda event: final.insert('1.0', "Tap the 'Talk to Aurora' button to send all text in this box to Aurora. \n Aurora's messages dissappear after 1 minute so read fast! ")) 


def talk():
    usr = final.get('1.0', 'end')
    final.delete('1.0', 'end')
    str = ctk.StringVar()
    res = chain.invoke({"User_input":usr}, verbose=False)
    
    str.set(res["text"].strip()) 
    if final.get('1.0').strip() == '':
        final.insert('1.0','Generating output...')
        frame.after(4000, lambda: (final.delete('1.0', 'end'), 
                                   final.insert('1.0', str.get())))
        frame.after(80000, lambda: final.delete('1.0', 'end'))
        
            

talk_btn = ctk.CTkButton(frame, text='Talk to Aurora', command=talk)
talk_btn.pack(padx=10, pady=10, expand=True, fill='both')



window.mainloop()
