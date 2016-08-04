import csv
import time
import datetime
from gpiozero import MotionSensor

pir = MotionSensor(4)


"""
Write data to a CSV file path 
    """
def csv_writer(data, path):

    with open(path,"w",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

    """
    Main
    """


data = []
i = 1
while True:
    if pir.motion_detected:
        current_time = str(datetime.datetime.now().time())
        current_date = str(datetime.datetime.now().date())
        data.append( (str(current_date)+","+str(current_time)).split(",") )

        print(datetime.datetime.now())
        path = "Entrance_Logs" + "(" + str(datetime.datetime.now().date()) + ")"
        csv_writer(data, path)
        time.sleep(5)
        i+=1
        
        
