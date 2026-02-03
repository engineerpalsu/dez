#!/bin/bash
for month in 01 02 03 04 05 06 07 08 09 10 11 12; do
  gunzip -k -f data/yellow_tripdata_2020-${month}.csv.gz
done && echo "All files extracted"