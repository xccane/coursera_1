H = int(input())   # высота шеста
A = int(input())   # метров вверх за день
B = int(input())   # метров вниз за ночь
# H > A > B. На какой день до вершины шеста?
print(1 + (H - A) // (A - B) + ((H - A) % (A - B) + A - B - 1) // (A - B))
