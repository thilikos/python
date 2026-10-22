import math


n = 10


f_old = 0                 # n-1-st  Fibonacci number
f_cur = 1                 # n-th    Fibonacci number
f_new = 1


i = 0

while i <= n:
  f_old = f_cur
  f_cur = f_new
  f_new = f_old + f_cur
  print(f_new)








