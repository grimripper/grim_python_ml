__author__ = 'vaibhavt'
from scipy.optimize import fsolve
import scipy as sp

arr1 = sp.array([0.08844, -97.31, 2.853e+04])
print(arr1)
fp = sp.poly1d(arr1)
print(fp)

print(fp - 100000)

reached_max = fsolve(fp - 100000, 800)/(7*24)
print(reached_max[0])
