from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

st.markdown(f"<style>.st-emotion-cache-1wrcr25   {{background-image: url('https://image.lexica.art/full_jpg/6d78ef65-eafe-4757-ab0b-a8f6fd0e3e57');background-size: cover; }}</style>", unsafe_allow_html=True)
def main():
    load_dotenv()
    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
    st.header("Ask your CSV 📈")
    with st.sidebar:
        csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:

        agent = create_csv_agent(
            OpenAI(temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))
if __name__ == "__main__":
    main()
