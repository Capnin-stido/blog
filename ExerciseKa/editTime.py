import os
# Taking time
waterTime = input('Enter the water time: ')
exerciseTime = input('Enter the exercise time: ')
eyeTime = input('Enter the eye exercise time: ')

#joining user entered data 
data = ' '.join([waterTime,exerciseTime,eyeTime]) 
#OUTPUT = 20 10 10
file = open(logFileName,'w')#opening file as write mode
file.write(data) #writting data in file
file.close() # Closing file
