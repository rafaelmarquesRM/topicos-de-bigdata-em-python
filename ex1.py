notaAv = 4
sim1 = 1
sim2 = 0

notaAvs = 5
nota = notaAv + sim1 + sim2
notaFinal = notaAvs + sim1 + sim2
media = 6
pres = 76

filhoDeMiliciano = True


if (nota>=media and pres>=75):
  print("Passou")

elif (notaFinal>=media):
  print("Passou na AVS")
  
elif (filhoDeMiliciano == True):
  print("Passou direto")

  
  
else:
  print("Reprovou")
