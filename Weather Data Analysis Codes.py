--- Import python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
%matplotlib inline


--- load data
import pandas as pd
weather_data = pd.read_csv("C:/Users/USER/Desktop/Alfido Tech Internship/Weather Data.csv")
weather_data.head()


--- Correct column names
weather_data.rename(columns={'Rel Hum_%': 'Rel Humidity %'}, inplace=True)
weather_data.head()

--- Check for missing values
missing_values = weather_data.isnull().sum()
weather_data.head()

--- Convert the 'Date/Time' column to a datetime data type
weather_data['Date/Time'] = pd.to_datetime(weather_data['Date/Time'])
weather_data.head()

--- Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

--- Create a histogram for Temperature
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Temp_C', bins=20, kde=True)
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['Rel Hum_%'], bins=20, color='green', kde=True)
plt.xlabel('Humidity')
plt.ylabel('Frequency')
plt.title('Humidity Distribution')
plt.tight_layout()
plt.show()


plt.subplot(1, 2, 2)
sns.histplot(data=df, x='Wind Speed_km/h', bins=20, kde=True)
plt.title('Wind Speed Distribution')
plt.xlabel('Wind Speed (km/h)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.boxplot(x= 'Wind Speed_km/h', data=df, color='orange')
plt.xlabel('Wind Speed (km/h)')
plt.title('Box Plot of Wind Speed Distribution')
plt.show()

--- Create a box plot for 'Temp_C'
plt.figure(figsize=(8, 6))
sns.boxplot(x='Temp_C', data=df, color='blue')
plt.xlabel('Temperature (°C)')
plt.title('Box Plot of Temperature Distribution')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Temp_C', y='Rel Hum_%', data=df, color='green')
plt.xlabel('Temperature (°C)')
plt.ylabel('Relative Humidity (%)')
plt.title('Scatter Plot of Temperature vs. Relative Humidity')
plt.show()


correlation_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()


print(summary_stats)
numeric_df = df.select_dtypes(include=['number'])


--- Time Series Analysis
import matplotlib.pyplot as plt

monthly_average = df['Temp_C'].resample('M').mean()

plt.figure(figsize=(12, 6))
plt.plot(monthly_average.index, monthly_average, label='Monthly Average Temperature (°C)', color='blue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Average Temperature Over Time')
plt.legend()
plt.show()
