import time

def countdown(seconds, boomTime):
    while seconds:
        if seconds == boomTime:
            print("Kaaaaaaaboooooooom!")
            break

        print("Time remaining:", seconds, "seconds.")
        time.sleep(1)
        seconds -= 1
while True:
    a = int(input("Enter a number to countdown: "))
    b = int(input("Enter a number to finish up the countdown: "))

    if a > b:
        countdown(a, b)
        break
    else:
        print("Countdown should be more than the time to finish. Please try again.")