#Obtain the values for small, medium and large treats. 
s = int(input())
m = int(input())
l = int(input())

#Calculate the happiness score.
happiness_score = s + m * 2 + l *3

#Initialize Barley's mood
mood = "sad"

#Alter Barley's mood if the happiness score is greater than or equal to 10
if happiness_score >= 10:
  mood = "happy"

print(mood)
