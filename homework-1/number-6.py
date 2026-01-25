import pandas as pd

# Read the data
prefix = 'data/'
df = pd.read_parquet(prefix + 'green_tripdata_2025-11.parquet')

# Read taxi zone lookup to get zone names
zones = pd.read_csv(prefix + 'taxi_zone_lookup.csv')

# Question 6: For passengers picked up in "East Harlem North" in November 2025,
# which was the drop off zone that had the largest tip?

# Find the LocationID for "East Harlem North"
east_harlem_north = zones[zones['Zone'] == 'East Harlem North']
print("East Harlem North zone info:")
print(east_harlem_north)

if len(east_harlem_north) == 0:
    print("\nError: East Harlem North zone not found!")
else:
    pickup_location_id = east_harlem_north.iloc[0]['LocationID']
    print(f"\nEast Harlem North LocationID: {pickup_location_id}")
    
    # Filter for November 2025
    df['lpep_pickup_date'] = pd.to_datetime(df['lpep_pickup_datetime']).dt.date
    nov_start = pd.to_datetime('2025-11-01').date()
    nov_end = pd.to_datetime('2025-12-01').date()
    
    november_trips = df[
        (df['lpep_pickup_date'] >= nov_start) & 
        (df['lpep_pickup_date'] < nov_end)
    ]
    
    print(f"\nTotal trips in November 2025: {len(november_trips)}")
    
    # Filter for pickups in East Harlem North
    east_harlem_pickups = november_trips[november_trips['PULocationID'] == pickup_location_id]
    
    print(f"Trips picked up from East Harlem North in November 2025: {len(east_harlem_pickups)}")
    
    # Find the trip with the largest tip
    if len(east_harlem_pickups) > 0:
        max_tip_trip = east_harlem_pickups.loc[east_harlem_pickups['tip_amount'].idxmax()]
        
        print(f"\nLargest tip amount: ${max_tip_trip['tip_amount']:.2f}")
        print(f"Drop off LocationID: {max_tip_trip['DOLocationID']}")
        
        # Get the drop off zone name
        dropoff_zone = zones[zones['LocationID'] == max_tip_trip['DOLocationID']]
        
        if len(dropoff_zone) > 0:
            print(f"\nAnswer: The drop off zone with the largest tip is:")
            print(f"Zone: {dropoff_zone.iloc[0]['Zone']}")
            print(f"Borough: {dropoff_zone.iloc[0]['Borough']}")
            print(f"Tip Amount: ${max_tip_trip['tip_amount']:.2f}")
        else:
            print(f"\nWarning: Drop off zone with LocationID {max_tip_trip['DOLocationID']} not found in lookup table")
    else:
        print("\nNo trips found from East Harlem North in November 2025")


# East Harlem North zone info:
#     LocationID    Borough               Zone service_zone
# 73          74  Manhattan  East Harlem North    Boro Zone

# East Harlem North LocationID: 74

# Total trips in November 2025: 46891
# Trips picked up from East Harlem North in November 2025: 12041

# Largest tip amount: $81.89
# Drop off LocationID: 263

# Answer: The drop off zone with the largest tip is:
# Zone: Yorkville West
# Borough: Manhattan
# Tip Amount: $81.89
