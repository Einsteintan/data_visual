import matplotlib.pyplot as plt

values = list(range(1,10))
squares = [x**2 for x in values]

# plt.scatter(values,squares,c='red',edgecolors='black',s=30) # c=(0,0,0)~(1,1,1)
# use colormap, see http://matplotlib.org/ 
# --> Examples --> Color Examples --> colormap_reference
plt.scatter(values,squares,c=squares,cmap=plt.cm.Blues,edgecolors='none',s=40)

# set title and add labels of axes
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of value',fontsize=14)

# set the range of the xlabel and ylabel
plt.axis([0,10,0,100])
# set the size of the ticks
plt.tick_params(axis='both',which='major',labelsize=14)

plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()
