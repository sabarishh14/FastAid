
try:
    import os
    import csv
    import time
    import webbrowser as w
    import COVID19Py

except:
    os.system('python -m pip install csv')
    os.system('python -m pip install time')
    os.system('python -m pip install webbrowser')
    os.system('python -m pip install COVID19Py')

covid19 = COVID19Py.COVID19()
print("""
          .---------------------------------------------------------------------------------------------------------.
          |                                                                                                         |
          |    8888888888     d8888   .d8888b. 88888888888        +++++++               d8888 8888888 8888888b.     |
          |    888           d88888  d88P  Y88b    888            +:::::+              d88888   888   888  "Y88b    |
          |    888          d88P888  Y88b.         888       ++++++:::::++++++        d88P888   888   888    888    |
          |    8888888     d88P 888   "Y888b.      888       +:::::::::::::::+       d88P 888   888   888    888    |
          |    888        d88P  888      "Y88b.    888       +:::::::::::::::+      d88P  888   888   888    888    | 
          |    888       d88P   888        "888    888       ++++++:::::++++++     d88P   888   888   888    888    |
          |    888      d8888888888  Y88b  d88P    888            +:::::+         d8888888888   888   888  .d88P    |
          |    888     d88P     888   "Y8888P"     888            +++++++        d88P     888 8888888 8888888P      |
          |                                                                                                         |
          |                   'FOR THE BEST AND FIRST AID, USE FAST AID' - CREATORS OF FAST AID                     |  
          |                                                                                                         |
          .---------------------------------------------------------------------------------------------------------.

                                         <<<<<<<<<   WELCOME TO FAST AID !!!!  >>>>>>>>>
 
                                                            DONE BY:

                                         <<<<<    ADITYA A    : XII - COMMERCE    >>>>>
                                         <<<<<    SABARISH SB : XII - SCIENCE     >>>>>
                                         <<<<<    GOPAL RATHI : XII - COMMERCE    >>>>>""")
print()
time.sleep(0.5)
print("                       FAST AID is an app which gives you precise details on Emergency Situations and Queries")
def main():
    while True:
        print()
        options()

def thanksdes():
    print("""
88888888888 888    888        d8888 888b    888 888    d8P      Y88b   d88P  .d88888b.   888     888 
    888     888    888       d88888 8888b   888 888   d8P        Y88b d88P  d88P" "Y88b  888     888 
    888     888    888      d88P888 88888b  888 888  d8P          Y88o88P   888     888  888     888 
    888     8888888888     d88P 888 888Y88b 888 888d88K            Y888P    888     888  888     888 
    888     888    888    d88P  888 888 Y88b888 8888888b            888     888     888  888     888 
    888     888    888   d88P   888 888  Y88888 888  Y88b           888     888     888  888     888 
    888     888    888  d8888888888 888   Y8888 888   Y88b          888     Y88b. .d88P  Y88b. .d88P 
    888     888    888 d88P     888 888    Y888 888    Y88b         888      "Y88888P"    "Y88888P"  
                                                                                                   
               <<<<<<< For Using FAST AID Services... Please Visit Us Again >>>>>>> """)

def covicheckdes():
    print("""
                        <<<<< FAST AID'S >>>>>
      __________ _    __________       ________  ________________ __
     / ____/ __ \ |  / /  _/ __ \     / ____/ / / / ____/ ____/ //_/
    / /   / / / / | / // // / / /    / /   / /_/ / __/ / /   /  ,<   
   / /___/ /_/ /| |/ // // /_/ /    / /___/ __  / /___/ /___/ /| |  
   \____/\____/ |___/___/_____/     \____/_/ /_/_____/\____/_/ |_|  
                                                                 """)

def covistatsdes():
    print("""
                        <<<<< FAST AID'S >>>>>
      __________ _    __________       ______________  ___________
     / ____/ __ \ |  / /  _/ __ \     / ___/_  __/   |/_  __/ ___/
    / /   / / / / | / // // / / /     \__ \ / / / /| | / /  \__ \ 
   / /___/ /_/ /| |/ // // /_/ /     ___/ // / / ___ |/ /  ___/ / 
   \____/\____/ |___/___/_____/     /____//_/ /_/  |_/_/  /____/  
                                                               
  """)

