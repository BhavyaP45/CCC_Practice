time = input().split(":")

time = [int(i) for i in time]
time_minute = time[0]*60 + time[1]
rush_hour = [15*60, 19*60]

if time_minute < 600:
    rush_hour = [7*60, 10*60]
distance = 120

time_until_rush = rush_hour[0] - time_minute
while distance > 0:
   if rush_hour[0] <= time_minute < rush_hour[1]:
      minus = (rush_hour[1] - time_minute)//2
      if (rush_hour[1] - time_minute)//2 > distance:
         minus = distance 
      time_minute += minus * 2
      distance -= minus

   elif time_minute < rush_hour[0]:
      minus = (rush_hour[0] - time_minute)
      if (rush_hour[0] - time_minute)//2 > distance:
         minus = distance
      time_minute += minus
      distance -= minus
   else:
    time_minute += distance 
    distance = 0
   print(distance, time_minute)

hour, second = divmod(time_minute, 60)

if hour >= 24:
   hour -= 24

if hour < 10:
   hour = "0" + str(hour)

if second == 0:
  second = "00"

print(hour, ":", second, sep = "")


