# Local QB (Mistral 7B) Flask App 🚀

This project runs a **local AI model (Mistral 7B)** with a **Flask web server**, and exposes an API endpoint for simple text generation.

---

## 🔧 Features
- Flask web server with `/ask` POST endpoint
- Local inference using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- Simple HTML frontend (`web.html`)
- CORS enabled for cross-origin requests

---

## 📂 Project Structure
project/
│── app.py                 # Flask server
│── text_gen_PROMAX.py     # Wrapper for llama-cpp model
│── requirements.txt
│── README.md
│── .gitignore
│
├── web/
│   ├── templates/
│   │   └── web.html       # Frontend page
│   └── static/
│       ├── webcss.css     # Example CSS file
│       └── script.js      # Example JS file
│
└── model (to be generated automatically)

---

## ⚡ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create & activate virtual environment
bash
Copy code
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

### 3. Install dependencies
bash
Copy code
pip install -r requirements.txt

### 4. Add your model
Download a Mistral 7B gguf model and place it inside a models/ folder (ignored by git).
or it will be generated automatically on starting the app

Example:
bash
Copy code
models/mistral-7b-instruct-v0.1.Q4_K_M.gguf

### 5. Run the Flask server
bash
Copy code
python app.py
The app runs at http://your IP Address:5000.

also ensure the webserver.html , the api points to the machine hosting the page , change to own ip address if using from othe rdevices :   
           try {
                const res = await fetch('http://127.0.0.1:5000/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt })
                });

###6 . Access the API:
 send a prompt affter starting the server using python second_app.py and accesing the web page 

###🌐 Optional: Public Access
To expose your server online :

Use : Cloudflare Tunnel or you can use NGRok(see more information ... added later)

Or host on a VPS with GPU
