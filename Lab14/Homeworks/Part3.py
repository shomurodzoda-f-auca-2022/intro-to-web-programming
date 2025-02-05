import time
def countdown(seconds):
    while seconds > 0:
        print("Seconds remaining:", seconds)
        time.sleep(1)
        seconds -= 1

a = int(input("Enter a countdown seconds: "))
countdown(a)
print("Time is up!")