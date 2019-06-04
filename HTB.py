import tkinter
import requests
import base64


raiz = tkinter.Tk()
raiz.title("HTB")
raiz.geometry("300x100")
raiz.configure(background="medium spring green")



def accion():
    response = requests.post('https://www.hackthebox.eu/api/invite/generate')
    key = response.json()['data']['code']
    invited_code = base64.b64decode(key)
    entrada = tkinter.Entry(raiz)
    entrada.config(justify="center", width=40)
    entrada.insert(0,invited_code)
    entrada.pack()

boton = tkinter.Button(raiz, text="Invite Code", command=accion, bg='medium spring green')
boton.config(fg="black")
boton.pack()

raiz.mainloop()
