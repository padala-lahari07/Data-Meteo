#Temperature Trends Over Time
df['date'] = pd.to_datetime(df['last_updated_epoch'], unit='s')

# Now plot the temperature trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='date', y='temperature_celsius')
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.show()

#Precipitation Trends Over Time
df = df.reset_index()  # Move 'date' from index to a regular column
df['date'] = pd.to_datetime(df['last_updated_epoch'], unit='s')
df = df.sort_values('date')
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='date', y='precip_mm')
plt.title('Precipitation Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.show()

#Correlation Matrix
numeric_df = df.select_dtypes(include=['number'])
plt.figure(figsize=(12, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()