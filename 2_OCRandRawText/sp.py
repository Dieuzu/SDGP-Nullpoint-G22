def Separatetxt(filename):
   f = open(filename)
   print("[SYSTEM] Dividing Task into seperate files\n")
   
   str1 = ""
   str2 = ""
   str3 = ""
   
   for x, line in enumerate(f):
         if  x == 14 :
            str1 = line
            a = open('output\\Raw\\Task_1.txt', 'w')
            print("[SYSTEM] Task 1 save successfully\n")
            a.write(str1)
            a.close()

         if x == 18 :
            str2 = line
            b = open('output\\Raw\\Task_2.txt', 'w')
            print("[SYSTEM] Task 2 save successfully\n")
            b.write(str2)
            b.close()

         if x == 22:
            str3 = line
            c = open('output\\Raw\\Task_3.txt', 'w')
            print("[SYSTEM] Task 3 save successfully\n")
            c.write(str3)
            c.close()
         
   f.close()