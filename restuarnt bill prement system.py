from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Bill Payment Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text=" \"NAME OF THE RESTAURANT\" ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
def CoustomerName():
    if (CoustomerName.get()==""):
        CoCoustomerName=0
    else:
        CoustomerName=(CoustomerName.get())
def CoustomerMobileNumber():
    if (CoustomerMobileNumber.get()==""):
        CoCoustomerMobileNumber=0
    else:
        CoustomerMobileNumber=int(CoustomerMobileNumber.get())
def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Kacci.get()==""):
        CoKacci=0
    else:
        CoKacci=float(Kacci.get())


    
    if (Teheri.get()==""):
        CoTeheri=0
    else:
        CoTeheri=float(Teheri.get())



    if (Berger.get()==""):
        CoBerger=0
    else:
        CoBerger=float(Berger.get())



    if (Biriyani.get()==""):
        CoBiriyani=0
    else:
        CoBiriyani=float(Biriyani.get())

        
    if (Kabab.get()==""):
        CoKabab=0
    else:
        CoKabab=float(Kabab.get())

     
    if (Drinks.get()==""):
        CoDrinks=0
    else:
        CoDrinks=float(Drinks.get())

                   
    CostofKacci =CoKacci * 250
    CostofDrinks=CoDrinks * 20
    CostofTeheri = CoTeheri* 150
    CostofBerger = CoBerger * 99
    CostBiriyani = CoBiriyani* 135
    CostKabab=CoKabab * 420

    CostofMeal= "Taka", str('%.2f' % (CostofKacci+CostofDrinks+CostofTeheri+CostofBerger+CostBiriyani+CostKabab))

    PayTax=((CostofKacci+CostofDrinks+CostofTeheri+CostofBerger+CostBiriyani+CostKabab) * 0.2)

    TotalCost=(CostofKacci+CostofDrinks+CostofTeheri+CostofBerger+CostBiriyani+CostKabab)
 
    Ser_Charge= ((CostofKacci+CostofDrinks+CostofTeheri+CostofBerger+CostBiriyani+CostKabab)/99)

    Service = "Taka", str ('%.2f' % Ser_Charge)

    OverAllCost ="Taka", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Taka", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Kacci.set("")
    Teheri.set("")
    Berger.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Biriyani.set("")
    Kabab.set("")
    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Kacci=StringVar()
Teheri=StringVar()
Berger=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Biriyani=StringVar()
Kabab=StringVar()

lblCustomerName= Label(f1, font=('arial', 16, 'bold'),text="Name",bd=16,anchor="w")
lblCustomerName.grid(row=0, column=0)
txtCustomerName=Entry(f1, font=('arial',16,'bold'),textvariable=CoustomerName,bd=10,insertwidth=4,bg="White",justify='right')
txtCustomerName.grid(row=0,column=1)

lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=1, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="White",justify='right')
txtReference.grid(row=1,column=1)

lblKacci= Label(f1, font=('arial', 16, 'bold'),text="Kacci",bd=16,anchor="w")
lblKacci.grid(row=2, column=0)
txtKacci=Entry(f1, font=('arial',16,'bold'),textvariable=Kacci,bd=10,insertwidth=4,bg="White",justify='right')
txtKacci.grid(row=2,column=1)


lblTeheri= Label(f1, font=('arial', 16, 'bold'),text="Teheri",bd=16,anchor="w")
lblTeheri.grid(row=3, column=0)
txtTeheri=Entry(f1, font=('arial',16,'bold'),textvariable=Teheri,bd=10,insertwidth=4,bg="White",justify='right')
txtTeheri.grid(row=3,column=1)


lblBerger= Label(f1, font=('arial', 16, 'bold'),text="Berger",bd=16,anchor="w")
lblBerger.grid(row=4, column=0)
txtBerger=Entry(f1, font=('arial',16,'bold'),textvariable=Berger,bd=10,insertwidth=4,bg="White",justify='right')
txtBerger.grid(row=4,column=1)

lblBiriyani= Label(f1, font=('arial', 16, 'bold'),text="Biriyani",bd=16,anchor="w")
lblBiriyani.grid(row=5, column=0)
txtBiriyani=Entry(f1, font=('arial',16,'bold'),textvariable=Biriyani,bd=10,insertwidth=4,bg="White",justify='right')
txtBiriyani.grid(row=5,column=1)

lblKabab= Label(f1, font=('arial', 16, 'bold'),text="Kabab",bd=16,anchor="w")
lblKabab.grid(row=6, column=0)
txtKabab=Entry(f1, font=('arial',16,'bold'),textvariable=Kabab,bd=10,insertwidth=4,bg="White",justify='right')
txtKabab.grid(row=6,column=1)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================
lblCoustomerMobileNumber= Label(f1, font=('arial', 16, 'bold'),text="Mobile Number",bd=16,anchor="w")
lblCoustomerMobileNumber.grid(row=0, column=2)
txtCoustomerMobileNumber=Entry(f1, font=('arial',16,'bold'),textvariable=CoustomerMobileNumber,bd=10,insertwidth=4,bg="White",justify='right')
txtCoustomerMobileNumber.grid(row=0,column=3)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=1, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="White",justify='right')
txtDrinks.grid(row=1,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=2, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="White",justify='right')
txtCost.grid(row=2,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=3, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="White",justify='right')
txtService.grid(row=3,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="Govt. Tax",bd=16,anchor="w")
lblStateTax.grid(row=4, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="White",justify='right')
txtStateTax.grid(row=4,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=5, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="White",justify='right')
txtSubTotal.grid(row=5,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=6, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="White",justify='right')
txtTotalCost.grid(row=6,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)


root.mainloop()