def emergendes():
    print("""
  _____ __  __ _____ ____   ____ _____ _   _  ______   __
 | ____|  \/  | ____|  _ \ / ___| ____| \ | |/ ___\ \ / /
 |  _| | |\/| |  _| | |_) | |  _|  _| |  \| | |    \ V / 
 | |___| |  | | |___|  _ <| |_| | |___| |\  | |___  | |  
 |_____|_|  |_|_____|_| \_ \\____|_____|_| \_|\____| |_|  
                                                         
     _____ _    ____ _____       _    ___ ____  
    |  ___/ \  / ___|_   _|     / \  |_ _|  _ \ 
    | |_ / _ \ \___ \ | |      / _ \  | || | | |
    |  _/ ___ \ ___) || |     / ___ \ | || |_| |
    |_|/_/   \_\____/ |_|    /_/   \_\___|____/ """)
                                                                                                        
def options():
    time.sleep(1)
    print(" The options are : ")
    time.sleep(1)
    print()
    print(" 1. SIGN UP - For Creating A New Account")
    print(" 2. SIGN IN - For Booking Appointments In The Hospitals")
    print(" 3. EMERGENCY FAST AID LOGIN - For Emergencies")
    print(" 4. FAST AID COVID-19 CHECK")
    print(" 5. COVID-19 STATS")
    print(" 6. ADMIN SERVICES - For Program Developers")
    print(" 7. EXIT")
    print()
    time.sleep(2)
    opt1=input(" Enter which option you choose : ")
    if opt1=='1':
        signup()
    if opt1=='2':
        signin()
    if opt1=='6':
        admin()
    if opt1=='3':
        medfastaid()
    if opt1=='4':
        fastcovid()
    if opt1=='5':
        covidstats()
    if opt1=='7':
        print()
        time.sleep(1)
        thanksdes()
        time.sleep(3)
        quit()
    else:
        print()
        print("You Have Entered An Incorrect Option...")

def optwosusi():
    time.sleep(1)
    print(" The options are : ")
    time.sleep(1)
    print()
    print(" 1. NEW APPOINTMENTS - For Booking New Appointments In The Hospitals")
    print(" 2. EMERGENCY FAST AID LOGIN - For Emergencies")
    print(" 3. FAST AID COVID-19 CHECK")
    print(" 4. COVID-19 STATS")
    print(" 5. EXIT")
    print()
    time.sleep(2)
    opt1=input(" Enter which option you choose : ")
    if opt1=='1':
        mainfastaid()
    if opt1=='2':
        medfastaid()
    if opt1=='3':
        fastcovid()
    if opt1=='4':
        covidstats()
    if opt1=='5':
        print()
        time.sleep(1)
        thanksdes()
        time.sleep(3)
        quit()
    else:
        print()
        print("You Have Entered An Incorrect Option...")

