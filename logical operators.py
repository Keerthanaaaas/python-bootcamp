age=int(input())
if(age>18):
  if(age>18 and age<24):
      print("elegble for 2 wheeler")
  elif(age>24 and age<45):
      print("elegble for both 2 and 4 wheeler")
  else(age>45):
      print("elgeble for 2 and 4 and 6 wheeler")
else:
  print("not elgible")