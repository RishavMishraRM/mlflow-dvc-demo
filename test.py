import pandas as pd

data = [
    {"name":"Rishav", "age":24, "city":"patna"},
    {"name":"subham", "age":25, "city":"delhi"},
    {"name":"sunny", "age":27, "city":"bhopal"}
]

df = pd.DataFrame(data)

df.to_csv("data/data.csv", index=False)