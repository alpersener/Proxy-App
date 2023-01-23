import os
import threading
import time
from tkinter import messagebox
import requests
import winreg
import csv
import concurrent.futures
import tkinter as tk
import customtkinter
from urllib.request import urlopen
import urllib
import socket
from bs4 import BeautifulSoup
from tkinter import *


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
#FONKSİYON KISIMLARI

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
    ip_dict = urllib.request.getproxies()
    if ip_dict:
        ip = ip_dict['http']
        msg = messagebox.showinfo("IP:", ip)
    else:
        msg = messagebox.showinfo("HATA!", "Proxy ayarları açık değil.")

def get_key(name):
    return winreg.QueryValueEx(INTERNET_SETTINGS, name)[0]
def siradakiIp():
    ip_list = []
    with open("proxylistv2.csv", 'r') as f:
        reader = csv.reader(f)
        for satir in reader:
            ip_list.append(satir[0])
    sonuc = messagebox.askyesno(title="UYARI!", message="Diğer IP'ye geçmek istediğinize emin misiniz?")
    if (sonuc == True):
        current_ip = get_key('ProxyServer')
        for ip in ip_list:
            if current_ip == ip:
                current_ip_index = ip_list.index(ip)
                break
        if not current_ip_index:
            current_ip_index = 0
        next_ip_index = current_ip_index + 1

        if next_ip_index >= len(ip_list):
            next_ip_index = 0
        next_ip = ip_list[next_ip_index]
        set_key('ProxyEnable', 1)
        set_key('ProxyOverride', u'*.local;<local>')
        set_key('ProxyServer', next_ip)
        messagebox.showinfo("Başarılı!", message="IP adresi değiştirildi.")






def ac():
    yeni_pencere = tk.Toplevel(root)
    yeni_pencere.title("Yeni pencere")
    yeni_pencere.geometry("400x500")
    def veriCek():
        url = entry.get()
        sayfa_icerigi = requests.get(url)
        soup = BeautifulSoup(sayfa_icerigi.content, "html.parser")
        sonuclar = soup.find_all('div', class_='card-body')
        for sonuc in sonuclar:
            liste.insert(tk.END, sonuc.text)
    liste = tk.Listbox(yeni_pencere)
    liste.pack(fill="both")
    entry=tk.Entry(yeni_pencere)
    entry.pack()
    dugme=tk.Button(yeni_pencere, text='Veri Çek', command=veriCek)
    dugme.pack()


def getContent():
  global veri_cekici_pencere
  veri_cekici_pencere = customtkinter.CTkToplevel()
  veri_cekici_pencere.title('Veri Çekici')
  global url_giris
  global listeleme

def zamanlamaIp():
    while True:
        time.sleep(300)
        siradakiIp()

thread = threading.Thread(target=zamanlamaIp)
thread.start()


#---------------------------------------------------------------------------------------------------------------
#GUI KISIMLARI


customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("500x350")
checkbox_var=tk.IntVar()

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=50,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="PROXY",font=("Roboto",44))
label.pack(pady=12,padx=10)



button3 = tk.Button(master=frame,text="PROXY AÇIK",bg="green")
button4=tk.Button(master=frame,text="PROXY KAPALI",bg="red")

button=customtkinter.CTkButton(master=frame,text="Proxy Aç",command=proxyAc)
button.pack(pady=12,padx=10)

button2=customtkinter.CTkButton(master=frame,text="Proxy kapat",command=proxyKapat)
button2.pack(pady=12,padx=10)

#checkbox=customtkinter.CTkCheckBox(master=frame,text="Timer",command="")
#checkbox.pack(pady=12,padx=10)

button5=customtkinter.CTkButton(master=frame,text="Kullanılan proxy ip:",command=ipGoster)
button5.pack(pady=12,padx=10)

button6=customtkinter.CTkButton(master=frame,text="Sıradaki IP geç",command=siradakiIp)
button6.pack(pady=12,padx=10)

button7=customtkinter.CTkButton(master=frame,text="getContent",command=ac)
button7.pack(pady=12,padx=10)






root.mainloop()


