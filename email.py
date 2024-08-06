email = input("Enter your E-mail: ")
k=0

if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-3]==".") ^ (email[-4]=="."):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            k=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                         k=1
                for i in email[(email.index("@")):(email.index("."))]:
                    if i.isdigit():
                        k=1
                
                if k==1:
                  print("Wrong Email")
                else:
                    print("Its correct Email")
            else:
                print("Wrong Email")
        else:
            print("Wrong Email")
    else:
        print("Wrong Email")
else:
    print("Wrong Email")