def signup():    
    print("""
 ____ ___ ____ _   _    _   _ ____  
/ ___|_ _/ ___| \ | |  | | | |  _ \ 
\___ \| | |  _|  \| |  | | | | |_) |
 ___) | | |_| | |\  |  | |_| |  __/ 
|____/___\____|_| \_|   \___/|_|     """)
    print()
    fname=input("Enter Your Sweet Name : ")
    un=input("Enter Your Username : ")
    if un=="":
        print("**** Sorry, Username Can't Be Empty !! ****")
        signup()
    f=open("USER DATA FA.csv","r")
    data=list(csv.reader(f))
    for i in range(len(data)):
        if un==data[i][1]:
            print()
            print("**** Username Taken. Please Try A Different One !! ****")
            signup()
    pwd=input("Enter Your Password : ")
    if len(pwd)<8:
        print()
        print("**** Sorry, Length Of Password Should Be 8 or More Characters ****")
        signup()
    if un==pwd:
        print()
        print("**** Sorry, Username and Password Should Not Be The Same ****")
        signup()
    else:
        repwd=input("Re-Enter your Password : ")
        if pwd==repwd:
            try:
                num=int(input("Enter Your Phone Number : "))
                gender=input("Enter Your Gender ( M/F ): ")
                email=input ("Enter Your E-Mail Id : ")
                data=[fname,un,pwd,num,gender,email]
                print()
                f=open("USER DATA FA.csv",'a',newline='')
                cw=csv.writer(f)
                cw.writerow(data)
                f.close()
                print("""
88888888888 888    888        d8888 888b    888 888    d8P      Y88b   d88P  .d88888b.   888     888 
    888     888    888       d88888 8888b   888 888   d8P        Y88b d88P  d88P" "Y88b  888     888 
    888     888    888      d88P888 88888b  888 888  d8P          Y88o88P   888     888  888     888 
    888     8888888888     d88P 888 888Y88b 888 888d88K            Y888P    888     888  888     888 
    888     888    888    d88P  888 888 Y88b888 8888888b            888     888     888  888     888 
    888     888    888   d88P   888 888  Y88888 888  Y88b           888     888     888  888     888 
    888     888    888  d8888888888 888   Y8888 888   Y88b          888     Y88b. .d88P  Y88b. .d88P 
    888     888    888 d88P     888 888    Y888 888    Y88b         888      "Y88888P"    "Y88888P"  
                                                                                                   
                          <<<<<<< For Registering To FAST AID >>>>>>> """)
                print()
                signin()
            except ValueError:
                print()
                print("**** Phone Number Should Only Be In Numbers !!! ****")
                signup()
        else:
            print()
            print("**** Sorry Re-entered Password Incorrect !!! ****")
            signup()
            
def mainfastaid():
    appt={1:'7:00 A.M - 9.00 A.M',2:'9.00 A.M - 11:00 A.M',3:'11:00 A.M - 1:00 P.M',4:'1:00 P.M - 3:00 P.M',5:'3:00 P.M - 5:00 P.M',6:'5:00 P.M - 7:00 P.M',7:'7:00 P.M - 9:00 P.M'}
    meddept={1:'PHYSICAL MEDICINE',2:'PAEDIATRICS',3:'GENERAL MEDICINE',4:'REHABILITATION',5:'INDIAN THERAPHY',6:'PSYCHOLOGY',7:'ONCOLOGY'}
    areadic={1:'T-NAGAR',2:'ANNA NAGAR',3:'GUINDY',4:'PERAMBUR',5:'NUNGAMBAKKAM',6:'MYLAPORE',7:'VELACHERY',8:'TAMBARAM',9:'KILPAUK',10:'KOYAMBEDU'}
    flag=0
    time.sleep(1)
    print("<<<<<<<<< Welcome To FAST AID MEDICAL SERVICES >>>>>>>>>> ")
    time.sleep(0.5)
    print("We Give The Best and Easiest SOLUTIONS For Any Medical Issue You Face...")
    print()
    time.sleep(2)
    print("Areas Of Medical Issue : ")
    print()
    print("1. PHYSICAL MEDICINE ( HEAD, BODY, JOINT PAIN )")
    print("2. PAEDIATRICS ( CHILD CARE SPECIALISTS )")
    print("3. GENERAL MEDICINE ( ADULT CARE [ COLD,COUGH,ETC. ] )")
    print("4. REHABILITATION ( DRUG AND ALCOHOL CURE )")
    print("5. INDIAN THERAPHY ( AYURVEDA, HOMEOPATHY, NATUROPATHY )")
    print("6. PSYCHOLOGY ( FOR MENTAL HEALTH )")
    print("7. ONCOLOGY ( CANCER TREATMENT )")
    print()
    deptopt=int(input("Which Department Do You Want Take An Appointment From The Above ? "))
    print()
    if deptopt>7:
        print("You Have Entered An Incorrect Option !!!")
        print()
        mainfastaid()
    time.sleep(1)
    print("Area Where You Stay In Chennai :")
    print()
    print("1. T-NAGAR")
    print("2. ANNA NAGAR")
    print("3. GUINDY") 
    print("4. PERAMBUR")
    print("5. NUNGAMBAKKAM")
    print("6. MYLAPORE")
    print("7. VELACHERY")
    print("8. TAMBARAM")
    print("9. KILPAUK")
    print("10. KOYAMBEDU")
    print()
    areaopt=int(input("Where Do You Stay In Chennai ? "))
    print()
    if areaopt>10:
        print("You Have Entered An Incorrect Option !!!")
        print()
        mainfastaid()
    time.sleep(1)
    print("Appointment Timings : ")
    print()
    print("1. 7:00 A.M - 9.00 A.M")
    print("2. 9.00 A.M - 11:00 A.M")
    print("3. 11:00 A.M - 1:00 P.M")
    print("4. 1:00 P.M - 3:00 P.M")
    print("5. 3:00 P.M - 5:00 P.M")
    print("6. 5:00 P.M - 7:00 P.M")
    print("7. 7:00 P.M - 9:00 P.M")
    print()
    apptime=int(input("Enter Your Option Number : "))
    if apptime>7:
        print("You Have Entered An Incorrect Option !!!")
        print()
        mainfastaid()
    time.sleep(0.5)
    with open("DOCTORS DATABASE.csv",'r') as f :
        data=list(csv.reader(f))
        for i in range(len(data)):
            if data[i][1]==meddept[deptopt] and data[i][2]==areadic[areaopt]:
                flag=1
                print()
                time.sleep(1.5)
                print("The Doctors Details Are As Follows : ")
                print(data[i][3])
                print()
                print("You Have To First Video Call The Doctor On",data[i][4],"Between",appt[apptime])
                print("Then Depending Upon Your Issue, You Will Be Instructed By The Doctor")
                print()
                conti=input("Do You Want To Continue ( YES/NO ) : ").upper()
                print()
                if conti=="YES" or conti=='Y':
                    optwosusi()
                else:
                    time.sleep(1)
                    thanksdes()
                    time.sleep(3)
                    quit()
        if flag==0:
            print("****** THE ENTERED DEPARTMENT OR AREA IS OUT OF THE LIST... ******")
            print()
            mainfastaid()

