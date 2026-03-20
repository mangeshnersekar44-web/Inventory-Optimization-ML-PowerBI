
import pandas as pd
from sqlalchemy import create_engine

# Read CSV directly
df = pd.read_csv("regional_sales_performance.csv")

# Create connection
engine = create_engine(
    "mysql+mysqlconnector://root:M084637N@localhost/sales_analysis"
)

# Upload dataframe to MySQL
df.to_sql(
    name="regional_sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data uploaded successfully!")

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+mysqlconnector://root:M084637N@localhost/sales_analysis"
)

df = pd.read_sql("SELECT * FROM regional_sales", engine)

print(df.head())
print(df.columns)
print(df.info())
print(df.shape)

