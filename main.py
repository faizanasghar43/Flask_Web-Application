import time


def stop_watch():
    print("Press CTRL+C to exit ")
    print("Hrs:Min:Sec")
    hrs = 0
    flag_1 = False
    while hrs <= 24:
        time.sleep(0)
        min = 0
        if flag_1 == True :
            break
        while min <= 60:
            time.sleep(0)
            sec = 1
            while sec <= 60:
                if flag_1 == True:
                    break
                time.sleep(1)
                print(hrs, ":", min, ":", sec)
                sec = sec + 1
            min = min + 10
            if min >= 1:
                flag_1 = True
        hrs = hrs + 1



stop_watch()