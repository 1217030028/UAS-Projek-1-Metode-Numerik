from simpson import*

def f(x):
    return 3*x**2 + 2*x + 1  # Example three-term expression

a = float(input('batas bawah = '))
b = float(input('batas atas = '))
n = int(input('jumlah grid = '))

integral = simpson(f, a, b, n)

print('Integral = ', integral)
