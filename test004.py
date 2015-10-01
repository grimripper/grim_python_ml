#features
# - sepal width, length
# - petal width, length

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
#print(data)

features = data['data']
feature_names = data['feature_names']
target = data['data']

for t,marker,c in zip(xrange(3), ">ox", "rgb"):
    plt.scatter(features[target == t,0],
                features[target == t,1],
                marker=marker,
                c=c)
