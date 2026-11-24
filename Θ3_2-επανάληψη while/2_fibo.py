# Script Eg3_2
# Fibonacci numbers and the Golden Ratio

# Initializations
print('   n        f_n             r_n  ')
print('---------------------------------------')
tol = 10**-15
n = 2
f_old = 1                 # n-1-st  Fibonacci number
f_cur = 1                 # n-th    Fibonacci number
f_new = 2                 # n+1-st  Fibonacci number
r_cur = f_cur/f_old       # n-th    Golden Ratio estimate
r_new = f_new/f_cur       # n+1-st  Golden Ratio estimate
print(f'  {n:2d}   {f_cur:8d}    {r_cur:20.15f} ')

while abs(r_new - r_cur) > tol:
    # Increase n and update...
    n = n + 1
    f_old = f_cur
    f_cur = f_new
    f_new = f_old + f_cur
    r_cur = r_new
    r_new = f_new/f_cur
    print(f'  {n:2d}   {f_cur:8d}    {r_cur:20.15f} ')
