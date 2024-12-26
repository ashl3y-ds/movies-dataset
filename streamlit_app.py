import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Movies dataset", page_icon="🎬")
st.title("🎬 Movies dataset")



# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    # Replace with your GitHub raw URL
    url = 'https://raw.githubusercontent.com/your-username/your-repository-name/main/data/cleaned_drought_data_part1.csv'
    
    # Load the dataset directly from GitHub using pandas
    df = pd.read_csv(url)
    
    return df

df = load_data()


