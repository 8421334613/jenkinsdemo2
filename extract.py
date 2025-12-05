import pandas as pd


print("extract data")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'mumbai']
    
}

df = pd.DataFrame(data)
print(df)