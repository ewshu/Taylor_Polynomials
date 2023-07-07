def approximate_value(self, x):
    """
        Approximates the value of f(x) using the taylor polynomial.
        x = point to approximate f(x)
    """
    fx = 0
    for i in range(len(self.coefficients)):
        fx += self.coefficients[i] * ((x - self.center)**i)  # coefficient * nth term
    return fx