import pandas as pd

# Read the data
prefix = 'data/'
df = pd.read_parquet(prefix + 'green_tripdata_2025-11.parquet')

# Question 4: Which was the pick up day with the longest trip distance?
# Only consider trips with trip_distance < 100 miles

# Filter trips with distance < 100 miles
filtered_trips = df[df['trip_distance'] < 100]

print(f"Total trips in dataset: {len(df)}")
print(f"Trips with distance < 100 miles: {len(filtered_trips)}")

# Find the trip with the longest distance
longest_trip = filtered_trips.loc[filtered_trips['trip_distance'].idxmax()]

print(f"\nLongest trip distance: {longest_trip['trip_distance']} miles")
print(f"Pickup datetime: {longest_trip['lpep_pickup_datetime']}")

# Extract the date (day) from the pickup datetime
pickup_date = pd.to_datetime(longest_trip['lpep_pickup_datetime']).date()

print(f"\nAnswer: The pick up day with the longest trip distance is: {pickup_date}")
print(f"Full pickup datetime: {longest_trip['lpep_pickup_datetime']}")

# Total trips in dataset: 46912
# Trips with distance < 100 miles: 46891

# Longest trip distance: 88.03 miles
# Pickup datetime: 2025-11-14 15:36:27

# Answer: The pick up day with the longest trip distance is: 2025-11-14
# Full pickup datetime: 2025-11-14 15:36:27