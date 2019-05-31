import matplotlib.pyplot as plt

x = list(range(1,5001))
y = [i**2 for i in x]

# plt.scatter(x,y,c='red',edgecolors='black',s=40)
plt.scatter(x,y,c=y,cmap=plt.cm.Reds,edgecolors='none',s=40)
plt.title('Example',fontsize=24)
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()