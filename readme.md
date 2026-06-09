Sunshine Clinic AI Chatbot
RAG-based AI assistant for clinic patients.
Works on Website (Streamlit) and WhatsApp (Twilio).
Uses Groq (free LLM) + HuggingFace embeddings (free) + ChromaDB (local).

STEP 1 — Get free API keys

Groq:        https://console.groq.com  → Create API key
HuggingFace: https://huggingface.co    → Settings → Tokens
Twilio:      https://twilio.com        → Free trial (WhatsApp sandbox)

STEP 2 — Setup
bashgit clone <your-repo>
cd clinic-chatbot
pip install -r requirements.txt
cp .env.example .env
# Fill in your keys in .env
STEP 3 — Add your clinic PDF
Put your clinic FAQ PDF at: data/clinic_faq.pdf
STEP 4 — Build vector database (run ONCE)
bashpython ingest.py
This creates a chroma_db/ folder. Run again only if you update the PDF.
STEP 5A — Run website bot locally
bashstreamlit run website_bot.py
Opens at http://localhost:8501
STEP 5B — Run WhatsApp bot locally
Terminal 1:
bashpython whatsapp_bot.py
Terminal 2 (install ngrok from https://ngrok.com/download):
bashngrok http 5000
Copy the https URL from ngrok (e.g. https://abc123.ngrok.io)
Go to Twilio Console → WhatsApp Sandbox → set webhook to:
https://abc123.ngrok.io/whatsapp
Then WhatsApp the Twilio sandbox number to test.
STEP 6 — Deploy website bot free on Streamlit Cloud

Push this folder to GitHub (public repo)
Go to https://share.streamlit.io
Connect repo, set main file as website_bot.py
Under Secrets, add:
GROQ_API_KEY = "gsk_..."
HF_TOKEN = "hf_..."
Deploy. Live URL in 3 minutes.

STEP 7 — Deploy WhatsApp bot free on Render

Push to GitHub
Go to https://render.com → New Web Service
Connect repo
Set Start Command: gunicorn whatsapp_bot:app
Add all env variables from .env
Deploy. Use the Render URL as your Twilio webhook.


Test questions

What are the clinic timings?
Which doctors are available on Monday?
How much is a cardiologist consultation?
How do I book an appointment?
Is the clinic open on Sunday?
क्लिनिक का समय क्या है?
डॉक्टर की फीस कितनी है?