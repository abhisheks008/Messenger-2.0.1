# creating a GUI
root = Tk()
root.title ("Messenger version 2.0.1")
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


# put the main code first and copy and paste the GUI code for creating the GUI and then run the both codes in a single file
# Author Abhishek Sharma
# 03rd November, 2020
