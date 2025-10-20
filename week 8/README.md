# CORD-19 Data Explorer Report

## Overview
The **CORD-19 Data Explorer** is a Streamlit-based application designed to explore and visualize metadata from the CORD-19 dataset. This dataset contains COVID-19-related research publications, and the application provides an interactive interface for filtering, analyzing, and visualizing the data. The tool is particularly useful for researchers and analysts who want to gain insights into publication trends, top journals, and the content of research titles.

---

## Features and Functionalities

### 1. **Data Loading**
The application begins by loading the dataset using the `load_data()` function. This function:
- Reads the `metadata.csv` file into a Pandas DataFrame.
- Converts the `publish_time` column to a datetime format, handling any errors gracefully.
- Extracts the publication year from the `publish_time` column and stores it in a new column called `year`.
- Drops rows where the `year` column contains missing values to ensure clean data for analysis.

The `@st.cache_data` decorator is used to cache the loaded data, improving performance by preventing redundant data loading during app interactions.

---

### 2. **Sidebar Filters**
The application provides an interactive **Year Range Slider** in the sidebar, allowing users to filter the dataset based on the publication year. The slider:
- Covers the range from 2018 to 2025.
- Defaults to the range 2020–2021.
- Filters the dataset to include only records where the `year` falls within the selected range.

The filtered dataset is then used for all subsequent visualizations and analyses.

---

### 3. **Visualizations**
The application includes three key visualizations to help users explore the dataset:

#### a. **Publications Over Time**
- A bar chart is generated to display the number of publications per year within the selected range.
- The `year` column is used to calculate the count of publications for each year, and the data is sorted in ascending order.

#### b. **Top 10 Journals**
- A bar chart is created to show the top 10 journals with the highest number of publications in the filtered dataset.
- The `journal` column is used to calculate the frequency of publications, and the top 10 journals are displayed.

#### c. **Word Cloud of Titles**
- A word cloud is generated from the titles of the publications in the filtered dataset.
- Titles are concatenated into a single string, and the `WordCloud` library is used to create a visual representation of the most frequently occurring words.
- The word cloud is displayed using Matplotlib, with the axes turned off for a cleaner appearance.

---

### 4. **Data Sample Display**
To provide users with a quick overview of the filtered dataset, the application displays the first few rows of the filtered DataFrame using `st.dataframe()`. This allows users to inspect the structure and content of the data.

---

## Code Implementation

### Key Libraries Used
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating the word cloud visualization.
- **Seaborn**: Imported but not used in the current implementation (can be utilized for additional visualizations in the future).
- **WordCloud**: For generating the word cloud from publication titles.

### Code Structure
The code is structured as follows:
1. **Imports**: All necessary libraries are imported at the beginning.
2. **Title and Description**: The app's title and a brief description are displayed using `st.title()` and `st.write()`.
3. **Data Loading**: The `load_data()` function handles data loading and preprocessing.
4. **Sidebar Filters**: The year range slider is implemented to filter the dataset.
5. **Visualizations**: Three visualizations (publications over time, top journals, and word cloud) are created and displayed.
6. **Data Sample**: A sample of the filtered dataset is displayed for user inspection.

---

## User Interaction
The application is highly interactive, allowing users to:
- Adjust the year range using the slider to dynamically filter the dataset.
- View updated visualizations and data samples based on the selected year range.

---

## Potential Improvements
While the application is functional and provides valuable insights, the following enhancements could be considered:
1. **Additional Filters**: Add filters for other columns, such as `authors`, `abstract`, or `keywords`.
2. **Advanced Visualizations**: Include more complex visualizations, such as heatmaps or network graphs, to analyze relationships between authors or topics.
3. **Export Functionality**: Allow users to download the filtered dataset or visualizations.
4. **Error Handling**: Improve error handling for cases where the dataset is missing or columns are not as expected.
5. **Seaborn Integration**: Utilize Seaborn for more aesthetically pleasing and customizable visualizations.

---

## Conclusion
The **CORD-19 Data Explorer** is a powerful tool for exploring COVID-19 research metadata. By leveraging Streamlit's interactivity and Python's data analysis libraries, the application provides an intuitive interface for filtering, analyzing, and visualizing the dataset. With further enhancements, it could become an even more robust tool for researchers and analysts.