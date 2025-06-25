import schedule
import time

def print_loop(data):
    schedule.every(3).seconds.do(lambda: print(data))
    while True:
        schedule.run_pending()
        time.sleep(1)