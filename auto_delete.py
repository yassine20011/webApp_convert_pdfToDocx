import time
import os

path = 'app/media'

def delete():
    while True:
        time.sleep(3)
        if len(os.listdir(path)) == 0:
            print("Directory is empty")
        else:
            print("Directory is not empty")
            counter = 1
            #print(counter)
            control_while = True
            while control_while:
                time.sleep(1)
                counter += 1
                print(counter)
                if counter == 60*60:
                    os.system("./rm.sh")
                    control_while = False
                else:
                    control_while = True
delete()
