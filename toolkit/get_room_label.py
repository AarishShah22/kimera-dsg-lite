
import sys
sys.path.append("/utlis") 
from text_toolkit import Make_up_template
import openai

gpt_version = "gpt-3.5-turbo"  
openai_api_key = ""  #add openai api key here
openai.api_key = openai_api_key

Template = "There is a room, in the room, there is xxx \n"
Question = "What room it could be like?(bedroom, iving room, office place or somthing else)\
            answer with just one word"


def get_room_label(candidates_list):
    completion = openai.ChatCompletion.create(
    model=gpt_version, 
    messages=[{"role": "user", "content": template+Question}]
    max_tokens=2, 
    temperature=0)
    return completion["choices"][0]["message"]["content"].strip()  











