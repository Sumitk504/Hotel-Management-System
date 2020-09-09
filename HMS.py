from tkinter import *
import time
from tkinter import ttk
import datetime



#===================Calculator Function=======================

def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def Clear():
    global operator
    operator = ''
    txt_input.set('')
    Display.insert(0,'Start Calculating...')

def Equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''

#===================================Total Function================
def TotalResult():
    #================Cost of Meal======================
    varme1 = Mealdicator.get()
    varme2 = Meal.get()
    if varme1 == 'Fried Rice':
        varme3 = (varme2*1.8)
        Cost.set(varme3)
    elif varme1 == 'Chicken':
        varme3 = (varme2*3.7)
        Cost.set(varme3)
    elif varme1 == 'Chicken Tandoori':
        varme3 = (varme2*1.2)
        Cost.set(varme3)
    elif varme1 == 'Burger':
        varme3 = (varme2*0.9)
        Cost.set(varme3)
    elif varme1 == 'Pizza':
        varme3 = (varme2*1.01)
        Cost.set(varme3)
    else:
        varme3 = (varme2 * 0.0)
        Cost.set(varme3)

    # ================Cost of Drink======================
    vardi1 = Drinkdicator.get()
    vardi2 = Drink1.get()
    if vardi1 == 'Bottled Water':
        vardi3 = (vardi2 * 1.8)
        Drinks.set(vardi3)
    elif vardi1 == 'Coca Cola':
        vardi3 = (vardi2 * 3.7)
        Drinks.set(vardi3)
    elif vardi1 == 'Pepsi':
        vardi3 = (vardi2 * 1.2)
        Drinks.set(vardi3)
    elif vardi1 == 'Sprite':
        vardi3 = (vardi2 * 0.9)
        Drinks.set(vardi3)
    elif vardi1 == 'Red Wine':
        vardi3 = (vardi2 * 1.01)
        Drinks.set(vardi3)
    else:
        vardi3 = (vardi2 * 0.0)
        Drinks.set(vardi3)

    #===================================Delivery Cost=============================
    num1 = float(Cost.get())
    num2 = float(Drinks.get())
    Delivery = (num1+num2) * 0.2

    #===================================Cost of Room==============================
    room = V.get()
    null = 0.0

    rvip = 10.0 #============Cost of VIP room=====================================
    rvip1 = Delivery/(10*0.5) #====VIP room with Delivery cost====================

    rnormal = 5.0 #=========Cost of Normal room===================================
    rnormal1 = Delivery/(5*2.5) #======Normal room with Delivery cost=============

    if room == 1:
        if chkb1.get() == 1:
            Service_Charge.set(rvip1)
            RoomCost.set(10.0)
            DevCost.set(Delivery)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(10.0)
    elif room == 2:
        if chkb1.get() == 1:
            Service_Charge.set(rnormal)
            RoomCost.set(5.0)
            DevCost.set(Delivery)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(5.0)
    elif room == 3:
        if chkb1.get() == 1:
            Service_Charge.set(null)
            RoomCost.set(null)
            DevCost.set(null)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(null)
    #==================Total Result=========================
    num3 = float(DevCost.get())
    num4 = float(RoomCost.get())
    num5 = float(Service_Charge.get())

    MyTotal = num1+num2+num3+num4+num5
    Total.set(MyTotal)
    FinalTotal = "Total = $",MyTotal

    num6 = Total.get()
    Display.delete(0,END)
    Display.insert(0,FinalTotal)

    if num6 == '0.0':
        Display.delete(0,END)
        Display.insert(0,'Please,make an order...')

#===================Currency Converter function=======================

