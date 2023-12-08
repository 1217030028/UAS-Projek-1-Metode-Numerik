from simpson import*

def f(x):
    return 4*x**3 + 3*x**2 + 2*x + 1  # Example four-term expression

a = float(input('batas bawah = '))
b = float(input('batas atas = '))
n = int(input('jumlah grid = '))

integral = simpson(f, a, b, n)

print('Integral = ', integral)
