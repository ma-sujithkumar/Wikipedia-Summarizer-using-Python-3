#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox
from wikipedia import *
import csv
import os


# In[2]:


master=Tk()


# In[3]:


def Search():
    data=text1.get()
    name=data+".txt"
    file=open(name,"w",encoding='utf8')
    sentences1=text2.get()
    try:
        result=wikipedia.summary(data,sentences=sentences1)
    except:
        messagebox.showerror("Wiki Searcher", "Difficult to identify, Provide more information")
    else:
        result=wikipedia.summary(data,sentences=sentences1)
        file.write(result)
        messagebox.showinfo("Wiki Searcher","Succesfully searched and saved")
    


# In[4]:


def Open():
    data=text1.get()
    name=data+".txt"
    os.system(name)


# In[5]:


def clear():
    text1.delete(0,END)
    text2.delete(0,END)


# In[6]:


def Save():
    return


# In[7]:


label1=Label(master,text="Enter the thing you want to search:")
label2=Label(master,text="Enter the number of sentences:")
label3=Label(master,text="Select the format:")
b1=Button(master,text="Search and Save",command=Search,padx=30,pady=20,font=15)
b3=Button(master,text="Open",command=Open,padx=30,pady=20,font=15)
b4=Button(master,text="Exit",command=master.quit,padx=30,pady=20,font=15)
b5=Button(master,text="Clear",command=clear,padx=30,pady=20,font=15)
text1=Entry(master,width=35,font=13,borderwidth=5)
text2=Entry(master,width=35,font=13,borderwidth=5)


# In[8]:


label1.grid(row=0,column=0)
text1.grid(row=1,column=0,ipadx=20,ipady=15)
label2.grid(row=2,column=0)
text2.grid(row=3,column=0,ipadx=20,ipady=15)
label3.grid(row=4,column=0)
b1.grid(row=7)
b3.grid(row=8)
b4.grid(row=9)
b5.grid(row=10)


# In[9]:


master.mainloop()

