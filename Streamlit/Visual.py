import streamlit as st
import pandas as pd
import pygwalker as pyg

# Set page configuration
st.set_page_config(
    page_title="VidyaAI",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    f"<style>.st-emotion-cache-1wrcr25   {{background-image: url('https://image.lexica.art/full_jpg/6d78ef65-eafe-4757-ab0b-a8f6fd0e3e57');background-size: cover; }}</style>", unsafe_allow_html=True)
# Create a sidebar with a file upload widget
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Load Data


@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        return None


df = load_data(uploaded_file)

# Set title and subtitle
st.header('Vidya Vizualizer')

# Display PyGWalker


def load_config(file_path):
    with open(file_path, 'r') as config_file:
        config_str = config_file.read()
    return config_str


config = load_config('config.json')

if df is not None:
    pyg.walk(df, env='Streamlit', dark='dark', spec=config)
else:
    st.warning("Upload a CSV file to visualize the data.")
