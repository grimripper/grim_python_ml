import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("C:\MyCode\BuildingMachineLearningSystemsWithPython\ch01\data\web_traffic.tsv",
                     delimiter="\t")

print(data)
x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x,y)
plt.xticks([w*7*24 for w in range(10)], ['week %i'%w for w in range(10)])
plt.autoscale(tight=False)
plt.grid()
#plt.show()

fpl, residuals, rank, sv, rcond = sp.polyfit(x,y,4,full=True)
f1 = sp.poly1d(fpl)
print(f1)
print(fpl)

print(residuals)

fx = sp.linspace(0,x[-1],1000)
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")
plt.show()
