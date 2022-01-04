from BAExcept import DepositError,WithdrawError,InsuffFundError,InvalidAccountError
import random,sys
from BAmenu import Amenu
import cx_Oracle
con=cx_Oracle.connect('surya','AshoK1775')
bcur=con.cursor()
acur=con.cursor()
totm=500
def deposit():
          pn=int(input("Enter your ATM pin:"))
          acur.execute("select * from atm where pin=%d"%pn)
          if((pn>=1000)and(pn<10000)):
                    for data in acur:
                              if(pn==data[1]):
                                        print("="*60)
                                        nm=float(input("Enter your amount for Deposit:"))
                                        if(nm<=0):
                                                  raise DepositError
                                        else:
                                                  totm=data[2]+nm
                                                  print("Welcome successfully credited balance :",nm)
                                                  print("Youe total amount is :",totm)
                                                  bcur.execute("update bank set Amount=%d where Accountnumber='%s'"%(totm,data[0]))
                                                  acur.execute("update atm set Amount=%d where Accountnumber='%s'"%(totm,data[0]))
                                                  con.commit()
                                                  break
                    else:
                              print("="*60)
                              print("Your ATM Pin is wrong.Please try again")
                              
          else:
                    print("="*60)
                    print("Sorry your ATM pin is wrong. ATM pin should be 4 digits")
          
def withdraw():
          pn=int(input("Enter your pin number of ATM:"))
          acur.execute("select * from atm where pin=%d"%pn)
          if(pn>=1000 and pn<10000):
                    for data in acur:
                              if(pn==data[1]):
                                        print("="*60)
                                        nm=float(input("Enter your amount for Withdraw:"))
                                        if(nm<=0):
                                                  raise WithdrawError
                                        elif(nm+500>data[2]):
                                                  raise InsuffFundError
                                        elif(nm<=data[2]):          
                                                  totm=data[2]-nm
                                                  print("Welcome successfully debited balance :",nm)
                                                  print("Your total amount is :",totm)
                                                  bcur.execute("update bank set Amount=%d where Accountnumber='%s'"%(totm,data[0]))
                                                  acur.execute("update atm set Amount=%d where Accountnumber='%s'"%(totm,data[0]))
                                                  con.commit()
                                                  break
                    else:
                              print("="*60)
                              print("\tSorry your ATM pin is wrong.Please try again")
                                        
          else:
                    print("="*60)
                    print("Sorry your ATM pin is wrong. ATM pin should be 4 digits only")

          
def balance_enq():
          ch=int(input("Enter your ATM pin:"))
          acur.execute("select * from atm where pin=%d"%ch)
          if((ch>=1000)and(ch<10000)):
                    for data in acur:
                              if(data[1]==ch):
                                        print("="*60)
                                        print("Your total amount is :",data[2])
                                        break
                    else:
                              print("="*60)
                              print("Sorry you entered wrong pin.Please try again")
                              
          else:
                    print("="*60)
                    print("Sorry your ATM pin is wrong. ATM pin should be 4 digits")
def generate_pin():
          jk='1234567890987';mk='123456789012345'
          acur.execute("select AccountNumber from atm")
          ac=input("Enter your account number:")
          for d in acur:
                    if(ac==d[0]):
                              print("="*60)
                              print("Sorry already generated ATM pin by You")
                              print("**************** Thanku **************")
                              print("="*60)
                              sys.exit()
                              
          if(len(ac)>len(jk) and len(ac)<len(mk)):
                    bcur.execute("select * from bank where AccountNumber='%s'"%ac)
                    for data in bcur:
                              for info in data:
                                        if(info==ac):
                                                  #print(data[5])
                                                  mn=int(input("Enter mobile number for get OTP who is link from bank A/C:"))
                                                  if(mn==data[5]):
                                                            otp=random.randint(1000,9999)
                                                            print(otp)
                                                            eotp=int(input("Enter the OTP:"))
                                                            if(eotp==otp):
                                                                       pn=int(input("Enter the Pin for generate ATM Pin:"))
                                                                       if((pn>=1000)and(pn<10000)):
                                                                                 acur.execute("insert into atm values('%s',%d,%d,%d)"%(ac,pn,data[3],mn))
                                                                                 con.commit()
                                                                                 print("="*60)
                                                                                 print("Welcome to you Your pin Successfully Generated")
                                                                                 print("Your ATM pin is = {}".format(pn))
                                                                                 #sys.exit()
                                                                                 break
                                                                                   
                                                                       else:
                                                                                 print("="*60)
                                                                                 print("Sorry your ATM pin is wrong. ATM pin should be 4 digits")
                                                                                 break
                                                            else:
                                                                      print("="*60)
                                                                      print("Sorry your entered OTP is wrong Please try again")
                                                                      break
                                                  else:
                                                            print("="*60)
                                                            print("Sorry entered Mobile number is not link from Bank A/C ")
                                                            break
                              break
                    else:
                              print("="*60)
                              print(" Sorry,You are not Bank user.First time you open the A/C in Bank")
          else:
                    raise InvalidAccountError
                    
                                                  
                              
                    
                                                  
                                        
                                        
                           
                           
                           
                                    
                           















          

