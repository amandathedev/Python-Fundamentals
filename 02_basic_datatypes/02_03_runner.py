'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

run = input("How many miles did you run in 30 minutes and 30 seconds?")
run = float(run) / 30.5
speed = (run * 60) * 1.6
speed = round(speed, 2)
print("You ran " + str(speed) + " kilometers per hour.")