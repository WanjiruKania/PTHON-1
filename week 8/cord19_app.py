# creating a simple Streamlit app to explore the CORD-19 dataset


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata from the CORD-19 dataset.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df.dropna(subset=['year'])

df = load_data()

# Sidebar filters
year_range = st.slider("Select Year Range", 2018, 2025, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"Showing {len(filtered_df)} records between {year_range[0]} and {year_range[1]}")

# Visualization 1: Publications over time
year_counts = filtered_df['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Visualization 2: Top Journals
top_journals = filtered_df['journal'].value_counts().head(10)
st.write("### Top 10 Journals")
st.bar_chart(top_journals)

# Visualization 3: Word Cloud of Titles
titles = " ".join(filtered_df['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

# Show a sample of data
st.write("### Sample of the Data")
st.dataframe(filtered_df.head())
