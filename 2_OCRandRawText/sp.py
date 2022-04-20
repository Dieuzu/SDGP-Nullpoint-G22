def Separatetxt(filename):
   f = open(filename)
   
   str1 = ""
   str2 = ""
   str3 = ""
   
   for x, line in enumerate(f):
         if  x == 14 :
            str1 = line
            a = open('D:\campus\\text\Task_1.txt', 'w')
            a.write(str1)
            a.close()

         if x == 18 :
            str2 = line
            b = open('D:\campus\\text\Task_2.txt', 'w')
            b.write(str2)
            b.close()

         if x == 22:
            str3 = line
            c = open('D:\campus\\text\Task_3.txt', 'w')
            c.write(str3)
            c.close()
         
   f.close()