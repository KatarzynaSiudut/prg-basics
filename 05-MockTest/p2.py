def f(n1, n2, n3):
  return len({n1, n2, n3}) == 3

print(f(3,3,4))
print(f(3,4,5))



def f(n1,n2,n3):
  if n1 != n2 and n1!= n3 and n2 != n3:
    return True
  else:
    return False

print(f(2,2,3))
print(f(4,3,2))
