from tkinter import scrolledtext
from tkinter import *
window=Tk()


# txtfld=Entry(window, width=30, text="This is Entry Widget", bd=5, borderwidth=1, justify=CENTER)
# txtfld.place(x=320, y=80)
# txtfld.grid(column=30, row=10)
stxt = scrolledtext.ScrolledText(window,width=50,height=15,
                                 borderwidth=1, bg='white',
                                 font=("Helvetica", 15))
stxt.insert(END, "Bijoy Text here")
stxt.pack(fill= BOTH, expand= True)


# Button
def clicked():
    res = stxt.get("1.0", END)
    out_txt.insert("1.0", res+"\n")

btn=Button(window, width=18, text="কনভার্ট করুন", fg='black', command=clicked, font=('Helvetica 15'), bg= "white")
btn.pack(pady=10)


# lbl=Label(window, text="ইউনি কোড টেক্সট", fg='red', font=("Helvetica", 20))
out_txt = scrolledtext.ScrolledText(window,width=50, height=15, 
                                    borderwidth=1, bg='white',
                                    font=("Helvetica", 15))
out_txt.insert(END, "ইউনি কোড টেক্সট")
out_txt.pack(fill= BOTH, expand= True)

window.title('রকমারি বিজয় টেক্সট কনভার্টার')
window.geometry("800x700+10+10")
window.mainloop()