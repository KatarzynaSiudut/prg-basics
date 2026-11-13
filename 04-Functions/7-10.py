def f(x, y):
  count = 0
  for n in range(x, y + 1):
    if n < 0 and n % 2 == 0:
      count += 1
  return count

print(f"f(-7, 8) returns {f(-7, 8)}")
print(f"f(-1, 11) returns {f(-1, 11)}")







