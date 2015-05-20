import matplotlib.pyplot as plt 
import numpy as np
counts={"abir":78,"zahid":87,"sumit":7,"Mamun":99,"Prosanto":12}
names =[]
votes = []

for key in counts:
	names.append(key)
	votes.append(counts[key])

x= np.arange(len(counts))

plt.bar(x,votes)
plt.xticks(x+0.5,names,rotations=90)