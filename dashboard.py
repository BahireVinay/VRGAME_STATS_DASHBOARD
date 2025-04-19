import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('game_data.csv')

# Create the app
st.title('VR Game Analytics Dashboard')

# Display basic stats
st.write("## Basic Statistics")
st.write(df.describe())

# Time Spent per Player
st.write("## Time Spent per Player")
sns.barplot(x='Player_ID', y='Time_Spent', data=df)
st.pyplot()

# Most Visited Locations
st.write("## Most Visited Locations")
location_counts = df['Location_Visited'].value_counts()
sns.barplot(x=location_counts.index, y=location_counts.values)
st.pyplot()

# Filter options for interactive data exploration
location = st.selectbox('Select Location:', df['Location_Visited'].unique())
filtered_data = df[df['Location_Visited'] == location]

st.write(f"Filtered Data for {location}")
st.write(filtered_data)

