import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from rag_core import ask
from dotenv import load_dotenv
 
load_dotenv()
 
app = Flask(__name__)
 
TWILIO_SID   = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WA_NUM = os.getenv("TWILIO_WHATSAPP_NUMBER")
 
GREETING_KEYWORDS = ["hi", "hello", "hey", "helo", "namaste", "नमस्ते", "हेलो", "start"]
 
def is_greeting(text: str) -> bool:
    return text.strip().lower() in GREETING_KEYWORDS
 
GREETING_MSG = """👋 *Sunshine Clinic Assistant*
 
Hello! I can help you with:
• 🕐 Clinic timings
• 👨‍⚕️ Doctor availability
• 💰 Consultation fees
• 📅 Appointment booking
• 🏥 Services & facilities
 
Just type your question in *Hindi or English*.
 
📞 Emergency: *9876500000*"""
 
@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").strip()
    from_number  = request.values.get("From", "")
 
    print(f"Message from {from_number}: {incoming_msg}")
 
    resp = MessagingResponse()
    msg  = resp.message()
 
    if not incoming_msg:
        msg.body("Please send a text message with your question.")
        return str(resp)
 
    if is_greeting(incoming_msg):
        msg.body(GREETING_MSG)
        return str(resp)
 
    answer = ask(incoming_msg)
 
    footer = "\n\n📞 *Sunshine Clinic* | 020-25001234"
    full_reply = answer + footer
 
    msg.body(full_reply)
    return str(resp)
 
 
@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "service": "Sunshine Clinic WhatsApp Bot"}, 200
 
 
if __name__ == "__main__":
    print("Starting WhatsApp bot server on port 5000...")
    print("Make sure ngrok is running: ngrok http 5000")
    app.run(debug=False, port=5000)
 