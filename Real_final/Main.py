#Hugo Zamarripa
#This Program will ask user for input on how much change he has and then display it in a graphical interface

from tkinter import *
from Hospital import Surgery
from Hospital import PatientAccount
from Hospital import Medication

fields = ('Patient Name', 'Days Spent', 'Surgery Type', 'Medication', 'Days Cost', 'Surgery Cost', 'Medication Cost',
          'Total Charge')


def get_values(entries):
    d = (float(entries['Days Spent'].get())) #calls class ro proccess the data
    s = (str(entries['Surgery Type'].get()))
    m = (str(entries['Medication'].get()))

    surg = Surgery(d, s, m)
    pat = PatientAccount(d, s, m)
    med = Medication(d, s, m)

    entries['Days Cost'].delete(0, END)#prints data into the empty fields
    entries['Days Cost'].insert(0, pat.days())
    entries['Surgery Cost'].delete(0, END)
    entries['Surgery Cost'].insert(0, surg.searchsurgery())
    entries['Surgery Cost'].delete(0, END)
    entries['Medication Cost'].insert(0, med.searchmeds())  # insert the computed values
    entries['Medication Cost'].delete(0, END)


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


if __name__ == '__main__':
    root = Tk()#create new GUI
    ents = makeform(root, fields)
    root.title("Medical Reciept")
    root.geometry('400x400')#control size
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Compute',
                command=(lambda e=ents: get_values(e))) #calls get calue to analyze input
    b1.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
