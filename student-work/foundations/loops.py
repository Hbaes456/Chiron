# Repeating work with loops
# Use a loop to add the numbers 1 through 5. Print each running total and the final total. Then write a while loop that prints a countdown 3, 2, 1 and finishes.
# Write your attempt below. See the course page for expected results.
total = 0
for sample in range(1,5):
    total = total + sample
    print("Sample:", sample, "Total:", total)
print("Finished:", total)