def admin():
    print("""
  _____ _    ____ _____      _    ___ ____       _    ____  __  __ ___ _   _ 
 |  ___/ \  / ___|_   _|    / \  |_ _|  _ \     / \  |  _ \|  \/  |_ _| \ | |
 | |_ / _ \ \___ \ | |     / _ \  | || | | |   / _ \ | | | | |\/| || ||  \| |
 |  _/ ___ \ ___) || |    / ___ \ | || |_| |  / ___ \| |_| | |  | || || |\  |
 |_|/_/   \_\____/ |_|   /_/   \_\___|____/  /_/   \_\____/|_|  |_|___|_| \_|""")
    print()
    aid=input("Enter Admin ID : ")
    apwd=input("Enter Admin Password : ")
    if aid=="admin" and apwd=="techbuffs2020":
        print()
        time.sleep(0.5)
        print("1. VIEW ALL ACCOUNT DETAILS")
        print("2. DELETE AN ACCOUNT")
        print()
        time.sleep(0.5)
        optad=int(input("Enter Your Option : "))
        if optad==1:
            str=""
            a=""
            f=open("USER DATA FA.csv","r")
            data=list(csv.reader(f))
            for i in data:
                for j in i:
                    a+=j+"\t\t"
                a+="\n"
            str+=a
            print()
            time.sleep(0.5)
            print("Name\t\tUsername\tPassword\t\tPhone Number\tGender\t\tEmail ID")
            print()
            time.sleep(0.25)
            print(str)
            conti=input("Do You Want To Continue ( YES/NO ) : ").upper()
            if conti=="YES" or conti=="Y":
                print()
                options()
            else:
                time.sleep(1)
                thanksdes()
                time.sleep(3)
                quit()
        if optad==2:
                delacc()
        else:
            print("Sorry, Please Enter A Correct Option !!")
            
    else:
        print("Sorry, Invalid User ID Or Password !!")
        
