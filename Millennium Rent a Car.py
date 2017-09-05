import pickle,os,time


def payment(cr,c): 
    print '''**Days are counted from 12:00 AM to 12:00 AM. Failure to return
your car by that time will result in being charged for an additional
day**'''
    global t
    t=input('Enter number of days: ')
    global prc
    prc = t*cr.bprice
    print
    print'''This is the final booking:'''
    print "Car to be rented - ", cr.name
    print "Number of days", t
    print "Total cost", prc
    print
    ch6=raw_input('Enter y to pay: ')
    if ch6=='y':
        c.cpayment()
    elif ch6=='0':
        print a
        rent()


     
class customer: #Class to hold Customer info
    n = 1
    name = ''
    age  = 0
    phno = 0
    rentals=[]
    def enter_details(self):
        a='------------------------------------------'
        print
        print "Enter details  - "
        self.name = raw_input("Enter name: ")
        if self.name=='0':
            print a
            rent()
        self.phno = int(raw_input("Enter phone number (05...): "))
        if self.phno==0:
            print a
            rent()
        self.age = input("Enter age: ")
        if self.age==0:
            print a
            rent()
        self.__credno = input('Enter credit card no: ')
        if self.__credno==0:
            print a
            rent()
        self.__pin = input("Enter pin: ")
        if self.__pin==0:
            print a
            rent()
    def cpayment(self):
        p=input('Enter Pin Number: ')
        if p==self.__pin:
            print 'Pin verified'
            time.sleep(2)
            print 'Processing...'
            time.sleep(4)
            print 'Payment of ',prc,'made to card number',self.__credno
        else:
            print 'Error, incorrect pin number, try again.'
            self.payment()
        p=0
    
    def display(self):
        print
        print 'DETAILS:-'
        print 'Name: ',self.name
        print 'Age: ',self.age
        print 'Phone Number: ',self.phno
        print 'Past Rentals: ',self.rentals
    def Det_list_create(self,cr):
        #serial no + cr.det + time + incomp
        l = [[customer.n, self.phno, cr.det, t]]
        print 'l', l
        print self.rentals
        self.rentals += l
        print self.rentals
    



class ecocars: #Class to hold Car info
    def __init__(self, name, year, colour, nplate, bprice, det=''):
        self.name = name
        self.year = year
        self.colour = colour
        self.nplate = nplate
        self.bprice = bprice
        self.det = det
        self.dets()
    def display(self):
        print 'Name: ',self.name
        print 'Year: ',self.year
        print 'Colour: ',self.colour
        print 'Number Plate: ',self.nplate
        print 'Base Price: ',self.bprice
        print 'Total price = Days x Base Price'
    def dets(self):
        self.det = self.name + '-' + str(self.nplate)    




class luxcars: #Class to hold Car info
    def __init__(self, name, year, colour, nplate, bprice, det=''):
        self.name = name
        self.year = year
        self.colour = colour
        self.nplate = nplate
        self.bprice = bprice
        self.det = det
        self.dets()
    def display(self):
        print 'Name: ',self.name
        print 'Year: ',self.year
        print 'Colour: ',self.colour
        print 'Number Plate: ',self.nplate
        print 'Base Price: ',self.bprice
        print 'Total price = Days x Base Price'
    def dets(self):
        self.det = self.name + '-' + str(self.nplate) 




class excars: #Class to hold Car info
    def __init__(self, name, year, colour, nplate, bprice, det=''):
        self.name = name
        self.year = year
        self.colour = colour
        self.nplate = nplate
        self.bprice = bprice
        self.det = det
        self.dets()
    def display(self):
        print 'Name: ',self.name
        print 'Year: ',self.year
        print 'Colour: ',self.colour
        print 'Number Plate: ',self.nplate
        print 'Base Price: ',self.bprice
        print 'Total price = Days x Base Price'
    def dets(self):
        self.det = self.name + '-' + str(self.nplate) 

