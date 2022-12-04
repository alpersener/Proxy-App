import os
import sys
import time
from tkinter import messagebox
import requests
import winreg
import csv
import concurrent.futures
import tkinter as tk
import customtkinter
from urllib.request import urlopen
import re as r
import urllib
import socket
import pandas as pd

## INTERNET SETTINGS VE PROXY AÇIP KAPATMA
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
    0, winreg.KEY_ALL_ACCESS)

def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
#------------------------------------------------------------------------------------------------------------------------
# PROXY LİSTESİ KONTROL ETME
proxylist = []

with open('proxylist.csv', 'r') as file:
        reader = csv.reader(file)
        for sira in reader:
            proxylist.append(sira[0])


#--------------------------------------------------------------------------------------------------------------------------
#GUI KISIMLARI
def proxyAc():
    button3.pack()
    button4.pack_forget()
    def proxyAyarlama(proxy):
        # user agent browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
        try:
            # httpin ile proxy çalışıyor mu kontrol etme
            r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http': proxy, 'https': proxy},
            timeout=1)
            print(r.json(), ' | Calisiyor | ', r.status_code)
            if (r.status_code == 200):
                val = proxy
                for sira in val:
                    if(val==val):
                        dosya = open('proxylistv2.csv', 'a')
                        print(val,file=dosya)
                        dosya.close()
                        break
                set_key('ProxyEnable', 1)
                set_key('ProxyOverride', u'*.local;<local>')
                set_key('ProxyServer', val)

        except:
            pass
        return proxy


    with concurrent.futures.ThreadPoolExecutor() as executor:
     executor.map(proxyAyarlama, proxylist)

def proxyKapat():
    set_key('ProxyEnable', 0)
    button3.pack_forget()
    button4.pack()
    os.remove('proxylistv2.csv')


def ipGoster():
    ip = urllib.request.getproxies()
    msg=messagebox.showinfo("IP:",ip)

#def checkButtonTiklandi():
    #for i in range(sum(1 for row in 'proxylistv2.csv')):

        #time.sleep(15)  #

#-------------------------------------------------------------------------------------------------------
#GUI KISIMLARI


customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("500x350")

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=50,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="PROXY",font=("Roboto",44))
label.pack(pady=12,padx=10)

button3 = tk.Button(master=frame,text="PROXY AÇIK",bg="green")
button4=tk.Button(master=frame,text="PROXY KAPALI",bg="red")


#entry1=customtkinter.CTkEntry(master=frame,placeholder_text="Username")
#entry1.pack(pady=12,padx=10)

button=customtkinter.CTkButton(master=frame,text="Proxy Aç",command=proxyAc)
button.pack(pady=12,padx=10)

button2=customtkinter.CTkButton(master=frame,text="Proxy kapat",command=proxyKapat)
button2.pack(pady=12,padx=10)

checkbox=customtkinter.CTkCheckBox(master=frame,text="Timer",command="checkButtonTiklandi")
checkbox.pack(pady=12,padx=10)

button5=customtkinter.CTkButton(master=frame,text="Kullanılan proxy ip:",command=ipGoster)
button5.pack(pady=12,padx=10)





root.mainloop()



















