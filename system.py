from tkinter import *
import tkinter as tk
import random
import time
from  tkinter import ttk


root =tk.Tk()
root.geometry()
root.title("PHARMACY MANAGEMENT SYSTEM")

# background_Image =tk(file = 'landscape.jpg')
# background_Label = tk.Label(root, image_names('background_Image'))
# background_Label.pack()

text_Input = StringVar()
operator =""

Tops = Frame(root, width = 4000,height=2000, relief = SUNKEN)
Tops.pack(side=TOP)

x1 = Frame(root, width = 2800,height= 1200, padx = 10, relief = SUNKEN)
x1.pack(side=LEFT)

x2 = Frame(root, width = 1200,height= 800,padx=10,  relief = SUNKEN)
x2.pack(side=RIGHT)

#============================= TIME  ========================================================================
localTime = time.asctime(time.localtime(time.time()))

#=========================== INFORMATION ====================================================================
ib1Info = Label(Tops, font=("segoe UI", 30, 'bold'), text = "PHARMACY MANAGEMENT SYSTEM", fg ="black", bg = 'white', bd =3, anchor='w', relief = RAISED)
ib1Info.grid(row=0,column = 0)

ib1Info = Label(Tops, font=("segoe UI", 20, 'bold'), text = localTime, fg ="dark blue", bd =10, anchor='w')
ib1Info.grid(row=1,column = 0)

#============================ CALCULATOR ============================================================================

def btnClick(numbers):
    global operator
    operator = operator+ str(numbers)
    text_Input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualTo():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    X =random.randint(10908,500876)
    randomRef = str(X)
    rand.set(randomRef)

    CoPain = float(pain.get())
    CoTonic = float(tonic.get())
    CoMala = float(mala.get())
    CoOint = float(oint.get())
    CoHerbal = float(herbal.get())
    CoOther = float(other.get())
    CoCough = float(cough.get())
    CoUlcer = float(ulcer.get())
    CoAnti = float(anti.get())
    CoOphthmal = float(ophthmal.get())
    CoContra = float(contra.get())

    CostofPain = CoPain*1.00
    CostofTonic = CoTonic * 15.00
    CostofOint = CoOint * 5.00
    CostofMala = CoMala * 12.00
    CostofHerbal = CoHerbal * 10.00
    CostofOther = CoOther * 13.00
    CostofCough = CoCough * 7.00
    CostofUlcer = CoUlcer * 15.00
    CostofAnti = CoAnti * 11.00
    CostofOphthmal = CoOphthmal * 12.00
    CostofContra = CoContra * 5

    CostOfMedicine = "C", str('%.2f' %( CostofPain +  CostofTonic + CostofOint + CostofMala + CostofHerbal +  CostofOther
                                        + CostofCough +  CostofUlcer + CostofAnti +  CostofOphthmal + CostofContra ))

    PayTax = (( CostofPain +  CostofTonic + CostofOint + CostofMala + CostofHerbal +  CostofOther
                                        + CostofCough +  CostofUlcer + CostofAnti +  CostofOphthmal + CostofContra  ) * 0.01)

    TotalCost = ( CostofPain +  CostofTonic + CostofOint + CostofMala + CostofHerbal +  CostofOther
                                        + CostofCough +  CostofUlcer + CostofAnti +  CostofOphthmal + CostofContra  )

    OverAllCost = "C", str('%.2f' %(    PayTax + TotalCost)
                           )

    cost_charge.set(CostOfMedicine)
    tax_charge.set(PayTax)
    stotal.set(CostOfMedicine)
    total.set(OverAllCost)


def qExit():
    root.destroy()

def Reset():
    rand.set("")
    pain.set("")
    tonic.set("")
    mala.set("")
    oint.set("")
    cough.set("")
    herbal.set("")
    other.set("")
    ulcer.set("")
    cost_charge.set("")
    tax_charge.set("")
    stotal.set("")
    total.set("")
    ophthmal.set("")
    anti.set("")
    contra.set("")



textDisplay = Entry(x2, font=('segoe UI', 15, 'bold'), textvariable=text_Input, bd=20, insertwidth=2,
                    bg="#c2eed8", justify='right')
textDisplay.grid(columnspan=4)

btn7 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="7", bg='#c2eed8', command=lambda: btnClick(7)).grid(row=2, column =0)

btn8 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="8", bg='#c2eed8', command=lambda: btnClick(8)).grid(row=2, column =1)

btn9 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="9", bg='#c2eed8', command=lambda: btnClick(9)).grid(row=2, column =2)

Addition=Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="+", bg='#c2eed8', command=lambda: btnClick("+")).grid(row=2, column =3)