def rent(): #Function holding the main program, neccessary for looping back.
    #Initiating Car objects
    c1 = ecocars('Nissan Sunny', '2017', 'Black', 12053, 160, 100)
    c2 = ecocars('Toyota Yaris', '2017', 'Yellow', 15269, 140, 90)
    c3 = ecocars('Ford Fiesta', '2017', 'Green', 02563, 150, 100)
    c4 = ecocars('Chevorlet Malibu', '2017', 'Red', 45802, 180, 120)
    lc1 = luxcars('Mercedez E Class', '2015', 'Maroon', 52639, 300, 250)
    lc2 = luxcars('BMW 5-series', '2016', 'Silver', 4589, 400, 350)
    lc3 = luxcars('Audi A5', '2017', 'Gold', 78596, 350, 300)
    lc4 = luxcars('Chevorlet Camaro', '2014', 'Yellow', 2365, 300, 250)
    ec1 = excars('Tesla Roadster', '2005', 'Blue', 125, 1000, 800)
    ec2 = excars('Lamborghini Huracan', '2013', 'Lime Green', 2563, 800, 600)
    ec3 = excars('Ferrari California', '2012', 'Red', 201, 1500, 1000)
    ec4 = excars('McLaren 250C', '2011', 'Orange', 264, 1000, 800)
    a='------------------------------------------'
    customers = open('customers.txt', 'ab+')
    print '''MAIN MENU
===CHOOSE OPTION===
1. New Customer
2. Existing customer
**To exit to main menu at anytime, enter 0**
    '''
    try:   
        ch = input("Enter choice: ")
            
        if ch == 1:
            c = customer()
            c.enter_details()
            c.display()
            print
            print '''CHOOSE OPTION
        1. New rental
        '''
            ch2 = input("Enter choice: ")
            if ch2 == 1:
                print
                print '''CHOOSE CLASS
        1. Economy
        2. Luxury
        3. Exotic
        ''' 
                ch3=input('Enter choice: ')
                print
                if ch3==1:
                    c1.display()
                    print
                    c2.display()
                    print
                    c3.display()
                    print
                    c4.display()
                    print
                    print '''CHOOSE CAR'''
                    ch4 = int(raw_input('Enter number on list: '))
                    if ch4==1:
                        cr=c1
                    elif ch4==2:
                        cr=c2
                    elif ch4==3:
                        cr=c3
                    elif ch4==4:
                        cr=c4
                    elif ch==0:
                        print a
                        rent()
                if ch3==2:
                    lc1.display()
                    print
                    lc2.display()
                    print
                    lc3.display()
                    print
                    lc4.display()
                    print
                    print '''CHOOSE CAR'''
                    ch4 = int(raw_input('Enter number on list: '))
                    if ch4==1:
                        cr=lc1
                    elif ch4==2:
                        cr=lc2
                    elif ch4==3:
                        cr=lc3
                    elif ch4==4:
                        cr=lc4
                    elif ch==0:
                        print a
                        rent()
                if ch3==3:
                    ec1.display()
                    print
                    ec2.display()
                    print
                    ec3.display()
                    print
                    ec4.display()
                    print
                    print '''CHOOSE CAR'''
                    ch4 = int(raw_input('Enter number on list: '))
                    if ch4==1:
                        cr=ec1
                    elif ch4==2:
                        cr=ec2
                    elif ch4==3:
                        cr=ec3
                    elif ch4==4:
                        cr=ec4
                    elif ch==0:
                        print a
                        rent()
                elif ch3==0:
                    print a
                    rent()
                print
                payment(cr,c)
                c.rentals=[]
                c.Det_list_create(cr)
                pickle.dump(c,customers)
                customer.n+=1
                customers.close()
                customers = open('customers.txt', 'ab+')
                print a
                rent()
                           
                    
        elif ch == 2:
            customers.close()
            customers=open('customers.txt','rb')
            tphno = int(raw_input("Enter phone number (05...): "))
            customers.seek(0)
            c=customer()
            try:
                while True:
                    c = pickle.load(customers)
                    if c.phno == tphno:
                        break
            except EOFError:
                print "Customer doesn't exist in our database. Create an account"
                print a
                rent()
            customers.close()
                
                    
                    
            c.display()
            print
            print '''CHOOSE OPTION
        1. Create new rental
        2. Edit details
        3. View History'''
             
            
            ch8 = input("Enter choice: ")
            if ch8 == 1:
                print
                print '''CHOOSE CLASS
            1. Economy
            2. Luxury
            3. Exotic
            ''' 
                ch9=input('Enter choice: ')
                print
                if ch9==1:
                    c1.display()
                    print
                    c2.display()
                    print
                    c3.display()
                    print
                    c4.display()
                    print
                    print '''CHOOSE CAR'''
                    ch10 = int(raw_input('Enter number on list: '))
                    if ch10==1:
                        cr=c1
                    elif ch10==2:
                        cr=c2
                    elif ch10==3:
                        cr=c3
                    elif ch10==4:
                        cr=c4
                    elif ch10==0:
                        print a
                        rent()
                if ch9==2:
                    lc1.display()
                    print
                    lc2.display()
                    print
                    lc3.display()
                    print
                    lc4.display()
                    print
                    print '''CHOOSE CAR'''
                    ch11 = int(raw_input('Enter number on list: '))
                    if ch11==1:
                        cr=lc1
                    elif ch11==2:
                        cr=lc2
                    elif ch11==3:
                        cr=lc3
                    elif ch11==4:
                        cr=lc4
                    elif ch11==0:
                        print a
                        rent()      
                if ch9==3:
                    ec1.display()
                    print
                    ec2.display()
                    print
                    ec3.display()
                    print
                    ec4.display()
                    print
                    print '''CHOOSE CAR'''
                    ch12 = int(raw_input('Enter number on list: '))
                    if ch12==1:
                        cr=ec1
                    elif ch12==2:
                        cr=ec2
                    elif ch12==3:
                        cr=ec3
                    elif ch12==4:
                        cr=ec4
                    elif ch12==0:
                        print a
                        rent()
                elif ch9==0:
                    print a
                    rent()
                f2=open("Dummy.txt",'ab')
                with open('customers.txt','ab+') as customers :
                    try:
                        while True:
                            c1=pickle.load(customers)
                            if c1.phno==tphno:
                                pass
                            else:
                                pickle.dump(c1,f2)
                    except EOFError:
                        pass
                f2.close()
                os.remove('customers.txt')
                os.rename('Dummy.txt','customers.txt')
                customers = open('customers.txt', 'ab+')
                payment(cr,c)
                c.Det_list_create(cr)
                pickle.dump(c,customers)
                customers.close()
                customer.n+=1
                print a
                rent()
                
            
            elif ch8 == 2:
                customers.close()
                f2 = open('dummy.txt', 'ab+')
                with open('customers.txt','ab+') as customers:
                    try:
                        customers.seek(0)
                        check = int(raw_input('Enter your phone number - '))
                        while True:
                            c = pickle.load(customers)
                            if c.phno == check:
                                c.name = raw_input('Enter new name - ')
                                c.age = int(raw_input('Enter new age - '))
                                c.phno = int(raw_input('Enter new phone number - '))
                                pickle.dump(c, f2)
                            else:
                                pickle.dump(c, f2)
                    except EOFError:
                        pass
                f2.close()
                os.remove('customers.txt')
                os.rename('dummy.txt', 'customers.txt')
                print a
                rent()
            elif ch8 == 'lol':
                customers.seek(0)
                check = int(raw_input('Enter your phone number - '))
                try:
                    print '[Sr.No., Phone Number, Car Details, Days Rented]'
                    while True:
                        c = pickle.load(customers)
                        if(c.phno == tphno):
                            print
                            print 'Rental History:-'
                            for b in c.rentals:
                                print b
                            break
            
                except EOFError:
                    print('You do not have an account yet')
                print a
                rent()
            elif ch8==0:
                print a
                rent()
        elif ch==0:
            print a
            rent()
    except ValueError:
        print 'Error: Incorrect input; returning to Main Menu.'
        print
        print a
        rent()
    except NameError:
        print 'Error: Incorrect input; returning to Main Menu.'
        print
        print a
        rent()
        
rent()
