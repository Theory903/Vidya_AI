import streamlit as st
from Model.AI.Bot import AI,say
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from st_pages import Page, show_pages
load_dotenv()
st.markdown(f"<style>.st-emotion-cache-ffhzg2 {{background-image: url('https://images.pexels.com/photos/2362009/pexels-photo-2362009.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')}}</style>", unsafe_allow_html=True)
show_pages(
    [
        Page("Streamlit/🏠homepage.py", "HOME PAGE","🏠"),
        Page("Streamlit/Main.py", "PlayGround", "🤖"),
        Page("Streamlit/app.py", "Ask PDF","📑"),
        Page("Streamlit/CSV.py", "Ask CSV","📉"),
        Page("Streamlit/Visual.py", "Visualize","📈"),
        Page("Streamlit/yt.py", "Chat with YOUTUBE","▶️"),
        Page("Streamlit/Code.py", "Code Analysis","👨‍💻"),
        Page("Streamlit/interview.py", "Interview","💬")
        
    ]
)
# Define initial messages if not already in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
def main(prompt):
    if prompt==" ":
        say("Write Something Valid...")
    else:
        return AI(prompt)
        # Get user input from the chat input

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():
            st.chat_message("user").write(prompt)
            # Replace this comment with the actual user input for AI processing
            user_input = prompt
            # Call the AI function with user input and get the bot's response
            bot_response = main(user_input)
            # Add the bot's response to the chat history
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            st.chat_message("assistant").write(bot_response)
            say(bot_response)
