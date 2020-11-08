speed=int(input('Enter speed: '))
time=int(input('Enter time: '))
if speed>=0:
    print(speed*time)
else:
    print(100+ (speed*time))