import schedule
import sched
import time
import queue
import datetime
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
today = datetime.date.today()
def iterar():
    i=0
    birthdays=googleCalendar.getBirthdays()
    if len(birthdays)!=0:
        date= birthdays[i]['date']
        while date.day == today.day and date.month==today.month:
            honored=birthdays[i]['honored']
            mensaje=birthdays[i]['message']
            googleCalendar.sendMessage(honored, mensaje)
            i=i+1
            date = birthdays[i]['date']
    else :
        print("No hay cumpleaños")
    # print(date)
    


# def obtener_fechas():
# def jobs():
   # print(all_jobs)


googleCalendar.bootDiscord()
time.sleep(5)

schedule.every(30).seconds.do(iterar)
schedule.every().day.at("13:48").do(iterar)
# all_jobs=schedule.get_jobs()
while True:
     schedule.run_pending()
     time.sleep(1)