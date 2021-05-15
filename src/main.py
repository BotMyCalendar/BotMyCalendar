import schedule
import sched
import time
import queue
from datetime import datetime
import struct
import googleCalendar

# lista de cumples

# cumpleaños_persona[
#         cumple{
#             'summary': string
#             'date': datetime
#             'homored': string
#             'message': string
#         }
# ]

def iterar():
    birthdays = googleCalendar.getBirthdays()
    if len(birthdays) != 0:
        for birthday in birthdays:
            honored = birthday['honored']
            mensaje = birthday['message']
            googleCalendar.sendMessage(honored, mensaje)
    else :
        print("No hay cumpleaños")
    

googleCalendar.bootDiscord()
time.sleep(5)

#schedule.every(1).seconds.do(iterar)
actualTime = datetime.now().strftime("%H:%M")
actualTime = actualTime[0:3]+str(int(actualTime.split(":")[1])+1)
print("Bot My Calendar will request you permissions at "+actualTime)
schedule.every().day.at(actualTime).do(iterar)

while True:
    schedule.run_pending()
    time.sleep(1)