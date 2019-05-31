from die import Die
import pygal

die1 = Die()
die2 = Die(10)

results = []
roll_times = 1000
for roll_num in range(roll_times):
    results.append(die1.roll()+die2.roll())
# print(results)

# analysis the results
frequences = []
max_result = die1.num_sides + die2.num_sides
for value in range(1,max_result+1):
    frequences.append(results.count(value))
# print(frequences)

# visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 and one D10 dice %d times.' % roll_times
hist.x_labels = [str(i) for i in range(1,max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of the Result'

hist.add('D6 + D10',frequences)
hist.render_to_file('die_visual.svg')