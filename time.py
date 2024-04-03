from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec=time.strftime('%S')
    am= time.strftime("%p")
    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%A")
    
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    
    lab_hr.after(200,date_time)
clock=Tk()
clock.title('  Python Clock')
clock.geometry('1000x500')
clock.config(bg='#420D09')


lab_hr=Label(clock,text="00",font=("Arial",60),fg="#FFC37F",bg="black")
lab_hr.place(x=40,y=50,height=150,width=100)
lab_txt=Label(clock,text="Hr.",font=("Arial Bold",30),fg="#FFC37F",bg="black")
lab_txt.place(x=40,y=220,height=40,width=100)



lab_min=Label(clock,text="00",font=("Arial Bold",60),fg="#FFC37F",bg="black")
lab_min.place(x=300,y=50,height=150,width=100)
lab_txt=Label(clock,text="Min.",font=("Arial",30),fg="#FFC37F",bg="black")
lab_txt.place(x=300,y=220,height=40,width=100)

lab_sec=Label(clock,text="AM/PM",font=("Arial Bold",20 ),fg="#FF8B3E", bg="black")
lab_sec.place(x=800,y=220,height=40,width=100)
lab_txt=Label(clock,text="Sec.",font=("Arial Bold",30),fg="#FFC37F",bg="black")
lab_txt.place(x=560,y=220,height=40,width=100)

lab_am=Label(clock,text="00",font=("Arial",60 ),fg="#FF8B3E", bg="black")
lab_am.place(x=800,y=50,height=150,width=100)
lab_sec=Label(clock,text="AM/PM",font=("Arial Bold",60),fg="#FFC37F",bg="black")
lab_sec.place(x=550,y=50,height=150,width=100)

#********date**********
lab_date=Label(clock,text="00",font=("Arial",60),fg="#FFC37F",bg="black")
lab_date.place(x=40,y=300,height=150,width=100)
lab_date_txt=Label(clock,text="Date",font=("Arial Bold",30),fg="#FFC37F",bg="black")
lab_date_txt.place(x=40,y=500,height=40,width=100)

lab_mo=Label(clock,text="00",font=("Arial",60),fg="#FFC37F",bg="black")
lab_mo.place(x=300,y=300,height=150,width=100)
lab_mo_txt=Label(clock,text="Month",font=("Arial Bold",20),fg="#FFC37F",bg="black")
lab_mo_txt.place(x=300,y=500,height=40,width=100)

lab_year=Label(clock,text="00",font=("Arial",60),fg="#FFC37F",bg="black")
lab_year.place(x=550,y=300,height=150,width=100)
lab_year_txt=Label(clock,text="Year",font=("Arial Bold",30),fg="#FFC37F",bg="black")
lab_year_txt.place(x=550,y=500,height=40,width=100)

lab_day=Label(clock,text="00",font=("Arial",14),fg="#FFC37F",bg="black")
lab_day.place(x=800,y=300,height=150,width=100)
lab_day_txt=Label(clock,text="Day",font=("Arial Bold",30),fg="#FFC37F",bg="black")
lab_day_txt.place(x=800,y=500,height=40,width=100)

date_time()

clock.mainloop()  