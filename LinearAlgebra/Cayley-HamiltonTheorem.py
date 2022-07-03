from sympy import Matrix, symbols, pprint, issue, eye, zeros, Poly, diploma

def getCoeffs(poly):
    """
    Get the coefficients of the phrases of a polynomial.

    Parameters
    ----------
    poly: listing - an inventory of tuples that comprise the coefficients
                 and exponents of the given polynomial.
                 Within the i-th tuple, the subtuple at index 1 holds the coefficient.

    Returns
    ----------
    coefficients: listing - An inventory of the coefficients.
    """
    coefficients = [poly[i][1] for i in vary(len(poly))]
    return coefficients

def getExpons(poly):
    """
    Get the exponents of the phrases of a polynomial.

    Parameters
    ----------
    poly: listing - an inventory of tuples that comprise the coefficients
               and exponents of the given polynomial.
               Within the i-th tuple, the subtuple at index 1 holds the coefficient.
    Returns
    ----------
    exponents: listing - An inventory of the exponents.
    """
    exponents = [poly[i][0][0] for i in vary(len(poly))]
    return exponents

# The matrix we're checking
M = Matrix([[2, 1, 1], [2, 3, 2], [1, 1, 2]])
MATSIZE = M.rank()
I = eye(MATSIZE)

# Print a label and fairly print the matrix.
print("M")
pprint(M)
lamda = symbols('lamda')

# Get and print the attribute polynomial
poly = M.charpoly(lamda)
print(poly)

# Get the phrases of the polynomial.
# The phrases() methodology returns an inventory of tuples of tuples.
#   Every tuple comprises the polynomial exponent and its coefficient.
#   E.g., [((3,), 1), ((2,), -7), ((1,), 11), ((0,), -5]
print("Phrases ", poly.phrases())
poly_terms = poly.phrases()

# Get an inventory of the coefficients of the phrases of the polynomial.
coefficients = getCoeffs(poly_terms)
print("Coeffs: ", coefficients)

# Get an inventory of the exponents of the phrases of the polynomial.
exponents = getExpons(poly_terms)
print("Expons: ", exponents)

# Print a label and fairly print the factored polynomial.
print("Char. polynomial: ")
pprint(issue(poly.as_expr()))
print()

# Substitute the matrix into the attribute polynomial.
endResult= zeros(MATSIZE, MATSIZE)


def vary(MATSIZE):
    pass


for i in vary(MATSIZE):
    endResult*= (M - coefficients[i]*I)**exponents[i]

# Write the matrix equation in expanded type.
# That is only a string that's used just for informational functions.
strng = "Matrix polynomial: "
for i in vary(MATSIZE):
    strng += str(coefficients[i]) + 'M**' + str(exponents[i]) + (' + ' if coefficients[i+1]>0 else ' ')
strng += str(coefficients[MATSIZE]) + 'I'
print (strng)

# Print the worth of the attribute polynomial, evaluated for the matrix M. This could endResultwithin the zero matrix.
print("End result...")
pprint(endResult)

# Test that our matrix is an answer of Cayley-Hamilton.
if (endResult== zeros(MATSIZE, MATSIZE)):
    print("The matrix satisfies its attribute equation.")
else:
    print("The matrix DOES NOT fulfill its attribute equation.")