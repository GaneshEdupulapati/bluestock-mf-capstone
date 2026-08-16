import requests
import pandas as pd

# Public API
url = "https://jsonplaceholder.typicode.com/users"

# Send GET request
response = requests.get(url)

# Check response status
print("Status Code:", response.status_code)

# Convert JSON response
data = response.json()

# Display JSON data
print("\nJSON Response:")
print(data)

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Display table
print("\nData:")
print(df)

# Save JSON data as CSV
df.to_csv("week2/api_assignment/api_data.csv", index=False)

print("\nCSV file created successfully!")