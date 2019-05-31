import matplotlib.pyplot as plt

values = [1,2,3,4,5]
squares = [x**2 for x in values]
plt.plot(values,squares,linewidth=3)

# set title and add label of the axis
plt.title("square Numbers",fontsize=24,loc='center')
plt.xlabel('Value',fontsize=14)
plt.ylabel('Sqaure of value',fontsize=14)

# set the size of the ticks
plt.tick_params(axis='both',labelsize=14)
plt.show()