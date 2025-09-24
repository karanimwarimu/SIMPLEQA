
from flask import Flask, request, jsonify, render_template
from text_gen_PROMAX import generate_text_promax
import time
import os 
from flask_cors import CORS 


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMP_DIR = r"F:\BIG (II)\WEB\template"
STATIC_DIR= r"F:\BIG (II)\WEB\static"

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMP_DIR)
CORS(app)
@app.route('/')
def index():
    return render_template('web.html')

@app.route('/ask', methods=['POST'])
def generate_prompt():
    data = request.get_json()
    prompt = data.get("prompt", "")
    start_time = time.time()
    result = generate_text_promax(prompt)
    end_time = time.time()

    print(f"\nPrompt: {prompt}")
    print(f"Response: {result}")
    total_time = end_time - start_time 
    print(f"TOTAL TIME: {total_time:.2f} seconds")

    return jsonify({
        "time_taken": f"{total_time:.2f} seconds" ,
        "response": result 
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
