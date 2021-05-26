import schedule


def time():
    print("Biep")


schedule.every(1).minutes.do(time)
