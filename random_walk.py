from random import choice

class RandomWalk():
    ''' generate a random walk data class '''

    def __init__(self,distance,num_points=5000):
        ''' initiate the attributes '''
        self.num_points = num_points

        # start point [0,0]
        self.x_values = [0]
        self.y_values = [0]
        # maximum distance
        self.distance = list(range(distance+1))
    
    def fill_walk(self):
        ''' calculate all the points '''

        while len(self.x_values) < self.num_points:

            x_direction = choice([1,-1])
            x_distance = choice(self.distance)
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice(self.distance)
            y_step = y_direction * y_distance

            # can't move 0
            if x_step == 0 and y_step == 0:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)

