from tkinter import *
def CalculateClickButton(event):
    ResultBMI =(float(textBoxWeight.get())/(float(textBoxHight.get())/100)**2)
    if ResultBMI < 18.5 :
        print("ผอมเกินไป",ResultBMI)
        lableResult.configure(text="ผอมเกินไป")
    elif ResultBMI > 18.5 and ResultBMI < 23  :
        lableResult.configure(text="น้ำหนักปกติ")
        print("น้ำหนักปกติ",ResultBMI)
    elif ResultBMI > 23 and ResultBMI < 25  :
        lableResult.configure(text="น้ำหนักเกิน")
        print("น้ำหนักเกิน",ResultBMI)
    elif ResultBMI > 25 and ResultBMI < 30  :
        print("อ้วน",ResultBMI)
        lableResult.configure(text="อ้วน")
    else:
        print("อ้วนมาก",ResultBMI)
        lableResult.configure(text="อ้วนมาก")





main = Tk()
lableHight= Label(main,text="ส่วนสููง (cm.)")
lableHight.grid(row=0,column=0)
textBoxHight= Entry(main)
textBoxHight.grid(row=0,column=1)
lableWeight= Label(main,text="น้ำหนัก (Kg.)")
lableWeight.grid(row=1,column=0)
textBoxWeight= Entry(main)
textBoxWeight.grid(row=1,column=1)
buttonCalculate = Button(main, text="คำนวณ")
buttonCalculate.grid(row=2,column=0)
buttonCalculate.bind('<Button-1>',CalculateClickButton)
lableResult= Label(main,text="ผลลัพธ์")
lableResult.grid(row=2,column=1)
main.mainloop()