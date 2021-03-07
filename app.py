from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import json



class Country:
    def __init__(self,root):
        self.root=root
        self.root.title("Countries Data")
        self.root.geometry("500x500")
        self.root.iconbitmap("logo990.ico")
        self.root.resizable(0,0)


        country_name=StringVar()


        def on_enter1(e):
            but_show['background']="black"
            but_show['foreground']="cyan"
            
            

        def on_leave1(e):
            but_show['background']="SystemButtonFace"
            but_show['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




        def clear():
            country_name.set('Select Country Name')
            text.delete('1.0','end')

        def getdata():
            text.delete('1.0','end')
            name=country_name.get()
            with open("country.json","r") as f:
                data=f.read()
            loading_data=json.loads(data)
            
            for i in range(len(loading_data)):
                if loading_data[i]['name']==name:
                    country_data=json.dumps(loading_data[i],indent=4)
                    text.insert('end',country_data)
            # print(country_name.get())


#================frame========================
        mainframe=Frame(self.root,width=500,height=500,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=150,relief="ridge",bd=3)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=343,relief="ridge",bd=3)
        secondframe.place(x=0,y=150)

#=================================================
        countries=["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda"\
                  ,"Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain"\
                  ,"Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia"\
                  ,"Bosnia and Herzegovina","Botswana","Brazil","Brunei Darussalam","Bulgaria","Burkina Faso"\
                  ,"Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Republic","Chad"\
                  ,"Chile","China","Colombia","Comoros","Congo (Brazzaville)","Congo (Kinshasa)","Costa Rica"\
                  ,"Croatia","Cuba","Cyprus","Czech Republic","Côte d'Ivoire","Denmark","Djibouti","Dominica"\
                  ,"Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia"\
                  ,"Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada"\
                  ,"Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Holy See","Honduras","Hungary"\
                  ,"Iceland","India","Indonesia","Iran (Islamic Republic of)","Iraq","Ireland","Israel","Italy","Jamaica"\
                  ,"Japan","Jordan","Kazakhstan","Kenya","Korea (Republic of)","Korea (Democratic People's Republic of)"\
                  ,"Kuwait","Kyrgyzstan","Lao PDR","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania"\
                  ,"Luxembourg","Macao","Macedonia (the former Yugoslav Republic of)","Madagascar","Malawi","Malaysia","Maldives"\
                  ,"Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro"\
                  ,"Morocco","Mozambique","Myanmar","Namibia","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","Norway"\
                  ,"Oman","Pakistan","Palestine, State of","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal"\
                  ,"Qatar","Republic of Kosovo","Romania","Russian Federation","Rwanda","Réunion","Saint Kitts and Nevis","Saint Lucia"\
                  ,"Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles"\
                  ,"Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka"\
                  ,"Sudan","Suriname","Swaziland","Sweden","Switzerland","Syrian Arab Republic","Taiwan","Tajikistan"\
                  ,"Tanzania, United Republic of","Thailand","Timor-Leste","Togo","Trinidad and Tobago","Tunisia","Turkey","Uganda","Ukraine","United Arab Emirates"\
                  ,"United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Venezuela (Bolivarian Republic of)","Viet Nam","Western Sahara","Yemen"\
                  ,"Zambia","Zimbabwe"]
        select_state_combo=Combobox(firstframe,value=countries,font=('times new roman',14),width=40,state="readonly",textvariable=country_name)
        select_state_combo.set("Select Country Name")
        select_state_combo.place(x=50,y=30)



        but_show=Button(firstframe,text="Show Data",font=('times new roman',13),width=15,cursor="hand2",command=getdata)
        but_show.place(x=60,y=90)
        but_show.bind("<Enter>",on_enter1)
        but_show.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,text="Clear",font=('times new roman',13),width=15,cursor="hand2",command=clear)
        but_clear.place(x=280,y=90)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#=================================================

        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=17,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black",wrap="word")      
        text.place(x=0,y=3)
        scol.config(command=text.yview)
         

        



if __name__=="__main__":
    root=Tk()
    Country(root)
    root.mainloop()