def signin():
    flag=0
    print ("""
  ____ ___ ____ _   _     ___ _   _ 
 / ___|_ _/ ___| \ | |   |_ _| \ | |
 \___ \| | |  _|  \| |    | ||  \| |
  ___) | | |_| | |\  |    | || |\  |
 |____/___\____|_| \_|   |___|_| \_|""")
    print()
    uncheck=input("Enter your username : ")
    pwdcheck=input("Enter your password : ")
    print()
    with open("USER DATA FA.csv",'r') as f :
        data=list(csv.reader(f))
        for i in range(len(data)):
            if data[i][1]==uncheck and data[i][2]==pwdcheck:
                flag=1
                print("****** LOGIN SUCCESFUL !! ******")
                print()
                mainfastaid()
        if flag==0:
            print("****** LOGIN FAILED !! CHECK YOUR USERNAME OR PASSWORD... ******")
            print()
            signin()

def delacc():
    print()
    print("""
     _    ____ ____ ___  _   _ _   _ _____    ____  _____ _     _____ _____ ___ ___  _   _ 
    / \  / ___/ ___/ _ \| | | | \ | |_   _|  |  _ \| ____| |   | ____|_   _|_ _/ _ \| \ | |
   / _ \| |  | |  | | | | | | |  \| | | |    | | | |  _| | |   |  _|   | |  | | | | |  \| |
  / ___ \ |__| |__| |_| | |_| | |\  | | |    | |_| | |___| |___| |___  | |  | | |_| | |\  |
 /_/   \_\____\____\___/ \___/|_| \_| |_|    |____/|_____|_____|_____| |_| |___\___/|_| \_|""")
    print()
    flag=0
    f1=open("USER DATA FA.csv","r")
    det=list(csv.reader(f1))
    un=input ("Enter your username : ")
    pwd=input ("Enter your password : ")
    for i in range (len(det)):
        if det [i][1]== un and det[i][2]==pwd:
            flag=1
            del det[i]
            print()
            print("Your Account Is Successfully Deleted !!!")
            f2=open("USER DATA FA.csv","w",newline="")
            cw=csv.writer(f2)
            cw.writerows(det)
            f2.close()
            break
    if flag==0:
        print()
        print("Sorry, Account Not Found !!!")
    f1.close()
    print()
    conti=input("Do You Want To Continue ( YES/NO ) : ").upper()
    if conti=="YES" or conti=="Y":
        print()
        options()
    else:
        time.sleep(1)
        thanksdes()
        time.sleep(3)
        quit()

def medfastaid():
    emmeddept={1:"CARDIOLOGY",2:"EMERGENCY",3:"PHARMACY"}
    emarea={1:'T-NAGAR',2:'ANNA NAGAR',3:'GUINDY',4:'PERAMBUR',5:'NUNGAMBAKKAM',6:'MYLAPORE',7:'VELACHERY',8:'TAMBARAM',9:'KILPAUK',10:'KOYAMBEDU'}
    emergendes()
    print()
    emfanum=int(input("Enter Your Phone Number : "))
    print()
    print("Which Area Do You Have A Emergency ? ")
    print()
    print("1. CARDIOLOGY ( HEART RELATED  )")
    print("2. EMERGENCY ( SEVERE PHYSICAL INJURY AND PREGNANCY )")
    print("3. PHARMACY ( FOR CONTACTING EMERGENCY PHARMACISTS ) ")
    print()
    emdepopt=int(input("Enter Your Option Number : "))
    print()
    time.sleep(1)
    print("Areas Where You Stay In Chennai :")
    print()
    print("1. T-NAGAR")
    print("2. ANNA NAGAR")
    print("3. GUINDY") 
    print("4. PERAMBUR")
    print("5. NUNGAMBAKKAM")
    print("6. MYLAPORE")
    print("7. VELACHERY")
    print("8. TAMBARAM")
    print("9. KILPAUK")
    print("10. KOYAMBEDU")
    print()
    emareaopt=int(input("Where Do You Stay In Chennai ? "))
    print()
    time.sleep(0.5)
    with open("DOCTORS DATABASE.csv",'r') as f :
        data=list(csv.reader(f))
        for i in range(len(data)):
            if data[i][1]==emmeddept[emdepopt] and data[i][2]==emarea[emareaopt]:
                flag=1
                time.sleep(1.5)
                print("The Hospitals Details Are As Follows : ")
                print(data[i][3])
                print()
                print("You Can Contact Them On",data[i][4])
                print()
                if emmeddept[emdepopt]=="PHARMACY":
                    pass
                elif emmeddept[emdepopt]=="EMERGENCY" or emmeddept[emdepopt]=="CARDIOLOGY":
                    print(data[i][5])
                    print()
                conti=input("Do You Want To Continue ( YES/NO ) : ").upper()
                print()
                if conti=="YES" or conti=='Y':
                    options()
                else:
                    time.sleep(1)
                    thanksdes()
                    time.sleep(3)
                    quit()
        if flag==0:
            print("****** THE ENTERED DEPARTMENT OR AREA IS OUT OF THE LIST... ******")
            print()
            mainfastaid()
            

