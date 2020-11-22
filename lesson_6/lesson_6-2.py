def countdown(func):
    import time
    def seconds(*args):
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        func(*args)
    return seconds
@countdown
def time_now():
    import time
    print(time.strftime('%H:%M', time.localtime()))
print("What time is now? ")
time_now()