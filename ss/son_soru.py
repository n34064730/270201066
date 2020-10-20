#If I leave my house at 6:52 am and run 1 mil at an easy pace (8 minutes per mile), then 3 miles at tempo (6 minutes per mile) and 2 mile
#at easy pace again, what time do I get home for breakfast?
first_hour = 6
first_minute = 52
easyv = 1/8
tempov = 1/6
movement_time = (5 / easyv +  3 / tempov)
total_time = movement_time + first_minute

saat = int(total_time // 60)
dakika = int(total_time % 60)
last_hour = saat + first_hour
print("The last time is {}:{}".format(last_hour,dakika))