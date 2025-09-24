#from Llama_cpp import Llama
from llama_cpp import Llama
import json

with open("configpro.json" , "r") as f :
    config=json.load(f)
  

lama_load = Llama(  
    model_path = config["model_path"] , 
    n_ctx = config["n_ctx"] , 
    n_threads = config["n_threads"] ,
    n_gpu_layers = config["n_gpu_layers"] 
    )

def generate_text_promax(prompt : str ) -> str:
    full_prompt = f"[INST] {prompt.strip()} [/INST]"
    output = lama_load(prompt = full_prompt , **config["model_config"])
    return output["choices"][0]["text"].strip()