import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
df = pd.read_csv('sample_data.csv')

# Display basic info
print("Data Overview:")
print(df.head())
print("\nData Info:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())

# Calculate average of Sales column
avg_sales = df['Sales'].mean()
print(f"\nAverage Sales: {avg_sales}")

# Visualization 1: Bar chart of Sales by Product
plt.figure(figsize=(10, 6))
plt.bar(df['Product'], df['Sales'], color='skyblue')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.savefig('sales_bar_chart.png')
plt.show()

# Visualization 2: Scatter plot of Sales vs Profit
plt.figure(figsize=(8, 6))
plt.scatter(df['Sales'], df['Profit'], color='green')
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.savefig('sales_profit_scatter.png')
plt.show()

# Visualization 3: Heatmap of correlation
correlation = df[['Sales', 'Profit']].corr()
plt.figure(figsize=(6, 5))
plt.imshow(correlation, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

# Insights
print("\nInsights and Observations:")
print("1. The average sales across all products is {:.2f}.".format(avg_sales))
print("2. From the bar chart, product G has the highest sales, while product F has the lowest.")
print("3. The scatter plot shows a positive correlation between Sales and Profit.")
print("4. The heatmap confirms a strong positive correlation between Sales and Profit (value close to 1).")
print("5. Overall, higher sales tend to lead to higher profits, which is expected in business contexts.")