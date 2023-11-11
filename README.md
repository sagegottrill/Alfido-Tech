# Alfido-Tech Internship
 This repository is a source code for the tasks that were assigned to me for my internship at Alfido Tech. The tasks include the following projects:
 - Weather Data Analysis
 - Uber Data Analysis
 - Inventory Analysis Case
   
# Weather-Data-Analysis-Alfido-Tech

Overview:-
  The Weather Data Analysis project leverages various data preprocessing techniques, data exploration, and the implementation of a Random Forest Classifier to predict weather descriptions based on provided weather data. The goal of this project is to build a reliable model for weather description classification, enabling applications in weather analysis.

Project Structure:-
Weather Data Analysis that analyzes weather data using Python libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn. The project description includes the following steps:
1. Importing and preprocessing the weather data, including renaming columns, converting data types, and checking for null values and duplicates.
2. Exploratory data analysis, including generating summary statistics, creating visualizations such as line plots, histograms, and heatmaps, and calculating correlations between numerical columns.
3. Standardizing weather descriptions by replacing various descriptions with more consistent labels such as 'Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Haze', and 'Thunderstorms'.
4. Handling outliers by creating boxplots and removing outliers from specific columns using the interquartile range method.
5. Oversampling the data using SMOTE to balance the target variable.
6. Building a random forest classifier to predict the weather type based on other variables such as temperature, humidity, wind speed, and pressure.
7. Evaluating the model's accuracy using metrics such as confusion matrix and classification report.

Project Conclusion:-
  Based on the evaluation of the Random Forest model, the project concludes that the model is effective in classifying weather descriptions. It achieves a high accuracy score of approximately 91%. The confusion matrix and classification report provide additional insights into the model's performance for different weather classes. This project serves as a comprehensive example of data preprocessing, exploratory data analysis, and machine learning classification techniques in the context of weather data. 

# Uber-Data-Analysis-Alfido-Tech

  This project involves exploration of the Uber Dataset using R and various data manipulation and visualization packages. The initial focus is on data preprocessing, where the dataset is loaded from a CSV file, and measures are taken to handle missing and inconsistent data. This includes replacing empty strings with NA values, converting date and time columns to datetime objects, removing duplicates, and standardizing location names.

  After data preprocessing, the project proceeds to understand the dataset's structure and dimensions, offering a summary of the "MILES" column to provide an overview of trip distances. The heart of the project lies in data visualization, with a series of compelling visualizations. These visualizations include a boxplot and histogram of trip distances, a bar plot displaying the count of Uber trips by purpose, and bar plots showing the top 10 start and stop locations by frequency.

  Furthermore, the project features bar plots to visualize the average miles by category and purpose, allowing for an in-depth exploration of how trip distances vary based on different categories and purposes. This approach to data analysis and visualization provides valuable insights into the Uber Dataset, making it an essential resource for decision-making, optimization, and understanding user behavior within the Uber platform.

# Inventory-Analysis-Case-Study-Alfido-Tech

  The project involves the use of Python libraries for data analysis, including Pandas, NumPy, Matplotlib, Seaborn, and WordCloud, as well as handling warnings in the code. The primary datasets used in this project include Purchase Price, Beginning Inventory, Ending Inventory, Purchases, Purchase Final, and Sales Final. The project encompasses an initial exploration of these datasets and dives into exploratory data analysis, with a focus on understanding the relationships, distributions, and insights that can be extracted from the data.

  The project structure includes initial data exploration, exploring relationships, distribution, and insights. Visualizations include word clouds, top brands by price, vendor-quantity relationships, total amounts for top vendors, and more.

  This data analysis and visualization project provides valuable insights into various aspects of product purchases and inventory. It showcases the power of data analysis and visualization techniques in extracting meaningful information from complex datasets. The visualizations and analysis presented in this project can be used for decision-making, identifying trends, and understanding the performance of vendors, brands, and products.
