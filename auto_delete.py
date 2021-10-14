import time
import os


def delete():
    while True:
        time.sleep(6)
        if len(os.listdir('/home/ubuntu/yassine/media')) == 0:
            print("Directory is empty")
        else:    
            print("Directory is not empty")
            counter = 1
            print(counter)
            control_while = True
            while control_while:
                time.sleep(1)
                counter += 1
                print(counter)
                if counter == 5:
                    os.system("./rm.sh")
                    control_while = False
                else:
                    control_while = True
delete()
