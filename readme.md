🏥 AI Clinic Chatbot
An AI-powered chatbot that answers patient queries 24/7 — trained on your clinic's own data. No hallucinations. Works on website and WhatsApp. Supports Hindi and English.

🔴 Live Demo
👉 Try the bot here - https://clinic-chatbot-j2xd.onrender.com

Ask it anything: timings, doctors, fees, appointments — in Hindi or English.


✨ Features

RAG-based — only answers from verified clinic documents, zero hallucinations
Bilingual — Hindi and English supported
Website chatbot — embeddable on any website with one line of code
WhatsApp bot — patients can message directly on WhatsApp
Quick reply buttons — one-tap answers for common questions
Free stack — Groq LLM + HuggingFace embeddings + ChromaDB


🏢 Works for any business
BusinessUse case🏥 Clinics & hospitalsTimings, doctors, fees, appointments🍽️ RestaurantsMenu, timings, reservations, delivery🏠 Real estate agenciesProperty listings, pricing, availability📊 CA firmsITR deadlines, documents, fees🎓 Coaching classesCourses, fees, schedules, admissions

🛠️ Tech Stack
LayerToolCostLLMGroq (Llama 3.3)FreeEmbeddingsHuggingFace all-MiniLM-L6-v2FreeVector DBChromaDBFreeWebsite UIStreamlitFreeWhatsAppTwilio SandboxFree (testing)

🚀 Run locally in 5 steps
1. Clone the repo
bashgit clone https://github.com/maheksayyed19/clinic-chatbot.git
cd clinic-chatbot
2. Install dependencies
bashpip install -r requirements.txt
3. Add your API keys — create a .env file
GROQ_API_KEY=your_groq_key
HF_TOKEN=your_huggingface_token
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
Get free keys at: Groq • HuggingFace • Twilio
4. Add your data and build vector DB
Put your PDF at data/clinic_faq.pdf then run:
bashpython ingest.py
5. Run the website bot
bashstreamlit run website_bot.py
Opens at http://localhost:8501

📱 WhatsApp bot setup
bash# Terminal 1
python whatsapp_bot.py

# Terminal 2
ngrok http 5000
Paste the ngrok URL into Twilio Console → WhatsApp Sandbox → Webhook:
https://your-ngrok-url.ngrok.io/whatsapp

☁️ Free deployment
Website bot → Streamlit Cloud

Push repo to GitHub
Go to share.streamlit.io → connect repo
Add secrets: GROQ_API_KEY and HF_TOKEN
Deploy — live URL in 3 minutes

WhatsApp bot → Render

Go to render.com → New Web Service
Connect repo → Start command: gunicorn whatsapp_bot:app
Add all env variables → Deploy


💬 Test questions
What are the clinic timings?
Which doctors are available on Monday?
How much is a cardiologist consultation?
How do I book an appointment?
Is the clinic open on Sunday?
क्लिनिक का समय क्या है?
डॉक्टर की फीस कितनी है?

📞 Want this for your business?
I build custom AI chatbots for local businesses in India — trained on your data, deployed in one week.
Mahek Sayyed — AI Developer, Solapur
• LinkedIn - https://www.linkedin.com/in/mahek-sayyed-ba0717387/ 
• Email - maheksayyed803@gmail.com

⭐ Star this repo if you found it useful!