btn6 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="6", bg='#c2eed8', command=lambda: btnClick(6)).grid(row=3, column =0)



btn5 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="5", bg='#c2eed8', command=lambda: btnClick(5)).grid(row=3, column =1)

btn4 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="4", bg='#c2eed8', command=lambda: btnClick(4)).grid(row=3, column =2)

Subtraction =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="-", bg='#c2eed8', command=lambda: btnClick("-")).grid(row=3, column =3)

btn3 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="3", bg='#c2eed8', command=lambda: btnClick(3)).grid(row=4, column =0)

btn2 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="2", bg='#c2eed8', command=lambda: btnClick(2)).grid(row=4, column =1)

btn1 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="1", bg='#c2eed8', command=lambda: btnClick(1)).grid(row=4, column =2)
Multiplication =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="*", bg='#c2eed8', command=lambda: btnClick("*")).grid(row=4, column =3)

btn0 =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="0", bg='#c2eed8', command=lambda: btnClick(0)).grid(row=5, column =0)
Clear =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="del", bg='#c2eed8',command=btnClear).grid(row=5, column =1)

equalTO =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="=", bg='#c2eed8', command= btnEqualTo).grid(row=5, column =2)

Division =Button(x2, padx=16, pady=16, bd=3,fg='black', font=('segoe UI', 15, 'bold'),
             text="/", bg='#c2eed8', command=lambda: btnClick("/")).grid(row=5, column =3)

#================================ PHARMACY INFO 1 ======================================================================

rand = StringVar()
pain = StringVar()
tonic = StringVar()
mala = StringVar()
oint = StringVar()
cough = StringVar()
herbal =StringVar()
other = StringVar()
ulcer = StringVar()
ophthmal =StringVar()
anti =StringVar()
contra = StringVar()
cost_charge = StringVar()
tax_charge = StringVar()
stotal = StringVar()
total = StringVar()
value0 = StringVar()
value1 =StringVar()
value2 =StringVar()
value3 =StringVar()
value4 =StringVar()
value5 =StringVar()
value6 =StringVar()
value7 =StringVar()
value8 =StringVar()
value9 =StringVar()
value10 =StringVar()
value11 =StringVar()


ib1Reference = Label(x1, font=('segoe UI',16, 'bold'), text='Medicine Reference',bd=1, bg= 'white', anchor='w', relief = RAISED)
ib1Reference.grid(row=0, column=0)
textReference =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=rand, bd=6, insertwidth=0,
                     bg='#c2eed8', justify='right')
textReference.grid(row=0, column=2, padx = 2, pady =12)



ib1Painkiller = Label(x1, font=('segoe UI',16, 'bold'), text='Painkillers',bd=1,bg= 'white', relief = RAISED)
ib1Painkiller.grid(row=1, column=0 , sticky=W)
textPainkiller =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=pain, bd=6, insertwidth=0,
                     bg='#c2eed8', justify='right')
textPainkiller.grid(row=1, column=2, padx = 5, pady =15)

ib1BloodTonic = Label(x1, font=('segoe UI',16, 'bold'), text='BloodTonic',bd=1, bg= 'white',anchor='w', relief =RAISED)
ib1BloodTonic.grid(row=2, column=0, sticky =W)
textBloodTonic =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=tonic, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textBloodTonic.grid(row=2, column=2,padx = 5, pady =15)


ib1Malaria = Label(x1, font=('segoe UI',16, 'bold'), text='Malarial Drugs',bd=1, bg= 'white',anchor='w', relief =RAISED)
ib1Malaria.grid(row=3, column=0, sticky =W)
textMalaria =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=mala, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textMalaria.grid(row=3, column=2,padx = 5, pady =15)


ib1Ointment = Label(x1, font=('segoe UI',16, 'bold'), text='Ointment',bd=1,bg= 'white', anchor='w', relief =RAISED)
ib1Ointment.grid(row=4, column=0, sticky =W)
textOintment =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=oint, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textOintment.grid(row=4, column=2,padx = 5, pady =15)


ib1Cough = Label(x1, font=('segoe UI',16, 'bold'), text='Cough Mixture',bd=1,bg= 'white', anchor='w', relief =RAISED)
ib1Cough.grid(row=5, column=0, sticky =W)
textCough =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=cough, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textCough.grid(row=5, column=2,padx = 5, pady =15)


ib1Herbal = Label(x1, font=('segoe UI',16, 'bold'), text='Herbal Mixture',bd=1, bg= 'white',anchor='w', relief =RAISED)
ib1Herbal.grid(row=6, column=0, sticky =W)
textHerbal =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=herbal, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textHerbal.grid(row=6, column=2,padx = 5, pady =15)


