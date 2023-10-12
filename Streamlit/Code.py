import streamlit as st
import openai

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Define a Streamlit app
st.title("Code Analysis")

code = st.text_area("Enter the code you want to analyze:", "", height=400)
st.markdown(f"<style>.st-emotion-cache-1wrcr25  {{background-image: url('https://images.pexels.com/photos/2362009/pexels-photo-2362009.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');background-size: cover; }}</style>", unsafe_allow_html=True)
if st.button("Analyze"):
    if code:
        prompt = f"Find all Bugs and modules used explain each and tech used,Please analyze the following code:\n\n"'{code}'"\n\nAnalysis:"
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a coding assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
        frequency_penalty=0.3,
        presence_penalty=0.3)
        analysis=response["choices"][0]["message"]["content"].strip()
        st.subheader("Analysis Result:")
        st.write(analysis)
    else:
        st.warning("Please enter code for analysis.")

# Optionally, add a section for displaying examples, tips, or additional information.
