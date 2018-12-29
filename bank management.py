import pickle
import math

class account():
    def __init__(self):
        self.cname=None
        self.acno=0L
        self.b=0.0
    def getdata(self):
        self.cname=raw_input("Enter customer name : ")
        if self.cname.isalpha()==False:
            raise ValueError
        self.acno=int(raw_input("Enter account number : "))
        self.b=float(raw_input("Enter opening balance : "))
    def showdata(self):
        print "The customer name is ",self.cname
        print "The account number is ",self.acno
        print "The opening balance is ",self.b

class saving(account):
    def __init__(self):
        print "No check book facilities available"
        account.__init__(self)
        self.rate=0.0
        self.time=0
        self.ci=0.0
    def getdata(self):
        account.getdata(self)
        self.time=int(raw_input("Enter time period : "))
        self.rate=float(raw_input("Enter rate of interest : "))
        self.ci=self.compound_interest()
    def showdata(self):
        account.showdata(self)
        print "The rate of interest is ",self.rate
        print "The time period of interest is ",self.time
        print "The compound interst is ",self.ci
    def deposit(self):
        a=float(raw_input("Enter amount to be deposited : "))
        self.b+=a
        print "The amount deposited successfully"
        print "The new amount is ",self.b
    def withdraw(self):
        a=float(raw_input("Enter amount to be withdrawn : "))
        if self.b<a:
            print "insufficient balance in the account "
        else:
            self.b-=a
            print "amount withdrawn successfully"
    def compound_interest(self):
        self.ci=self.b+math.pow(1+self.rate/100,self.time)
        self.b+=self.ci
        return self.ci

class current(account):
    def __init__(self):
        print "No interest will be given "
        print "Cheque book facility available"
        account.__init__(self)
        self.min=1000
    def deposit(self):
        a=float(raw_input("Enter amount to be deposited : "))
        self.ob+=a
        print "The amount deposited successfully"
        print "The new amount is ",self.ob
    def withdrawal(self):
        a=float(raw_input("Enter amount to be withdrawn : "))
        if self.b<a:
            print "insufficient balance in the account "
        else:
            self.b-=a
            print "amount withdrawn successfully"
    def check(self):
        if self.b<self.min:
            print "The balance of account is less than minimum balance of Rs.1000"
            print "A penalty of Rs.100 is imposed "
            self.b-=100
            print "The balance left in the account is ",self.b

def fixed(account):
    def __init__(self):
        print "Withdrawal is allowed only after half of the time period has passed"
        account.__init__(self)
        self.t=0
    def getdata(self):
        account.getdata()
        self.t=int(raw_input("Enter time period (1 or 3 or 5) : "))
    def showdata(self):
        account.showdata()
        print "The time period is ",self.t
    def withdrawal(self):
        t=int(raw_input("Enter the time period which has passed : "))
        if self.t<=t:
            print "withdrawal is allowed"
            print "Withdrawal successful"
        
    
def create():
    while True:
        print "Enter The type of account to be created\n "
        print "1. For Savings account"
        print "2. For Current account"
        print "3. For fixed deposit"
        print "0. To Return To The Main menu\n "
        c=raw_input("Enter your choice : ")
        f1=open("account.log","ab")
        if c=="0":
            f1.close()
            print
            break
        elif c=="1":
            a1=saving()
            while True:
                try:
                    a1.getdata()
                    break
                except ValueError:
                    print "Invalid input : Retry... "
            a1.showdata()
            pickle.dump(a1,f1)
            print "Account created successfully\n"
        elif c=="2":
            a1=current()
            while True:
                try:
                    a1.getdata()
                    break
                except ValueError:
                    print "Invalid input : Retry... "
            a1.showdata()
            pickle.dump(a1,f1)
            print "Account created successfully"
        elif c=="3":
             a1=fixed()
             while True:
                try:
                    a1.getdata()
                    break
                except ValueError:
                    print "Invalid input : Retry... "
             a1.showdata()
             pickle.dump(a1,f1)
             print "Account created successfully"
        else:
            print "Invalid choice : Enter a valid \"OPTION\" : 0.....3 : returning.... \n"


