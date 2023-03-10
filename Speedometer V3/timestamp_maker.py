
#THIS IS FOR CREATING EXAMPLE TIMESTAMPS FOR TESTING 

import csv
#import pandas
import time
import random 

times_ran = 0
f = open('timestamps.csv','w')


#Number of times the for loop runs
num_of_interations = 10

for _ in range(0, num_of_interations):
	#How long between each timestamp

#If you want shorter numbers, you want cut them off useing :1
	current_time = round(time.time() * 100)
	f.write(str(current_time))
	f.write('\n')
	#changes Speed
	speed = 1
	time.sleep(speed)


	times_ran = times_ran + 1
	progress = num_of_interations - times_ran
	print('time left: ' + str(progress))

f.close()




# - Clayton Leuck, February 2023