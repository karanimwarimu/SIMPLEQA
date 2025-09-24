from transformers import pipeline 

generator = pipeline( "text-generation" , r"E:\BIG\MODEL\models--gpt2\snapshots\607a30d783dfa663caf39e06633721c8d4cfcd7e"  , tokenizer= "gpt2")

def generate_text(prompt : str ) -> str :
  full_prompt = "You are a helpful assistant, answer this " + prompt 

  result = generator(full_prompt ,  max_new_tokens=56,  truncation=True,  temperature=0.7 , top_k=10, top_p=0.97, repetition_penalty=1.2 ,  pad_token_id=50256 )
  return result[0]