ib1Other = Label(x1, font=('segoe UI',16, 'bold'), text='AntiHypentensive',bd=1, bg= 'white', anchor='w', relief =RAISED)
ib1Other.grid(row=7, column=0, sticky =W)
textOther =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=other, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textOther.grid(row=7, column=2,padx = 5, pady =15)


#================== PHARMACY INFO 2 ============================================================

ib1Antibiotics = Label(x1, font=('segoe UI',16, 'bold'), text='AntiBiotics',bd=1, bg= 'white',anchor='w', relief =RAISED)
ib1Antibiotics.grid(row=0, column=3, sticky=W)
textAntibiotics =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=ulcer, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textAntibiotics.grid(row=0, column=5,padx = 5, pady =15)




ib1Ophthal = Label(x1, font=('segoe UI',16, 'bold'), text='Ophthalmic',bd=2,bg= 'white', anchor='w', relief =RAISED)
ib1Ophthal.grid(row=1, column=3, sticky=W)
textOphthmal =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=ophthmal, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textOphthmal.grid(row=1, column=5,padx = 5, pady =15)


ib1Anti = Label(x1, font=('segoe UI',16, 'bold'), text='AntiDiabetic',bd=1,bg= 'white', anchor='w', relief =RAISED)
ib1Anti.grid(row=2, column=3, sticky=W)
textAnti =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=anti, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textAnti.grid(row=2, column=5,padx = 5, pady =15)


ib1Cough = Label(x1, font=('segoe UI',16, 'bold'), text='Contraceptive',bd=1,bg= 'white', anchor='w', relief =RAISED)
ib1Cough.grid(row=3, column=3, sticky=W)
textCough =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=contra, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textCough.grid(row=3, column=5,padx = 5, pady =15)


ib1Tax = Label(x1, font=('segoe UI',16, 'bold'), text='Tax Charge',bd=1, bg= 'white',anchor='w', relief =RAISED)
ib1Tax.grid(row=4, column=3, sticky=W)
textTax =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=tax_charge, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textTax.grid(row=4, column=5,padx = 5, pady =15)


ib1Cost = Label(x1, font=('segoe UI',16, 'bold'), text='Cost',bd=1,bg= 'white', anchor='w', relief =RAISED)
ib1Cost.grid(row=5, column=3, sticky=W)
textCost =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=cost_charge, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textCost.grid(row=5, column=5,padx = 5, pady =15)


ib1Subtotal = Label(x1, font=('segoe UI',16, 'bold'), text='Subtotal',bd=1,bg= 'white', anchor='w', relief =RAISED)
ib1Subtotal.grid(row=6, column=3, sticky=W)
textSubtotal =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=stotal, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textSubtotal.grid(row=6, column=5,padx = 5, pady =15)

ib1Total = Label(x1, font=('segoe UI',16, 'bold'), text='Total Cost',bd=1,bg= 'white', anchor='w', relief =RAISED)
ib1Total.grid(row=7, column=3, sticky=W)
textTotal =Entry(x1, font=('segoe UI',10, 'bold'), textvariable=total, bd=6, insertwidth=4,
                     bg='#c2eed8', justify='right')
textTotal.grid(row=7, column=5,padx = 5, pady =15)

#===========================================DROPMENU==========================================

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value1, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =2, column =1)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value0, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =1, column =1)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value2, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =3, column =1)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value3, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =4, column =1)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value4, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =5, column =1)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value5, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =6, column =1)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value6, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =7, column =1)

'''box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value0, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =1, column =1)'''

#==========================================COLUMN TWO====================================================
box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value7, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =0, column =4)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value8, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =1, column =4)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value9, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =2, column =4)

box = ttk.Combobox(x1, font=("candera", 10, 'bold'), textvariable = value10, state = 'readonly')
box['values'] = ('','Para', 'Phopain', 'Efpac','Panacin', 'Kwik Action')
box.current(0)
box.grid(row =3, column =4)






#===============================  BUTTONS  ============================================================================

btnTotal =Button(x1,padx=16, pady=0,bd=8,fg='black',font=('segoe UI',16, 'bold'),
                 width=7,text='Total',bg='#c2eed8', command=Ref).grid(row=8,column=1)

btnReset =Button(x1,padx=16, pady=0,bd=8,fg='black',font=('segoe UI',16, 'bold'),
                 width=7,text='Reset',bg='#c2eed8', command=Reset).grid(row=8,column=2)

btnqExit =Button(x1,padx=16, pady=0,bd=8,fg='black',font=('segoe UI',16, 'bold'),
                 width=7,text='Quit',bg='#c2eed8', command=qExit).grid(row=8,column=3)







root.mainloop()

