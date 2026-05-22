import time
import pandas as pd
from sqlalchemy import create_engine

DB_URL = "mysql+mysqlconnector://user:password@localhost:3306/my_database"

max_retries = 10
retry_delay = 10

engine = None

for attempt in range(max_retries):
    try:
        print(f"Attempt {attempt + 1} to connect...")

        engine = create_engine(DB_URL)

        with engine.connect() as connection:
            print("Connected to MySQL!")

        break

    except Exception as e:
        print("Database is not ready yet...")
        print(e)

        time.sleep(retry_delay)

if engine is None:
    raise Exception("Could not connect to database")

query = "SELECT * FROM titanic"

df = pd.read_sql(query, engine)

print(df)

print("\nShape of DataFrame:")
print(df.shape)