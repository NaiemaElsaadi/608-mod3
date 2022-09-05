# File 5 - population-dispersion.py (Section 4.18)  Naiema Elsaadi
# by useing the statistics module to calculate measures of dispersion for a population. 
# Using the data provided in 4.18 for 10 six-sided die rolls, and by calling functions in the statistics module - calculate:
# Population variance using pvariance()
# Population standard deviation using pstdev()

import statistics
statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
print('This is Population variance of 10 six-sided die rolls', statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]) )
print('This is Population standard of 10 six-sided die rolls', statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]) )
print ('My name is Naiema Elsaadi')