
points = [(0, 0), (3, 4), (6, 8), (6, 14), (10, 17)]

total = 0
longest = 0
longest_from = 0

for i in range(len(points) - 1):
    x1, y1 = points[i]          # tuple unpacking
    x2, y2 = points[i + 1]
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    total = total + d
    print("Segment", i + 1, ":", points[i], "->", points[i + 1], "=", round(d, 2), "km")
    if d > longest:
        longest = d
        longest_from = i

print("\nTotal route distance:", round(total, 2), "km")
print("Longest segment: Segment", longest_from + 1, "from", points[longest_from],
      "to", points[longest_from + 1], "=", round(longest, 2), "km")
