import pandas as pd

# Read the data
prefix = 'data/'
df = pd.read_parquet(prefix + 'green_tripdata_2025-11.parquet')

# Display basic info
print("Dataset info:")
print(df.info())
print("\nFirst few rows:")
print(df.head())

# Question: For trips in November 2025, how many trips had trip_distance <= 1 mile?
# Filter for November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive)
november_trips = df[
    (df['lpep_pickup_datetime'] >= '2025-11-01') & 
    (df['lpep_pickup_datetime'] < '2025-12-01')
]

print(f"\nTotal trips in November 2025: {len(november_trips)}")

# Filter for trips with distance <= 1 mile
short_trips = november_trips[november_trips['trip_distance'] <= 1]

print(f"Trips with distance <= 1 mile: {len(short_trips)}")
print(f"\nAnswer: {len(short_trips)} trips")

# Total trips in November 2025: 46891
# Trips with distance <= 1 mile: 8007