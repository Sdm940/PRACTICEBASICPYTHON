a=3
while a>0:
    p=int(input("ENTER YOUR PASSWORD: "))
    L=input("ENTER YOUR LOGIN: ")
    if p==5678 and L=="admin":
        print("ACCESS GRANTED")
        break
    else:
         print("ACCESS DENIED")
         a=a-1
         continue