def dep():
    f1=open("account.log","ab+")
    while True:
        try:
            n=raw_input("Enter name of customer : ")
            if n.isalpha==False:
                raise ValueError
            a=int(raw_input("Enter account number : "))
            k=float(raw_input("Enter the amount to be deposited : "))
            break
        except ValueError:
            print "Invalid input : Enter digits "
    while True:
        try:
            a1=pickle.load(f1)
            if a1.cname==n and a1.ano==a:
                a1.deposit()
                break
        except EOFError:
            f1.close()
            print "Account Not Found"
            
def withdraw():
    f1=open("account.log","ab+")
    while True:
        try:
            n=raw_input("Enter name of customer : ")
            if n.isalpha==False:
                raise ValueError
            a=int(raw_input("Enter account number : "))
            k=float(raw_input("Enter the amount to be deposited : "))
            break
        except ValueError:
            print "Invalid input : Enter digits "
    while True:
        try:
            a1=pickle.load(f1)
            if a1.cname==n and a1.ano==a:
                a1.withdrawal()
                break
        except EOFError:
            f1.close()
            print "Account Not Found"

def view():
    while True:
        print "Choose an option\n"
        print "1. To view a specific account details"
        print "2. To filter accounts of particular alphabet"
        print "3. To view all the savings account"
        print "4. To view all the current accounts"
        print "5. To view all the fixed deposits"
        print "6. To view all the accounts"
        print "0. To return to the main menu\n"
        c=raw_input("Enter your choice : ")
        if c=="0":
            print
            break
        elif c=="1":
            f1=open("account.log","rb")
            while True:
                try:
                    a=int(raw_input("Enter account number"))
                    break
                except ValueError:
                    print "invalid input: Enter a valid input: Retry..."
            try:
                while True:
                    a1=pickle.load(f1)
                    if a1.cname==a:
                        a1.showdata()
                        break
            except EOFError:
                f1.close()
                print "Record not found"
        elif c=="2":
            while True:
                try:
                    k=raw_input("Enter an alphabet to display all the accounts starting with that alphabet : ") 
                    if k.isalpha==False:
                        raise ValueError
                    break
                except ValueError:
                    print "invalid input: Enter a valid input: Retry..."
            while True:
                try:
                    a1=pickle.load(f1)
                    if a1.cname[0]==k:
                        a1.showdata()
                        print
                except EOFError:
                    f1.close()
        elif c=="3":
            f1=open("account.log","rb")
            try:
                while True:
                    a1=pickle.load(f1)
                    if a1.__class__.__name__=="saving":
                        a1.showdata()
            except EOFError:
                f1.close()
        elif c=="4":
            f1=open("account.log","rb")
            try:
                while True:
                    a1=pickle.load(f1)
                    if a1.__class__.__name__=="current":
                        a1.showdata()
            except EOFError:
                f1.close()
        elif c=="5":
            f1=open("account.log","rb")
            try:
                while True:
                    a1=pickle.load(f1)
                    if a1.__class__.__name__=="fixed":
                        a1.showdata()
            except EOFError:
                f1.close()
        elif c=="6":
            f1=open("account.log","rb")
            try:
                while True:
                    a1=pickle.load(f1)
                    a1.showdata()
            except EOFError:
                f1.close()

        else:
            print "Invalid choice : Enter a valid \"OPTION\" : 0.....3 : returning.... \n"    
    
            
print "                             Welcome to the \"BANK MANAGEMENT\" System\n"

while True:
    print "choose an option to continue\n "
    print "1. To create accounts"
    print "2. To deposit amount"
    print "3. To withdraw amount"
    print "4. To view account details"
    print "0. To Exit"
    ch=raw_input("Enter an option of your choice : ")
    if ch=="0":
        break
    elif ch=="1":
        print
        create()
    elif ch=="2":
        print
        dep()
    elif ch=="3":
        print
        withdraw()
    elif ch=="4":
        print
        view()
    else:
        print "Invalid choice : Enter a valid \"OPTION\" : 0.....3 : returning.... \n"
