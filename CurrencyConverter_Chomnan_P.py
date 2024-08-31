from currency_converter import CurrencyConverter
c = CurrencyConverter(fallback_on_missing_rate=True)

from tkinter import *
from tkinter import ttk

MainWindow = Tk()
MainWindow.title("Currency converter")
MainWindow.geometry('400x200')
list_currency = ['AUD', 'PLN', 'RON', 'HKD', 'HRK', 'MTL', 'DKK', 'HUF', 'SGD', 'GBP'
                 , 'IDR', 'NZD', 'JPY', 'MYR', 'INR', 'CNY', 'EEK', 'TRL', 'CYP', 'MXN'
                 , 'PHP', 'BGN', 'CAD', 'ZAR', 'SEK', 'SIT', 'LTL', 'RUB', 'SKK', 'EUR'
                 , 'NOK', 'BRL', 'ROL', 'KRW', 'USD', 'CHF', 'ILS', 'ISK', 'THB', 'LVL'
                 , 'CZK', 'TRY']

combo_currency = ttk.Combobox(MainWindow,values=list_currency,width=6)
combo_currency.place(x=120, y=50)
combo_new_currency = ttk.Combobox(MainWindow,values=list_currency,width=6)
combo_new_currency.place(x=305, y=50)

text_box_currency = Entry(MainWindow,width=15)
text_box_currency.place(x=20, y=51)

button_convert_click = Button(MainWindow, text="convert")
button_convert_click.place(x=20, y=75)

lable_result = Label(MainWindow,text="Amount",width=13,borderwidth=1, relief="solid")
lable_result.place(x=205, y=51)
label1= Label(MainWindow,text="Amount and currency :")
label1.place(x=20, y=25)
label2= Label(MainWindow,text="Select new currency :")
label2.place(x=205, y=25)
label3= Label(MainWindow,text="to")
label3.place(x=185, y=50)
label_last_available_date_currency = Label(MainWindow)
label_last_available_date_currency.place(x=22, y=101)


def search_currency(event):
   value = event.widget.get()
   if value == '' :
      combo_currency['value'] = list_currency
   else:
      data = []

      for item in list_currency:
         if value.lower() in item.lower():
            data.append(item)
      combo_currency['values'] = data


def search_new_currency(event):
   value = event.widget.get()
   if value == '' :
      combo_new_currency['value'] = list_currency
   else:
      data = []

      for item in list_currency:
         if value.lower() in item.lower():
            data.append(item)
      combo_new_currency['values'] = data


def convert_click_button(event):

   result_exchange = c.convert(float(text_box_currency.get()), combo_currency.get(), combo_new_currency.get())
   print(result_exchange)
   result_exchange = float("{:.2f}".format(result_exchange))
   lable_result.configure(text=result_exchange)
   first_date, last_date = c.bounds[combo_currency.get()]
   rate_currency = c.convert(1, combo_currency.get(), combo_new_currency.get())
   last_update_currency = "1 " + str(combo_currency.get()) + " : " + str(float("{:.2f}".format(rate_currency))) + " " + str(combo_new_currency.get()) + ' last update on ' + str(last_date)
   label_last_available_date_currency.configure(text=last_update_currency)



combo_currency.set('Search')
combo_new_currency.set('Search')
combo_currency.bind('<KeyRelease>',search_currency)
combo_new_currency.bind('<KeyRelease>',search_new_currency)
button_convert_click.bind('<Button-1>',convert_click_button)


MainWindow.mainloop()