def Convert():
    var2 = indicator.get()
    var3 = var1.get()
    if var2 == 'India':
        Display.delete(0,END)
        var4 = ('Rupee',(var3*73.00))
        Display.insert(0,var4)
    elif var2 == 'USA':
        Display.delete(0,END)
        var4 = ('USD',(var3*1.00))
        Display.insert(0,var4)
    elif var2 == 'China':
        Display.delete(0,END)
        var4 = ('Yuan',(var3*4.88))
        Display.insert(0,var4)
    elif var2 == 'Russia':
        Display.delete(0,END)
        var4 = ('RUB',(var3*75.90))
        Display.insert(0,var4)
    elif var2 == 'Japan':
        Display.delete(0,END)
        var4 = ('Yen',(var3*106.27))
        Display.insert(0,var4)
    elif var2 == 'Canada':
        Display.delete(0,END)
        var4 = ('CAD',(var3*1.31))
        Display.insert(0,var4)
    else:
        Display.delete(0,END)
        Display.insert(0,'Error:Select a country!')
        
   #============================Reset Button======================

'''def scroll():
    for line in Line:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.1)
        print('')'''

def Hotel():
    Display.delete(0,END)
    Display.insert(0,'Hotel Management Sys.')

def Powered():
    Display.delete(0, END)
    Display.insert(0, 'Powered by Python...')

def Reset():
    Display.delete(0, END)
    Display.insert(0, 'System Resetting...')
    Display.after(2000,Hotel)
    Display.after(4000,Powered)
    Display.after(6000,Rest)

def Rest():
    Clear()
    Display.delete(0,END)
    Display.insert(0,'Hello! Welcome')
    Mealdicator.set(value='Delicious Meal')
    Drinkdicator.set(value='Fresh Drink')
    indicator.set(value='Choose a Country')
    txtQtofMeal.delete(0,END)
    txtQtofMeal.insert(0,0)
    txtQtofDrink.delete(0,END)
    txtQtofDrink.insert(0,0)
    txtAmount.delete(0,END)
    txtAmount.insert(0,0)
    RoomCost.set(0.0)
    Total.set(0.0)
    Service_Charge.set(0.0)
    Drinks.set(0.0)
    Cost.set(0.0)
    chkb1.set(0)
    V.set(3)
    DevCost.set(0.0)

#==========================Clear Button========================
def ClearScreen():
    Display.delete(0,END)
    RoomCost.set('')
    Total.set('')
    Service_Charge.set('')
    Drinks.set('')
    Cost.set('')
    DevCost.set('')
 
 #============================Time================================
def tick():
    d = datetime.datetime.now()
    Today = '{:%B %d, %Y}'.format(d)

    mytime = time.strftime('%I:%M:%S%p')
    lblInfo.config(text=(mytime+' '+Today))
    lblInfo.after(200,tick)


root = Tk()
root.geometry('1366x768+0+0')
root.title('Hotel Management System')

#===================Window's partition=======================

Tops = Frame(root, width=1366, height=80, bg='blue', relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=720, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=200, height=668, relief=SUNKEN)
f2.pack(side=RIGHT)

#=======================Main Screen=========================

txt_input = StringVar(value = 'Welcome...')
Display = Entry(Tops, font='arial 89 bold', fg='white', bd=24, bg='blue', justify='right', textvariable=txt_input)
Display.grid(columnspan=4)

#======================Date and Time=========================


lblInfo = Label(f2,font=('arial',19,'bold'),fg='dark blue',bd=5,anchor=W)
lblInfo.grid(row=1,column=0,columnspan=4)
tick()

#=======================Calculator===========================

#========================Row 1===============================
operator = ''

btn7 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='7', command=lambda:btn(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='8', command=lambda:btn(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='9', command=lambda:btn(9)).grid(row=2, column=2)
btnC = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='C', command=Clear).grid(row=2, column=3)

#========================Row 2===============================

