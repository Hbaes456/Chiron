# Calculations and comparisons
# Calculate speed for 4 metres over 2 seconds. Decide whether it is at or below a 2 m/s limit, then repeat for 5 metres. Print the speed and comparison for each case.
# Write your attempt below. See the course page for expected results.
distance_m = 0.0
elapsed_s = 2.0
speed_m_per_s = distance_m / elapsed_s
enabled = True
under_limit = speed_m_per_s <= 2.0
print("Speed:", speed_m_per_s)
print("Allowed:", enabled and under_limit)
