import json
from transformers import pipeline 

with open("config.json" , "r") as f :
    configfile = json.load(f)

generator = pipeline("text-generation" , model=configfile["model_path"] , tokenizer = configfile["tokenizer"]) 

def generate_text_PRO( prompt : str) -> str :
    full_prompt = "You are a powerful assistant , please answer this : " + prompt
    result = generator(full_prompt , **configfile["generator"])

    return result[0]