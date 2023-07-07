def print_equation(self):
    eqn_string = ""
    for i in range(self.order + 1):
        if self.coefficients[i] != 0:
            eqn_string += str(self.coefficients[i]) + ("(x-{})^{}".format(self.center, i) if i > 0 else "") + " + "
    eqn_string = eqn_string[:-3] if eqn_string.endswith(" + ") else eqn_string
    print(eqn_string)

def print_coefficients(self):
    print(self.coefficients)

def get_coefficients(self):
    """
        Returns the coefficients of the taylor series
    """
    return self.coefficients