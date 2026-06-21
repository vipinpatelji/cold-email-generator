import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="Cold Email Generator", page_icon="✉️")
st.title("✉️ Cold Email Generator")

sender_name = st.text_input("Your Name")
company     = st.text_input("Target Company")
college     = st.text_input("your college")
offer       = st.text_input("What you offer")
tone        = st.selectbox("Tone", ["Professional", "Friendly", "Persuasive"])

if st.button("Generate Email", type="primary"):
    if not all([sender_name, company, college, offer]):
        st.error("Please fill all fields!")
    else:
        with st.spinner("Writing your email..."):
            try:
                model  = genai.GenerativeModel("gemini-2.5-flash")
                prompt = f"Write a {tone} cold email. Sender: {sender_name},  College: {college}, Offer: {offer}. Include subject line and a clear CTA. Keep it under 8 lines."
                result = model.generate_content(prompt).text
                st.success("Done!")
                st.text_area("Your Email", value=result, height=300)
            except Exception as e:
                st.error(f"Error: {e}")
