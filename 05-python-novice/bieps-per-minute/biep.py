import schedule
# import time


def tijd():
    print("Biep!")


schedule.every(1).minutes.do(tijd)

while True:
    schedule.run_pending()
