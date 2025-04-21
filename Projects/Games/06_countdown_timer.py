import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')  # \r brings cursor back to start of line
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

try:
    timing = int(input("Enter time in seconds: "))
    countdown_timer(timing)
except ValueError:
    print("Please enter a valid number!")
