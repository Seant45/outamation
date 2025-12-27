#Introduction to pandas
import pandas as pd  # Import Pandas  

# Create a small dataset  
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}  
df = pd.DataFrame(data)  # Convert dictionary to DataFrame  

print(df)  # Display the dataset  
df.sort_values(by='Age')
print(df)
#====================
# Basic Pandas Operations 
# Import Pandas → import pandas as pd
# Read CSV → df = pd.read_csv("file.csv")
# Check Data → df.head(), df.info(), df.describe()
# Filter Data → df[df['Age'] > 30]
# Sort Data → df.sort_values(by='Age')
# Handle Missing Values → df.fillna(value), df.dropna()