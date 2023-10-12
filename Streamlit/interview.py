import os
import openai
import streamlit as st

#=============================================================================
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
#=============================================================================

st.title("Interview Prepration")
st.markdown(f"<style>.st-emotion-cache-ffhzg2 {{background-image: url('https://images.pexels.com/photos/6044198/pexels-photo-6044198.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')}}</style>", unsafe_allow_html=True)
text_input = st.text_input("How can i help you",placeholder = "talk with me", key = "input")

role = st.selectbox("ROLE",index = None, options = ("User","Developer"))


if role and text_input:
    
    
    


    if "history" not in st.session_state:
        st.session_state["history"] = []
        
    if "generated" not in st.session_state:
        st.session_state["generated"] = ["Hello how can i help you"]
        
    if "past" not in st.session_state:
        st.session_state["past"] = ["Hey ! :wave: "]
        
        
    #response_container = st.container()
    
    container = st.container()
    
    with container:
        st.title("Thanks for asking")
        st.title("yeh container ke andar ka hissa hai")
        #st.write(response["choices"][0]["message"]["content"])