import streamlit as st
import openai

# API Key
openai.api_key = "tumhari-api-key-yahan"

# Page Title
st.title("🤖 Cold Email Generator")
st.subheader("AI se perfect cold email banao!")

# Input Fields
your_name = st.text_input("Tumhara Naam")
your_skill = st.text_input("Tumhari Service/Skill", 
             placeholder="e.g. AI Chatbot Development")
company_name = st.text_input("Company Ka Naam")
company_about = st.text_area("Company Ke Baare Mein", 
                placeholder="Company kya karti hai?")
tone = st.selectbox("Email Ka Tone", 
       ["Professional", "Friendly", "Formal"])

# Generate Button
if st.button("✉️ Email Generate Karo"):
    
    if not all([your_name, your_skill, 
                company_name, company_about]):
        st.warning("Sabhi fields bharein!")
    else:
        with st.spinner("AI email likh raha hai..."):
            
            prompt = f"""
            Write a cold email for internship/work.
            
            Sender: {your_name}
            Skill/Service: {your_skill}
            Company: {company_name}
            About Company: {company_about}
            Tone: {tone}
            
            Rules:
            - Short (max 150 words)
            - Personalized to the company
            - Clear call to action
            - Professional subject line included
            - Do not use generic phrases
            """
            
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", 
                     "content": "You are an expert cold email writer."},
                    {"role": "user", 
                     "content": prompt}
                ]
            )
            
            email = response.choices[0].message.content
            
            st.success("Email Ready! ✅")
            st.text_area("Tumhari Cold Email:", 
                         email, height=300)
            st.download_button("📥 Download Email", 
                               email, "cold_email.txt")