btn4 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='4', command=lambda:btn(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='5', command=lambda:btn(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='6', command=lambda:btn(6)).grid(row=3, column=2)
btnplus = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', bg='orange', text='+', command=lambda:btn('+')).grid(row=3, column=3)

#========================Row 3===============================

btn1 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='1', command=lambda:btn(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='2', command=lambda:btn(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='3', command=lambda:btn(3)).grid(row=4, column=2)
btnminus = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', bg='orange', text='-', command=lambda:btn('-')).grid(row=4, column=3)

#========================Row 4===============================

btn0 = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', text='0', command=lambda:btn(0)).grid(row=5, column=0)
btndot = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', bg='orange', text='.', command=lambda:btn('.')).grid(row=5, column=1)
btndivision = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', bg='orange', text='/', command=lambda:btn('/')).grid(row=5, column=2)
btnmultiply = Button(f2, padx=15, pady=2, bd=8,font='arial 30 bold', bg='orange', text='x', command=lambda:btn('*')).grid(row=5, column=3)

#========================Row 5===============================

btnequals = Button(f2, padx=64, pady=2, bd=8, font='arial 30 bold', bg='green', text='=', command=Equal).grid(row=6, column=0, columnspan=2)
btnopenbrakcet = Button(f2, padx=19, bd=8, pady=2, font='arial 30 bold', bg='orange', text='(', command=lambda:btn('(')).grid(row=6, column=2)
btnclosebracket = Button(f2, padx=23, bd=8, pady=2, font='arial 30 bold', bg='orange', text=')', command=lambda:btn(')')).grid(row=6, column=3)

#=======================Choose Meal===========================

Meal = IntVar()
Mealdicator = StringVar(value='Dilicious Meal')

lblMeal = Label(f1, font='arial 16 bold', text='Choose Meal', bd=10, anchor=W)
lblMeal.grid(row=0, column=0)
txtMeal = ttk.Combobox(f1, font='arial 16 bold', textvariable=Mealdicator)
txtMeal['values'] = ('Fried Rice', 'Chicken', 'Chicken Tandoori', 'Burger', 'Pizza')
txtMeal.grid(row=0, column=1)

lblQtofMeal = Label(f1, font='arial 16 bold', text='Qty. of Meal', bd=10, anchor=W)
lblQtofMeal.grid(row=1, column=0)
txtQtofMeal= Entry(f1, font='arial 16 bold', textvariable=Meal, bd=10, insertwidth=4, bg='white', justify='right')
txtQtofMeal.grid(row=1, column=1)

#=======================Choose Drinks===========================

Drink1 = IntVar()
Drinkdicator = StringVar(value='Fresh Drinks')

lblDrink = Label(f1, font='arial 16 bold', text='Choose Drink', bd=10, anchor=W)
lblDrink.grid(row=2, column=0)
txtDrink = ttk.Combobox(f1, font='arial 16 bold', textvariable=Drinkdicator)
txtDrink['values'] = ('Bottled Water', 'Coca Cola', 'Pepsi', 'Sprite', 'Red Wine')
txtDrink.grid(row=2, column=1)

lblQtofDrink = Label(f1, font='arial 16 bold', text='Qty. of Drink', bd=10, anchor=W)
lblQtofDrink.grid(row=3, column=0)
txtQtofDrink = Entry(f1, font='arial 16 bold', textvariable=Drink1, bd=10, insertwidth=4, bg='white', justify='right')
txtQtofDrink.grid(row=3, column=1)

#=======================Order Delivery==========================
chkb1 = IntVar()

lblHomeDev = Label(f1, font='arial 16 bold', text='Order Delivery', bd=10, anchor=W)
lblHomeDev.grid(row=4, column=0)
check1 = Checkbutton(f1, font='arial 16 bold', text='Yes', variable=chkb1)
check1.grid(row=4, column=1)

#=======================Book a Room==========================
V = IntVar()
V.set(3)

lblRoom = Label(f1, font='arial 16 bold', text='Book a Room', bd=10, anchor=W)
lblRoom.grid(row=5, column=0)
MyRadios = Radiobutton(f1, font='arial 16 bold', text='VIP', variable=V, value='1')
MyRadios .grid(row=5, column=1)
MyRadios = Radiobutton(f1, font='arial 16 bold', text='Normal', variable=V, value='2')
MyRadios .grid(row=5, column=1, sticky=W)
MyRadios = Radiobutton(f1, font='arial 16 bold', text='No', variable=V, value='3')
MyRadios .grid(row=5, column=1, sticky=E)

#=======================Cost Display Screen==========================
Cost = StringVar()
lblMeall = Label(f1, font='arial 16 bold', text='Cost of Meal($)', bd=16, anchor=W)
lblMeall.grid(row=0, column=2)
txtMeall = Entry(f1, font='arial 16 bold', textvariable=Cost, bd=10, fg='white', insertwidth=4, bg='blue', justify='right')
txtMeall.grid(row=0, column=3)

Drinks = StringVar()
lblDrink1 = Label(f1, font='arial 16 bold', text='Cost of Drinks($)', bd=16, anchor=W)
lblDrink1.grid(row=1, column=2)
txtDrink1 = Entry(f1, font='arial 16 bold', textvariable=Drinks, bd=10, fg='white', insertwidth=4, bg='blue', justify='right')
txtDrink1.grid(row=1, column=3)

DevCost = StringVar()
lblDev = Label(f1, font='arial 16 bold', text='Delivery Cost($)', bd=16, anchor=W)
lblDev.grid(row=2, column=2)
txtDev = Entry(f1, font='arial 16 bold', textvariable=DevCost, bd=10, fg='white', insertwidth=4, bg='blue', justify='right')
txtDev.grid(row=2, column=3)

RoomCost = StringVar()
lblRoom = Label(f1, font='arial 16 bold', text='Cost of Room($)', bd=16, anchor=W)
lblRoom.grid(row=3, column=2)
txtRoom = Entry(f1, font='arial 16 bold', textvariable=DevCost, bd=10, fg='white', insertwidth=4, bg='blue', justify='right')
txtRoom.grid(row=3, column=3)

Service_Charge = StringVar()
lblSer_Ch = Label(f1, font='arial 16 bold', text='Service Charge($)', bd=16, anchor=W)
lblSer_Ch.grid(row=4, column=2)
txtSer_Ch = Entry(f1, font='arial 16 bold', textvariable=Service_Charge, bd=10, fg='white', insertwidth=4, bg='blue', justify='right')
txtSer_Ch.grid(row=4, column=3)

Total = StringVar()
lblTotal = Label(f1, font='arial 16 bold', text='Total Cost($)', bd=16, anchor=W)
lblTotal.grid(row=5, column=2)
txtTotal = Entry(f1, font='arial 16 bold', textvariable=Total, bd=10, fg='white', insertwidth=4, bg='blue', justify='right')
txtTotal.grid(row=5, column=3)

#=======================Currency Converter==========================
var1 = IntVar()
indicator = StringVar(value='Choose Country')

lblCurr_Con = Label(f1, font='arial 16 bold', fg='Yellow', bg='black', padx=60, text='Currency Converter')
lblCurr_Con.grid(row=6, column=0, columnspan=4)

lblCountry = Label(f1, font='arial 16 bold', text='Nationality', bd=10, anchor=W)
lblCountry.grid(row=7, column=0)
txtCountry = ttk.Combobox(f1, font='arial 16 bold', textvariable=indicator)
txtCountry['values'] = ('India','USA','Russia','Canada','China','Japan')
txtCountry.grid(row=7, column=1)

lblAmount = Label(f1, font='arial 16 bold', text='Amount($)', bd=16, anchor=W)
lblAmount.grid(row=7, column=2)
txtAmount = Entry(f1, font='arial 16 bold', textvariable=var1, bd=10, insertwidth=4, bg='white', justify='right')
txtAmount.grid(row=7, column=3)

#=======================Control Button==========================
btnConvert = Button(f1, font='arial 16 bold', padx=5, pady=3, bd=13,fg='yellow', width=12, text='Convert', bg='black', command=Convert)
btnConvert.grid(row=8, column=0)

btnTotal = Button(f1,padx=3,pady=3,bd=13,fg='yellow',font=('arial',16,'bold'),width=12,text='Total',bg='black', command=TotalResult)
btnTotal.grid(row=8,column=1)

btnReset = Button(f1,padx=5,pady=3,bd=13,fg='yellow',font=('arial',16,'bold'),width=12,text='Reset',bg='black', command=Reset)
btnReset.grid(row=8,column=2)

btnScreen = Button(f1,padx=5,pady=3,bd=13,fg='yellow',font=('arial',16,'bold'),width=12,text='Clear',bg='black', command=ClearScreen)
btnScreen.grid(row=8,column=3)

root.mainloop()