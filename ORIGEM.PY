from datetime import datetime, timedelta
horap = input ("Que horas você entrou? ")
hora = datetime.strptime(horap, "%H:%M")
ex = timedelta (hours=8, minutes=50)
hora_final = hora + ex
print ("Horario de saida:", hora_final.strftime("%H:%M"))
hora_maxima = timedelta (hours=2, minutes=00)
hora_extra = hora_final + hora_maxima
print ("Seu horário maximo final com hora extra é :", hora_extra.strftime("%H:%M"))