segundos_str = input("Por Favor, Entre com o número de segundos que deseja converter: ")
total_seg = int(segundos_str)

horas = total_seg // 3600
segs_restantes = total_seg % 3600
minutos = segs_restantes // 60

segs_restantes_finais = segs_restantes % 60
dias = total_seg // 35760
print(horas, "Horas, ", minutos, "Minutos e ", segs_restantes_finais, "Segundos.")
print("São", dias, "Dias." )
