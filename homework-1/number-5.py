import pandas as pd

# Read the data
prefix = 'data/'
df = pd.read_parquet(prefix + 'green_tripdata_2025-11.parquet')

# Read taxi zone lookup to get zone names
zones = pd.read_csv(prefix + 'taxi_zone_lookup.csv')

# Question 5: Which was the pickup zone with the largest total_amount (sum of all trips) 
# on November 18th, 2025?

# Filter for November 18th, 2025
df['lpep_pickup_date'] = pd.to_datetime(df['lpep_pickup_datetime']).dt.date
target_date = pd.to_datetime('2025-11-18').date()
nov_18_trips = df[df['lpep_pickup_date'] == target_date]

print(f"Total trips on November 18th, 2025: {len(nov_18_trips)}")

# Group by PULocationID and sum the total_amount
zone_totals = nov_18_trips.groupby('PULocationID')['total_amount'].sum().reset_index()
zone_totals.columns = ['LocationID', 'total_amount_sum']

# Sort by total_amount to find the largest
zone_totals = zone_totals.sort_values('total_amount_sum', ascending=False)

# Merge with zone names
zone_totals = zone_totals.merge(zones, left_on='LocationID', right_on='LocationID', how='left')

# Display top 10 zones
print("\nTop 10 pickup zones by total_amount on November 18th, 2025:")
print(zone_totals[['LocationID', 'Zone', 'Borough', 'total_amount_sum']].head(10))

# Get the zone with the largest total_amount
top_zone = zone_totals.iloc[0]
print(f"\nAnswer: The pickup zone with the largest total_amount is:")
print(f"Zone: {top_zone['Zone']}")
print(f"Borough: {top_zone['Borough']}")
print(f"LocationID: {top_zone['LocationID']}")
print(f"Total Amount: ${top_zone['total_amount_sum']:.2f}")

# Total trips on November 18th, 2025: 1773

# Top 10 pickup zones by total_amount on November 18th, 2025:
#    LocationID                         Zone    Borough  total_amount_sum
# 0          74            East Harlem North  Manhattan           9281.92
# 1          75            East Harlem South  Manhattan           6696.13
# 2          43                 Central Park  Manhattan           2378.79
# 3         244     Washington Heights South  Manhattan           2139.05
# 4         166          Morningside Heights  Manhattan           2100.59
# 5         130                      Jamaica     Queens           1998.11
# 6          97                  Fort Greene   Brooklyn           1780.41
# 7          65  Downtown Brooklyn/MetroTech   Brooklyn           1499.02
# 8          95                 Forest Hills     Queens           1423.75
# 9          82                     Elmhurst     Queens           1251.82

# Answer: The pickup zone with the largest total_amount is:
# Zone: East Harlem North
# Borough: Manhattan
# LocationID: 74
# Total Amount: $9281.92
