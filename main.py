# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
from Tkinter import *
#from Tkinter import  ttk
import matplotlib.pyplot as plt;
import pandas as pd
from pandas import DataFrame
from time import time 
from PIL import ImageTk,Image


def pl_2017_1():
    
    
    df=pd.read_csv("2017.csv")
    count=[]
    div=["A","B","C"]
    countA=0
    countB=0
    countC=0
    
    for col in df["Division"]:
         if col=="A": 
             countA=countA+1
         elif col=="B":
             countB=countB+1
         else:
             countC=countC+1
    
    
    count.append(countA)
    count.append(countB)
    count.append(countC)     
             
    
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
    
    plt.pie(count, labels=div, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Pie Chart")
    plt.title("Divisionwise Placements of Computer Engineering")
    plt.show()
    plt.close()
    
def pl_2018_1():
    df=pd.read_csv("2018.csv")
    count=[]
    div=["A","B","C"]
    countA=0
    countB=0
    countC=0

    for col in df["Div"]:
    	if col=="A": 
         countA=countA+1
     	elif col=="B":
         countB=countB+1
     	else:
         countC=countC+1


    count.append(countA)
    count.append(countB)
    count.append(countC)     
         

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
    plt.pie(count, labels=div, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Pie Chart")
    plt.title("Divisionwise Placements of Computer Engineering 2018")
    plt.show()
    plt.close()

def pl_2019_1():
	df=pd.read_csv("placement1.csv")
	pk=[]
	cmpn=[]
	for col in df["no_of_students_placed"]:
     		pk.append(float(col))
	for col in df["company_name"]:
     		cmpn.append(col)
   
	c_pos = [i for i, _ in enumerate(cmpn)]
	plt.bar(c_pos,pk, color='blue')
	plt.xlabel("Companies")
	plt.ylabel("no of students placed")
	plt.title(" Companywise Analysis of placements in 2019")
	plt.xticks(c_pos, cmpn,rotation=90,horizontalalignment="left")
	# Turn on the grid
	plt.minorticks_on()
	plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
	# Customize the minor grid
	plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
	plt.show()      

def pl_2019_2():

	df=pd.read_csv("single.csv")
	means_a = []
	means_b = []
	means_c=[]
	means_d=[]
	means_e=[]
	clg=[]

	for col in df["Civil_Engineering"]:
	     means_a.append(int(col))
	for col in df["Computer_Engineering"]:
	     means_b.append(int(col))
	for col in df["Entc_Engineering"]:
	     means_c.append(int(col))
	for col in df["It_Engineering"]:
	     means_d.append(int(col))
	for col in df["Mechanical_Engineering"]:
	     means_e.append(int(col))
	for col in df["college_name"]:
	     clg.append(col)

	labels=['PCET_NMIET_Talegaon','PCET_PCCOE_Nigdi','PCET_PCCOE&R _Ravet']
	c_pos = [i for i, _ in enumerate(labels)]
	g=DataFrame(df,columns=['Civil_Engineering','Computer_Engineering','Entc_Engineering','It_Engineering','Mechanical_Engineering'])
	g.plot(kind='bar')
	plt.minorticks_on()
	plt.xticks(c_pos,labels,rotation=360)
	plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
	plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
	plt.title("Single offers analysis")
	plt.legend(loc="best")
	plt.show()

def pl_2019_3():

	df=pd.read_csv("double.csv")
	means_a = []
	means_b = []
	means_c=[]
	means_d=[]
	means_e=[]
	clg=[]

	for col in df["Civil_Engineering"]:
     		means_a.append(int(col))
	for col in df["Computer_Engineering"]:
     		means_b.append(int(col))
	for col in df["Entc_Engineering"]:
     		means_c.append(int(col))
	for col in df["It_Engineering"]:
     		means_d.append(int(col))
	for col in df["Mechanical_Engineering"]:
     		means_e.append(int(col))
	for col in df["college_name"]:
     		clg.append(col)

	labels=['PCET_NMIET_Talegaon','PCET_PCCOE_Nigdi','PCET_PCCOE&R _Ravet']
	c_pos = [i for i, _ in enumerate(labels)]
	g=DataFrame(df,columns=['Civil_Engineering','Computer_Engineering','Entc_Engineering','It_Engineering','Mechanical_Engineering'])
	g.plot(kind='bar')
	plt.minorticks_on()
	plt.xticks(c_pos,labels,rotation=360)
	plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
	plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
	plt.title("Double offers analysis")
	plt.legend(loc="best")
	plt.show()

def pl_2018_2():

	df=pd.read_csv("2018placement.csv")
	pk=[]
	cmpn=[]
	for col in df["no_of_students_placed"]:
     		pk.append(float(col))
	for col in df["company_name"]:
     		cmpn.append(col)
   
	c_pos = [i for i, _ in enumerate(cmpn)]
	plt.bar(c_pos,pk, color='blue')
	plt.xlabel("Companies")
	plt.ylabel("no of students placed")
	plt.title(" Companywise Analysis of placements in 2018")
	plt.xticks(c_pos, cmpn,rotation=90,horizontalalignment="left")
	# Turn on the grid
	plt.minorticks_on()
	plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
	# Customize the minor grid
	plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
	plt.show()
 
def pl_2018_3():
             main=Tk();
             main.geometry('300x300')
             main.title("Offer count")
             main.configure(background='lightgreen')
             df=pd.read_csv("2018.csv")

             cs1=df['Company_Select_1']
             d="Total count of single offer is:",cs1.notnull().sum()
             messageVar = Message(main, text = d,width=300)  
             messageVar.config(bg='lightgreen') 
	     messageVar.pack( ) 

             cs2=df['Company_Select_2']
             d="Total count of double offer is:",cs2.notnull().sum()
             messageVar1 = Message(main, text = d,width=300)  
             messageVar1.config(bg='lightgreen') 
	     messageVar1.pack( ) 

             cs3=df['Company_Select_3']
             d="Total count of triple offer is:",cs3.notnull().sum()
             messageVar2 = Message(main, text = d,width=300)  
             messageVar2.config(bg='lightgreen') 
	     messageVar2.pack( ) 
	     main.mainloop( )  

def pl_2017_2(): 
             main=Tk();
             main.geometry('300x300')
             main.title("No of students placed:")
             main.configure(background='lightgreen')
             df=pd.read_csv("2017.csv")

             cs1=df['Job']
             d="Total count of students placed is:",cs1.notnull().sum()
             messageVar = Message(main, text = d,width=300)  
             messageVar.config(bg='lightgreen') 
	     messageVar.pack( )
             main.mainloop( )  

def pl_2017_3():            
             main=Tk();
             main.geometry('300x300')
             main.title("No of students higher studies :")
             main.configure(background='lightgreen')
             df=pd.read_csv("2017.csv")

             cs2=df['Higher_Studies']
             d="Number of students went for Higher studies:",cs2.notnull().sum()
             messageVar = Message(main, text = d,width=300)  
             messageVar.config(bg='lightgreen') 
	     messageVar.pack( ) 

def pl_2019_4():
                
                df=pd.read_csv("2019branch.csv")
		means_a = []
		means_b = []
		means_c=[]
		means_d=[]
		br=[]

		for col in df["Eligible_Students"]:
		    means_a.append(int(col))
		for col in df["Single_Offer"]:
		     means_b.append(int(col))
		for col in df["Double_Offer"]:
		     means_c.append(int(col))
		for col in df["Tripple_Offer"]:
		     means_d.append(int(col))
		for col in df["Branch"]:
		     br.append(col)

		labels=['Computer','E&TC','IT','Mech','Civil']
		c_pos = [j for j, _ in enumerate(labels)]
		g=pd.DataFrame(df,columns=['Eligible_Students','Single_Offer','Double_Offer','Tripple_Offer'])
		g.plot(kind='bar')
		plt.minorticks_on()
		plt.xticks(c_pos,labels,rotation=360)
		plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
		plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
		plt.title("Branchwise placement analysis")
		plt.legend(loc="best")
		plt.show()

def pl_2018_4():
                df=pd.read_csv("2018.csv")
		count=[]
		Gender=["Male","Female"]
		countM=0
		countF=0
		n_groups=1

		for col in df['Gender']:
		     if col=="M": 
			 countM=countM+1
		     else:
			 countF=countF+1
		   
		count.append(countM)
		count.append(countF)

		colors = ["#1f77b4", "#ff7f0e"]
		explode = (0.1, 0)  
		plt.pie(count, labels=Gender, colors=colors,
		autopct='%1.1f%%', shadow=True, startangle=140)
		plt.title("Pie Chart")
		plt.title("Gender ratio of placement")
		plt.show()

def back():
 
		

		def pl_2017_():
                    root.destroy()
		    r=Tk();
		    r.geometry('800x800')
		    r.title("2017 Placements")
                    la=Label(r,text="2017 Placement Analysis",width=40,font=("bold",20),bg='aqua')
		    la.place(x=90,y=53)  
		    r.configure(background='aqua')
		    def back1():
			r.destroy()
			back()
		
		    Button(r,text="Divisionwise placement analysis", height="2", width="30",bg='orange',fg='black',command=pl_2017_1).place(x=280,y=210)
		    Button(r,text="students placed", height="2", width="30",bg='orange',fg='black',command=pl_2017_2).place(x=280,y=260)
		    Button(r,text="Higher Studies", height="2", width="30",bg='orange',fg='black',command=pl_2017_3).place(x=280,y=310)
		    #Button(r,text="2019", height="2", width="30",bg='orange',fg='black').place(x=280,y=360)
		    #Button(r,text="2019", height="2", width="30",bg='orange',fg='black').place(x=280,y=410)
		    Button(r,text='Back', height="2", width="10",bg='black',fg='white', command=back1).place(x=680,y=650)
		    
		    

		def pl_2018_():
                    root.destroy()
		    r=Tk();
		    r.geometry('800x800')
		    r.title("2018 Placements") 
                    la=Label(r,text="2018 Placement Analysis",width=40,font=("bold",20),bg='aqua')
		    la.place(x=90,y=53)
		    r.configure(background='aqua')
                    def back1():
			r.destroy()
			back() 
		    Button(r,text="Divisionwise placement analysis", height="2", width="30",bg='orange',fg='black',command=pl_2018_1).place(x=280,y=210)
		    Button(r,text="companywise placement analysis", height="2", width="30",bg='orange',fg='black',command=pl_2018_2).place(x=280,y=260)
		    Button(r,text="Offer count", height="2", width="30",bg='orange',fg='black',command=pl_2018_3).place(x=280,y=310)
		    Button(r,text="Gender ratio of placement", height="2", width="30",bg='orange',fg='black',command=pl_2018_4).place(x=280,y=360)
		    #Button(r,text="2019", height="2", width="30",bg='orange',fg='black').place(x=280,y=410)
		    Button(r,text='Back', height="2", width="10",bg='black',fg='white', command=back1).place(x=680,y=650)
		    
		def pl_2019_():
		    root.destroy()
                    r=Tk();
		    r.geometry('800x800')
		    r.title("2019 Placements") 
                    la=Label(r,text="2019 Placement Analysis",width=40,font=("bold",20),bg='aqua')
		    la.place(x=90,y=53)
		    r.configure(background='aqua') 
                    def back1():
			r.destroy()
			back()
		    Button(r,text="companywise placement analysis", height="2", width="30",bg='orange',fg='black',command=pl_2019_1).place(x=280,y=210)
		    Button(r,text="collegewise single offer analysis", height="2", width="30",bg='orange',fg='black',command=pl_2019_2).place(x=280,y=260)
		    Button(r,text="collegewise double offer analysis", height="2", width="30",bg='orange',fg='black',command=pl_2019_3).place(x=280,y=310)
		    Button(r,text="Branchwise placement analysis", height="2", width="30",bg='orange',fg='black',command=pl_2019_4).place(x=280,y=360)
		    #Button(r,text="2019", height="2", width="30",bg='orange',fg='black').place(x=280,y=410)
		    Button(r,text='Back', height="2", width="10",bg='black',fg='white', command=back1).place(x=680,y=650)

                root  = Tk()
		root.geometry('800x800')
		root.title("Pccoe Placements")
                canvas = Canvas(root, width = 800, height = 600)  
                canvas.pack()  
                img = ImageTk.PhotoImage(Image.open("pccoe1.jpg"))  
                canvas.create_image(0, 0, anchor=NW, image=img)


		la=Label(root,text="Placement Analysis System",width=40,font=("bold",20),bg='white')
		la.place(x=90,y=53)
		root.configure(background='white')

		Button(root,text="2017", height="2", width="20",bg='maroon',fg='white',command=pl_2017_).place(x=30,y=420)

		Button(root,text="2018", height="2", width="20",bg='maroon',fg='white',command=pl_2018_).place(x=250,y=420)

		Button(root,text="2019", height="2", width="20",bg='maroon',fg='white',command=pl_2019_).place(x=480,y=420)

		
		
		root.mainloop()
    
back()


