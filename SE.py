class Queue:

  def __init__(self):
      self.queue = list()

  def insert(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False

  def size(self):
      return len(self.queue)
    # Pop method to remove element
  def remove(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")
#################################################################
def match(s1,s2,flag):
    s1=s1.lower()
    s2=s2.lower()
    if flag==0:
        if s2 in s1:
            return False
        else:
            return True
    else:
        if s2==s1:
            return False
        else:
            return True
###############################################################
def click():
	os.system('./test.sh '+str(listbox.get(listbox.curselection())))

#############################################################
def algo():
	search= Queue()
	search.insert(root)
	unknown=str(x.get())
	engine=not(int(var1.get()))
	result=[]
	number_of_check=0
	number_of_match=0
	while search.size():
    		try:
        		address=search.remove()
        		l=os.listdir(address)
        		if len(l)>0:
            			for name in os.listdir(address):
                			number_of_check+=1
                			if not(match(name,unknown,engine)):
                    				result.append(str(address+'/'+name))
                    				number_of_match+=1
                			if match(str(name),'.',0):
                    				search.insert(address+'/'+name)
                    
    		except:
        		a=1

	listbox.delete(0, END)
	if len(result):
              a=1
	else:
              listbox.insert(END, "no match found")
	label1.config(text="Total check: "+str(number_of_check))
	label2.config(text="Total match: "+str(number_of_match))
	for list_search in result:
		listbox.insert(END, str(list_search))
########################################################################################


import os,sys
from tkinter import *
root="/home"
r = Tk() 
r.title('Search Engine')
r.geometry('550x300')
var1 = IntVar() 
x=StringVar()
w=Entry(r, textvariable=x)
st1=Checkbutton(r, text='All search', variable=var1)
button2=Button(r, text='Search', width=25, command=algo) 
button3=Button(r, text='open', width=10, command=click) 
button1 =Button(r, text='Stop', width=25, command=r.destroy)
label1 = Label( r, text=" " )
label2 = Label(r,text=" ") 
scrollbar = Scrollbar(r)
listbox = Listbox(r, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.pack(side=LEFT, fill=BOTH)
scrollbar.pack(side=RIGHT, fill=Y)
st1.pack()
w.pack()
button2.pack() 
button1.pack()
button3.pack()
w.place(x = 10, y =10, width=250, height=25) 
st1.place(x =230, y =10, width=200, height=25 )
button2.place(x = 10, y =50, width=100, height=25) 
button3.place(x = 270, y =260, width=100, height=25) 
button1.place(x = 150, y =50, width=100, height=25) 
label1.place(x=280,y=50)
label2.place(x=280,y=70)
listbox.place(x=10,y=100,width=500)
r.mainloop() 










