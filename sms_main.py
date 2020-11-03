import requests
import json
from tkinter import *
from tkinter.messagebox import showerror,showinfo

def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulk"
    params = {
        'authorization' : 'JLX7bm0UsAS2EqWRGxFCh48wcPanBp9gIriHuVyTdkt3NDzjQ6GiKm6NWwtHQ8MZF1ckyb9fsqSJTedX',
        'sender_id' : 'SMSIND',
        'message' : message,
        'language' : 'english',
        'route' : 'p',
        'numbers' : number
    }
    response = requests.get(url, params = params)
    dic = response.json()
    print (dic)
    return dic.get('return')

def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms (num,msg)
    if (r==True):
        showinfo("Success!!","Message sent successfully")
    else:
        showerror("Error while sending","Something went wrong. Try again!")



# creating a GUI
root = Tk()
root.title ("Messenger version 2.0.0")
root.geometry("400x625")
font = ('Times new roman', 18, 'bold')

textNumber = Entry(root, font = font)
textNumber.pack(fill = X, pady = 20)

font1 = ('times new roman', 14)
textMsg = Text(root, font = font1)
textMsg.pack(fill = X)

sendBtn = Button(root, text = "SEND MESSAGE", command = btn_click)
sendBtn.pack()



root.mainloop()
