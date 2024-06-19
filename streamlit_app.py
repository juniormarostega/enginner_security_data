import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Security Data Analysis")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write(data)
    
    # Bar chart for attacks by year
    attacks_by_year = data['year'].value_counts().sort_index()
    st.subheader("Attacks by Year")
    plt.figure(figsize=(10, 6))
    plt.bar(attacks_by_year.index, attacks_by_year.values)
    plt.xlabel('Year')
    plt.ylabel('Number of Attacks')
    plt.title('Number of Attacks per Year')
    st.pyplot(plt)
    
    # Bar chart for attacks by type
    attacks_by_type = data['type'].value_counts()
    st.subheader("Attacks by Type")
    plt.figure(figsize=(10, 6))
    plt.bar(attacks_by_type.index, attacks_by_type.values)
    plt.xlabel('Type of Attack')
    plt.ylabel('Number of Attacks')
    plt.title('Number of Attacks by Type')
    st.pyplot(plt)

    # Filter data by country
    country = st.selectbox('Select a Country', data['country'].unique())
    filtered_data = data[data['country'] == country]
    st.write(filtered_data)

    # Cross data visualization
    st.subheader(f"Attacks in {country} by Year")
    country_attacks_by_year = filtered_data['year'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    plt.bar(country_attacks_by_year.index, country_attacks_by_year.values)
    plt.xlabel('Year')
    plt.ylabel('Number of Attacks')
    plt.title(f'Number of Attacks per Year in {country}')
    st.pyplot(plt)
else:
    st.info("Please upload a CSV file to proceed.")
