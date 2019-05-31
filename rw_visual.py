import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    num_points,distance = 2000,10
    rw = RandomWalk(distance,num_points)
    rw.fill_walk()
    point_numbers = list(range(num_points))
    # set the figure size
    plt.figure(dpi=128,figsize=(10,6))
    '''
    plt.scatter(rw.x_values,rw.y_values,marker='s',c=point_numbers,\
                cmap=plt.cm.Reds,edgecolors='none',s=20)
    '''
    plt.plot(rw.x_values,rw.y_values,linewidth=1,c='red')
    # emphasis the start and end point
    plt.scatter(0,0,marker='s',c='green',edgecolors='none',s=20)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],marker='s',\
                c='blue',edgecolors='none',s=20)
    # hide the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False) 
    plt.show()

    while True:
        keep_running = input('Make another random walk? (Y/N):')
        if keep_running in ('Y','N'):
            break
        else:
            print('Please enter Y or N!')
        
    if keep_running == 'N':
        break 
    