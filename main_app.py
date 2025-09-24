from flask import Flask , request , jsonify 
from text_gen import generate_text
from text_gen_PRO import generate_text_PRO
from text_gen_PROMAX import generate_text_promax
import time 

app= Flask(__name__)

@app.route('/generate' ,  methods =['POST'])

def  GENERATE_PROMPT():
 data = request.get_json()
 prompt = data.get("prompt" , " ")
 #result = generate_text(prompt)
 start_time = time.time()
 result = generate_text_promax(prompt)
 print (result)
 return jsonify({"reply": result })
 end_time= time.time()

 print(f"TOTAL TIME :  {start_time-end_time:.2f} seconds")


if __name__ == '__main__':
 app.run(host = '127.0.0.1' , port = 5000 ,  debug =True )
