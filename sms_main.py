import requests
import json
from tkinter import *
from tkinter.messagebox import showerror,showinfo

def send_sms(number, message):
    url = " " #put your URL from the website
    params = {
        'authorization' : '',  # put the Authorization API here
        'sender_id' : ' ', # put the sender_id here
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
