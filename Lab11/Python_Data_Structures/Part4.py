# Tuples are immutable, we cannot change already-stored data in it.
points = (10, 20)
print(points[1])

for point in points:
    print(point, end=" ")

print()