import pandas as pd

data = [
    {"name":"Rishav", "age":24, "city":"patna"},
    {"name":"subham", "age":25, "city":"delhi"},
    {"name":"sunny", "age":27, "city":"bhopal"}
]

df = pd.DataFrame(data)

data_1 = [
    {"name":"Ris", "age":25, "city":"new_delhi"},
    {"name":"Subh", "age":27, "city":"patna"}
]


df = pd.DataFrame(data + data_1)
df.to_csv("data/data.csv", index=False)