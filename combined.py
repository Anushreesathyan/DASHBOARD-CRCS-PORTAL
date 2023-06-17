import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mpld3
import numpy as np

df = pd.read_csv("Dummy dataset.csv")

# Count the number of societies in each state or district
society_count = df['State'].value_counts()

# Plot the countplot
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='State', order=society_count.index)
plt.xlabel('State or District')
plt.ylabel('Number of Societies')
plt.title('Number of Societies in each State or District')
plt.xticks(rotation=90)
html_path_1 = 'society_count_chart.html'
html_1 = mpld3.fig_to_html(plt.gcf())

# To visualize the relationship between the date of registration and the area of operation
df['Date of Registration'] = pd.to_datetime(df['Date of Registration'])
plt.figure(figsize=(12, 8))
plt.scatter(df['Date of Registration'], df['Area of Operation'])
plt.xlabel('Date of Registration')
plt.ylabel('Area of Operation')
plt.title('Relationship between Date of Registration and Area of Operation')
plt.xticks(rotation=45)
html_path_2 = 'registration_area_scatter.html'
html_2 = mpld3.fig_to_html(plt.gcf())

# To visualize the number of societies registered each year
df['Year'] = df['Date of Registration'].dt.year
year_counts = df['Year'].value_counts().sort_index()
plt.figure(figsize=(12, 8))
year_counts.plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Number of Societies')
plt.title('Number of Societies Registered per Year')
plt.xticks(rotation=45)
html_path_3 = 'societies_registered_yearly.html'
html_3 = mpld3.fig_to_html(plt.gcf())

# To visualize the number of societies registered in each state
state_counts = df['State'].value_counts()
plt.figure(figsize=(12, 8))
state_counts.plot(kind='bar')
plt.xlabel('State')
plt.ylabel('Number of Societies')
plt.title('Number of Societies Registered per State')
plt.xticks(rotation=45)
html_path_4 = 'societies_registered_state.html'
html_4 = mpld3.fig_to_html(plt.gcf())

# To visualize the number of societies based on their sector type
sector_counts = df['Sector Type'].value_counts()
plt.figure(figsize=(12, 8))
sector_counts.plot(kind='bar')
plt.xlabel('Sector Type')
plt.ylabel('Number of Societies')
plt.title('Number of Societies Registered by Sector Type')
plt.xticks(rotation=45)
html_path_5 = 'societies_registered_sector.html'
html_5 = mpld3.fig_to_html(plt.gcf())

# To create a heatmap showing the count of societies categorized by state and sector type
cross_tab = pd.crosstab(df['State'], df['Sector Type'])
plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab, cmap='Blues', annot=True, fmt='d', cbar=True)
plt.title('Count of Societies by State and Sector Type')
plt.xlabel('Sector Type')
plt.ylabel('State')
plt.xticks(rotation=45)
html_path_6 = 'heatmap.html'
html_6 = mpld3.fig_to_html(plt.gcf())

# Concatenate all the HTML code together
html_combined = f'''
<html>
<head>
  <title>Society Visualizations</title>
</head>
<body>
  <!-- Visualization 1: Number of Societies in each State or District -->
  <h2>Number of Societies in each State or District</h2>
  {html_1}

  <!-- Visualization 2: Relationship between Date of Registration and Area of Operation -->
  <h2>Relationship between Date of Registration and Area of Operation</h2>
  {html_2}

  <!-- Visualization 3: Number of Societies Registered per Year -->
  <h2>Number of Societies Registered per Year</h2>
  {html_3}

  <!-- Visualization 4: Number of Societies Registered per State -->
  <h2>Number of Societies Registered per State</h2>
  {html_4}

  <!-- Visualization 5: Number of Societies Registered by Sector Type -->
  <h2>Number of Societies Registered by Sector Type</h2>
  {html_5}

  <!-- Visualization 6: Count of Societies by State and Sector Type -->
  <h2>Count of Societies by State and Sector Type</h2>
  {html_6}
</body>
</html>
'''

# Save the combined HTML code to a file
with open('combined_visualizations.html', 'w') as file:
    file.write(html_combined)