def fastcovid():
    url1="https://www.amazon.in/Dettol-Original-Protection-Alcohol-Sanitizer/dp/B088KJWGB5/ref=sr_1_5?dchild=1&keywords=sanitizer&qid=1607245499&sr=8-5"
    url2="https://www.amazon.in/Gear-ProShield-Reusable-Layer-Facemask/dp/B08C858KTF/ref=sr_1_5?dchild=1&keywords=mask&qid=1607255606&sr=8-5"
    points=0
    print()
    covicheckdes()
    print()
    print("Please Answer 'Yes' OR 'No' For Questions For This Simple COVID-19 Check.")
    print("Your Answers Will Determine Your Results For This COVID-19 Check.")
    print()
    qtn1=input("Were You Having FEVER In Recent Times ? ").upper()
    if qtn1=='NO' or qtn1=='N' or qtn1=='n':
        points+=1
    qtn2=input("Were You Having DRY COUGH In Recent Times ? ").upper()
    if qtn2=='NO' or qtn2=='N' or qtn2=='n':
        points+=1
    qtn3=input("Were You Having DIFFICULTY IN BREATHING or SHORTNESS OF BREATH In Recent Times ? ").upper()
    if qtn3=='NO' or qtn3=='N' or qtn3=='n':
        points+=1
    qtn4=input("Were You Becoming FREQUENTLY TIRED In Recent Times ? ").upper()
    if qtn4=='NO' or qtn4=='N' or qtn4=='n':
        points+=1
    qtn5=input("Were You Having CHEST PAIN In Recent Times ? ").upper()
    if qtn5=='NO' or qtn5=='N' or qtn5=='n':
        points+=1
    print()
    if points==0:
        print("RESULT :")
        print("You Have Scored 0/5 In Our Fast 'COVID-19' Check")
        print("It Seems That You Need Major Doctor Assistance As Soon As Possible !!")
        print("Please Visit The Doctor Immediately...")
        print()
    elif points==1:
        print("RESULT :")
        print("You Have Scored 1/5 In Our Fast 'COVID-19' Check")
        print("It Looks Like Your Body Is Not In The Best Condition !!")
        print("Please Visit The Doctor Immediately For Best Assistance...")
    elif points==2:
        print("RESULT :")
        print("You Have Scored 2/5 In Our Fast 'COVID-19' Check")
        print("It Feels Like You Should Have A Conversation With A Doctor , ")
        print("Since You Are Facing A Little Bit Of A Difficulty... ")
    elif points==3:
        print("RESULT :")
        print("You Have Scored 3/5 In Our Fast 'COVID-19' Check")
        print("Doesn't Look Like Your Body Isn't In The Best Condition It Should Be !!")
        print("Please Take All The COVID-19 Precautionary Measures & Stay Safe...")
    elif points==4:
        print("RESULT :")
        print("You Have Scored 4/5 In Our Fast 'COVID-19' Check")
        print("It Looks Like Your Body Needs An Oil Refill :) ")
        print("Please Let The Doctor Know How You Are Feeling, So That He Could Service It For YOU !!")
    elif points==5:
        print("RESULT :")
        print("You Have Scored 5/5 In Our Fast 'COVID-19' Check")
        print("You Are Perfectly Safe & Have No Serious Symptoms Of COVID-19")
        print("Continue To Take Care Of Yourself & Stay Safe :)")
    print()
    prod1=input("Do You Want To Buy A Sanitizer ? (YES/NO) ").upper()
    if prod1=='YES' or prod1=='Y':
        w.open_new(url1)   
    print()
    prod2=input("Do You Want To Buy A Mask ? (YES/NO) ").upper()
    if prod2=='YES' or prod2=='Y':
        w.open_new(url2)
    time.sleep(8)
    print()
    print("READ THIS !!")
    print()
    time.sleep(2)
    print("COVID-19 Precautionary Measures You Should Follow :")
    print()
    print("1. Wear A Mask At All Times & Sanitise Your Hands Once A While When Outside...") 
    print("2. Stay Atleast 1 Metre Away From Everyone At All Times...")
    print("3. Avoid Crowded Places And Gathering As Much As Possible...")
    print("4. Avoid Touching Your Eyes, Nose And Mouth...")
    print("5. Cover Coughs & Sneezes With A Bent Elbow. Wash Your Hands Then...")
    print()
    print("Thank You For Using FAST AID 'COVID-19' Check !!!")
    print()
    conti=input("Do You Want To Continue ( YES/NO ) : ").upper()
    print()
    if conti=="NO" or conti=="N":
        time.sleep(1)
        thanksdes()
        time.sleep(3)
        quit()
    else:
        options()
        
    
        
