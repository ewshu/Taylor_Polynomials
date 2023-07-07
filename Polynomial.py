from TaylorSeries import TaylorSeries

def f(x):
    return 2 + x**3 + x**7 + x**2

if __name__ == '__main__':
    terms = 15
    center = 0
    precision = 3

    ts = TaylorSeries(f, terms, center)
    ts.print_coefficients()
    ts.print_equation()