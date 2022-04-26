def Separatetxt(filename):
   import Json
   f = open(filename)
   print("[SYSTEM] Dividing Task into seperate files\n")
   
   str1 = ""
   str2 = ""
   str3 = ""
   str4 = ""
   str5 = ""

   for x, line in enumerate(f):
      if  x == 12 :
         str1 = line
      elif x == 13:
         str2 = line
         a = open('output\Raw\Task_3.txt', 'w')
         print("[SYSTEM] Task 3 save successfully\n")
         a.write(str1+str2)
         a.close()

      if x == 9 :
         str3 = line
      elif x == 10:
         str4 = line
         b = open('output\Raw\Task_2.txt', 'w')
         print("[SYSTEM] Task 2 save successfully\n")
         b.write(str3+str4)
         b.close()

      if x == 7:
         str5 = line
         c = open('output\Raw\Task_1.txt', 'w')
         print("[SYSTEM] Task 1 save successfully\n")
         c.write(str5)
         c.close()
         
   f.close()