def covidstats():
    covistatsdes()
    print()
    print("Which country's COVID-19 Stats Do You Want To See ?")
    print("1. INDIA")
    print("2. BAHRAIN")
    print("3. USA")
    print("4. AUSTRALIA")
    print("5. CHINA")
    print()
    covidopt=input("Which option do you chose from the above ? : ")
    print()
    if covidopt=='1':
        location = covid19.getLocationByCountryCode("IN")
        print('* Total Number Of Confirmed Cases In India Are : ',location[0]['latest']['confirmed'])
        print('* Total Number Of Death Cases In India Are : ',location[0]['latest']['deaths'])
        print()
        print("Thank You For Using Fast Aid 'COVID-19' Stats !!!!")
        print()
    elif covidopt=='2':
        location = covid19.getLocationByCountryCode("BH")
        print('* Total Number Of Confirmed Cases In Bahrain Are : ',location[0]['latest']['confirmed'])
        print('* Total Number Of Death Cases In Bahrain Are : ',location[0]['latest']['deaths'])
        print()
        print("Thank You For Using Fast Aid 'COVID-19' Stats !!!!")
        print()
    elif covidopt=='3':
        location = covid19.getLocationByCountryCode("US")
        print('* Total Number Of Confirmed Cases In United States Are : ',location[0]['latest']['confirmed'])
        print('* Total Number Of Death Cases In United States Are : ',location[0]['latest']['deaths'])
        print()
        print("Thank You For Using Fast Aid 'COVID-19' Stats !!!!")
        print()
    elif covidopt=='4':
        location = covid19.getLocationByCountryCode("AU")
        print('* Total Number Of Confirmed Cases In Australia Are : ',location[0]['latest']['confirmed'])
        print('* Total Number Of Death Cases In Australia Are : ',location[0]['latest']['deaths'])
        print()
        print("Thank You For Using Fast Aid 'COVID-19' Stats !!!!")
        print()
    elif covidopt=='5':
        location = covid19.getLocationByCountryCode("CN")
        print('* Total Number Of Confirmed Cases In China Are : ',location[0]['latest']['confirmed'])
        print('* Total Number Of Death Cases In China Are : ',location[0]['latest']['deaths'])
        print()
        print("Thank You For Using Fast Aid 'COVID-19' Stats !!!!")
        print()
    else:
        print("Please Enter A Correct OPTION !!!")
        print()
        
    conti=input("Do You Want To Continue ( YES/NO ) : ").upper()
    if conti=="YES" or conti=="Y":
        print()
        options()
    else:
        time.sleep(1)
        thanksdes()
        time.sleep(3)
        quit()

    
main()
