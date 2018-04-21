# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import mysql.connector
import paramiko
import csv
from sshtunnel import SSHTunnelForwarder
from tkinter import *
from PIL import ImageTk, Image
from mysql.connector import errorcode

#bulk task
def show_entry_fields():

    #establishes an ssh tunnel
    server = SSHTunnelForwarder(
            ("ceres.ucsd.edu", 22),
            ssh_username="ceres",
            ssh_pkey="/Users/tylerreagan/.ssh/id_rsa",
            remote_bind_address=('127.0.0.1', 3306))
    server.start();

    #connects to MySQL database
    db = mysql.connector.connect(user='root',
                                 password='4aGuP.Ta',
                                 host='127.0.0.1',
                                 port=server.local_bind_port,
                                 database='gene_dictionary')

    ##cursor object to exeecute queries
    cursor = db.cursor()

    #binds user input for locus to a variable
    locus = e1.get()
    
    #23kchip query skeleton
    query23 = ("SELECT 23kchip.Locus, 23kchip.Probe_ID, exp_nums.Signal, exp_nums.P, exp_nums.p_val, exp_info.Ecotype, exp_info.Tissue, exp_info.Treatment FROM exp_nums INNER JOIN 23kchip USING (Probe_ID) INNER JOIN exp_info USING (Expt) WHERE 23kchip.Locus=%s", (locus, ))
    
    #8kchip query skeleton
    query08 = ("SELECT 8kchip.Locus, 8kchip.Probe_ID, exp_nums.Signal, exp_nums.P, exp_nums.p_val, exp_info.Ecotype, exp_info.Tissue, exp_info.Treatment FROM exp_nums INNER JOIN 8kchip USING (Probe_ID) INNER JOIN exp_info USING (Expt) WHERE 8kchip.Locus=%s", (locus, ))
    
    #executes 23kchip query
    try:
        cursor.execute(*query23)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    
    #calls fetchone until None is returned (no more rows) for 23kchip
    #checks if query is blank
    result23 = ()
    if cursor.fetchone() == None:
        pass
    else:
        for row in iter(cursor.fetchone, None):
            result23 += (row, )
            #print(row)
        
    #creates and populates a temp .csv file with results
        csv23 = open("Schroeder:23k(%s).csv" % locus,'w')
        writer = csv.writer(csv23, dialect = 'excel')
        writer.writerow(['Locus','Probe_ID','Signal','P','p_val','Ecotype','Tissue','Treatment'])
        writer.writerows(result23)
        csv23.close()
        print('\nAn excel file Schroeder:23k(%s).csv has been made to display your results.' % locus)
        #print('WARNING: This file may possibly be overwritten after your next search.')
        
    #executes 8kchip query
    try:
        cursor.execute(*query08)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    #calls fetchone until None is returned (no more rows) for 8kchip
    #checks if query is blank
    result08 = ()
    if cursor.fetchone() == None:
        pass
    else:
        for row in iter(cursor.fetchone, None):
            result08 += (row, )
            #print(row)

    #creates and populates a temp .csv file with results
        csv08 = open("Schroeder:8k(%s).csv" % locus,'w')
        writer = csv.writer(csv08, dialect = 'excel')
        writer.writerow(['Locus','Probe_ID','Signal','P','p_val','Ecotype','Tissue','Treatment'])
        writer.writerows(result08)
        csv08.close()
        print('\nAn excel file Schroeder:8k(%s).csv has been made to display your results.' % locus)
        #print('WARNING: This file may possibly be overwritten after your next search.')
    
    #kills cursor, closes connection to database, and wipes entry form field
    cursor.close()
    db.close()
    server.stop();
    e1.delete(0,END)

    #informs the user that their query is complete for given locus
    print('\nThe results for locus %s have been printed. \n' % locus)

def quit():
    global master
    master.destroy()

#creates and manages the displayed window
master = Tk()
master.title("Encyclogenia")
master.geometry("420x420")
master.configure(background='grey')

#setting up image
img = ImageTk.PhotoImage(Image.open("DNAboiz.jpg"))

#displaying image
imglabel = Label(master, image=img).grid(row=1, column=1, sticky="NSWE")

Label(master, text="Locus").grid(row=0, column=0, padx=10)

#entry box
e1 = Entry(master)

#fills starting entry box
e1.insert(10,"ATMG00640")

e1.grid(row=0, column=1, pady=(10, 10))

#show button code to initiate query
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=0, pady=10)
Button(master, text='Quit', command=quit).grid(row=3, column=1, pady=10)

mainloop( )
