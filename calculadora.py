import tkinter as tk
import math
from tkinter import END, messagebox, ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=200, height=200)
        self.title("Practice 2")
        self.entry_display=tk.Entry(self, width=50)
        self.entry_display.place(x=10,y=10)
        
        self.entry_bin=tk.Entry(self, width=40, state="readonly")
        self.entry_bin.place(x=50,y=70)
        self.label_bin=tk.Label(self, text="BIN")
        self.label_bin.place(x=10,y=70)
        self.entry_oct=tk.Entry(self, width=40, state="readonly")
        self.entry_oct.place(x=50,y=90)
        self.label_oct=tk.Label(self, text="OCT")
        self.label_oct.place(x=10,y=90)
        self.entry_dec=tk.Entry(self, width=40, state="readonly")
        self.entry_dec.place(x=50,y=110)
        self.label_dec=tk.Label(self, text="DEC")
        self.label_dec.place(x=10,y=110)
        self.entry_hex=tk.Entry(self, width=40, state="readonly")
        self.entry_hex.place(x=50,y=130)
        self.label_hex=tk.Label(self, text="HEX")
        self.label_hex.place(x=10,y=130)

        self.ban_dec=True
        self.ban_bin=False
        self.ban_oct=False
        self.ban_hex=False
        self.ban_punto=False

        self.btpoint=tk.Button(self, text=".", command=lambda:self.Enviar_display("."))
        self.btpoint.place(x=90,y=310)
        self.btMasMenos=tk.Button(self, text="+/-", command=self.cambiar_signo)
        self.btMasMenos.place(x=40,y=310)
        self.bt0=tk.Button(self, text="0", command=lambda:self.Enviar_display("0"))
        self.bt0.place(x=70,y=310)
        self.bt1=tk.Button(self, text="1", command=lambda:self.Enviar_display("1"))
        self.bt1.place(x=40,y=280)
        self.bt2=tk.Button(self, text="2", command=lambda:self.Enviar_display("2"))
        self.bt2.place(x=60,y=280)
        self.bt3=tk.Button(self, text="3", command=lambda:self.Enviar_display("3"))
        self.bt3.place(x=80,y=280)
        self.bt4=tk.Button(self, text="4", command=lambda:self.Enviar_display("4"))
        self.bt4.place(x=40,y=250)
        self.bt5=tk.Button(self, text="5", command=lambda:self.Enviar_display("5"))
        self.bt5.place(x=60,y=250)
        self.bt6=tk.Button(self, text="6", command=lambda:self.Enviar_display("6"))
        self.bt6.place(x=80,y=250)
        self.bt7=tk.Button(self, text="7", command=lambda:self.Enviar_display("7"))
        self.bt7.place(x=40,y=220)
        self.bt8=tk.Button(self, text="8", command=lambda:self.Enviar_display("8"))
        self.bt8.place(x=60,y=220)
        self.bt9=tk.Button(self, text="9", command=lambda:self.Enviar_display("9"))
        self.bt9.place(x=80,y=220)

        self.btSuma=tk.Button(self, text="+", command=lambda:self.Operador("+") )
        self.btSuma.place(x=100,y=280)
        self.btResta=tk.Button(self, text="-", command=lambda:self.Operador("-"))
        self.btResta.place(x=100,y=250)
        self.btResultado=tk.Button(self, text="=", command=lambda:self.Operacion())
        self.btResultado.place(x=106,y=310)
        self.btMultiplicacion=tk.Button(self, text="*", command=lambda: self.Operador("*"))
        self.btMultiplicacion.place(x=100,y=220)
        self.btDivision=tk.Button(self, text="/", command=lambda: self.Operador("/"))
        self.btDivision.place(x=110,y=190)
        self.btExponente=tk.Button(self, text="^", command=lambda: self.Operador("^"))
        self.btExponente.place(x=60,y=190)

        self.btRaiz=tk.Button(self, text="\u221A", command=lambda: self.Operador("\u221A"))
        self.btRaiz.place(x=40,y=160)
        self.btPorcentaje=tk.Button(self, text="%", command=self.aplicar_porcentaje)
        self.btPorcentaje.place(x=60,y=160)
        self.btLimpiar=tk.Button(self, text="CE", command=self.clean_screen)
        self.btLimpiar.place(x=83,y=160)
        self.btBack=tk.Button(self, text="<-", command=self.backspace)
        self.btBack.place(x=110,y=160)
        self.btTangente=tk.Button(self, text="tan", command=lambda: self.Operador("tan"))
        self.btTangente.place(x=80,y=190)
        self.btFactorial=tk.Button(self, text="n!", command=lambda: self.Operador("!"))
        self.btFactorial.place(x=40,y=190)

        self.btA=tk.Button(self, text="A", command=lambda:self.Enviar_display("A"))
        self.btA.place(x=20,y=160)
        self.btB=tk.Button(self, text="B", command=lambda:self.Enviar_display("B"))
        self.btB.place(x=20,y=190)
        self.btC=tk.Button(self, text="C", command=lambda:self.Enviar_display("C"))
        self.btC.place(x=20,y=220)
        self.btD=tk.Button(self, text="D", command=lambda:self.Enviar_display("D"))
        self.btD.place(x=20,y=250)
        self.btE=tk.Button(self, text="E", command=lambda:self.Enviar_display("E"))
        self.btE.place(x=20,y=280)
        self.btF=tk.Button(self, text="F", command=lambda:self.Enviar_display("F"))
        self.btF.place(x=20,y=310)

        self.numero_aux=0
        self.oper=""
        self.reset_display=False

    def clear_conversions(self):
        for entry in (self.entry_bin, self.entry_oct, self.entry_dec, self.entry_hex):
            entry.config(state="normal")
            entry.delete(0, END)
            entry.config(state="disabled")

    def clean_screen(self):
        self.entry_display.config(state="normal")
        self.entry_display.delete(0, END)
        self.entry_display.config(state="disabled")
        self.numero_aux = 0
        self.oper = ""
        self.reset_display = False
        self.clear_conversions()

    def backspace(self):
        self.entry_display.config(state="normal")
        texto = self.entry_display.get()
        if texto:
            self.entry_display.delete(len(texto) - 1, END)
        self.entry_display.config(state="disabled")
        self.actualizar_sistemas(self.entry_display.get())

    def Enviar_display(self,numero):
        self.entry_display.config(state="normal")
        display=self.entry_display.get()

        if self.reset_display:
            display = ""
            self.reset_display = False
        else:
            display = self.entry_display.get()

        if numero == ".":
            if "." in display:
                self.entry_display.config(state="disabled")
                return
            if not display:
                display = "0"

        self.entry_display.delete(0,END)
        self.entry_display.insert(0,display + str(numero))
        self.entry_display.config(state="disabled")

        self.actualizar_sistemas(self.entry_display.get())

    def aplicar_porcentaje(self):
        valor = self.entry_display.get().strip()
        if not valor:
            return

        try:
            numero = float(valor)
        except ValueError:
            return

        resultado = numero / 100
        self.entry_display.config(state="normal")
        self.entry_display.delete(0, END)
        self.entry_display.insert(0, str(resultado))
        self.entry_display.config(state="disabled")
        self.actualizar_sistemas(self.entry_display.get())

    def cambiar_signo(self):
        valor = self.entry_display.get().strip()
        if not valor:
            return

        resultado = valor[1:] if valor.startswith("-") else "-" + valor
        self.entry_display.config(state="normal")
        self.entry_display.delete(0, END)
        self.entry_display.insert(0, resultado)
        self.entry_display.config(state="disabled")
        self.actualizar_sistemas(resultado)

    def Operador(self, oper):
        valor = self.entry_display.get().strip()
        if not valor:
            if oper in ("tan", "\u221A", "!"):
                self.oper = oper
            return

        try:
            self.numero_aux = float(valor)
        except (OverflowError, ValueError):
            self.entry_display.config(state="normal")
            self.entry_display.delete(0,END)
            self.entry_display.insert(0,"Overflow")
            self.entry_display.config(state="disabled")
            self.clear_conversions()
            self.reset_display=True
            return

        self.oper = oper
        self.entry_display.config(state="normal")
        self.entry_display.delete(0,END)
        self.entry_display.config(state="disabled")
        self.reset_display=True

    def Operacion(self):
        try:
            r=0
            if self.oper=="*":
                r=float(self.numero_aux)*float(self.entry_display.get())
            elif self.oper=="+":
                r=float(self.numero_aux)+float(self.entry_display.get())
            elif self.oper=="/":
                r=float(self.numero_aux)/float(self.entry_display.get())
            elif self.oper=="-":
                r=float(self.numero_aux)-float(self.entry_display.get())
            elif self.oper=="^":
                r=float(self.numero_aux)**float(self.entry_display.get())
            elif self.oper=="%":
                r=(float(self.numero_aux) * float(self.entry_display.get())) / 100
            elif self.oper=="\u221A":
                valor = self.entry_display.get() or self.numero_aux
                r=float(valor)**0.5
            elif self.oper=="tan":
                valor = self.entry_display.get() or self.numero_aux
                r=math.tan(math.radians(float(valor)))
            elif self.oper=="!":
                valor = self.entry_display.get() or self.numero_aux
                r=math.factorial(int(valor))
            if isinstance(r, float) and not math.isfinite(r):
                raise OverflowError
        except (OverflowError, ValueError, ZeroDivisionError):
            self.entry_display.config(state="normal")
            self.entry_display.delete(0,END)
            self.entry_display.insert(0,"Overflow")
            self.entry_display.config(state="disabled")
            self.clear_conversions()
            self.reset_display=True
            return

        self.entry_display.config(state="normal")
        self.entry_display.delete(0,END)
        self.entry_display.insert(0,str(r))
        self.entry_display.config(state="disabled")
        self.reset_display=True
     
    
    def actualizar_sistemas(self, numero):
        print(self.ban_punto)
        if self.ban_dec:
            try:
                if self.ban_punto==False:
                    self.entry_bin.config(state="normal")
                    self.entry_bin.delete(0,END)
                    self.entry_bin.insert(0,self.dec_bin(numero))
                    self.entry_bin.config(state="disabled")

                    self.entry_oct.config(state="normal")
                    self.entry_oct.delete(0,END)
                    self.entry_oct.insert(0,self.dec_oct(numero))
                    self.entry_oct.config(state="disabled")

                    self.entry_hex.config(state="normal")
                    self.entry_hex.delete(0,END)
                    self.entry_hex.insert(0,self.dec_hex(numero))
                    self.entry_hex.config(state="disabled")

                self.entry_dec.config(state="normal")
                self.entry_dec.delete(0,END)
                self.entry_dec.insert(0,self.entry_display.get())
                self.entry_dec.config(state="disabled")
            except:
                print("")
        elif self.ban_bin:

            try:
                if self.ban_punto==False:
                    self.entry_bin.config(state="normal")
                    self.entry_bin.delete(0,END)
                    self.entry_bin.insert(0,self.entry_display.get())
                    self.entry_bin.config(state="disabled")

                    self.entry_dec.config(state="normal")
                    self.entry_dec.delete(0,END)
                    self.entry_dec.insert(0,self.bin_dec(numero))
                    self.entry_dec.config(state="disabled")

                    self.entry_oct.config(state="normal")
                    self.entry_oct.delete(0,END)
                    self.entry_oct.insert(0,self.bin_oct(self.bin_dec(numero)))
                    self.entry_oct.config(state="disabled")

                    self.entry_hex.config(state="normal")
                    self.entry_hex.delete(0,END)
                    self.entry_hex.insert(0,self.bin_hex(self.bin_dec(numero)))
                    self.entry_hex.config(state="disabled")
            except:
                print("")
    
    def dec_bin(self, numero):
        if "." in numero:
            self.ban_punto=True
            return "Error"
        else:
            self.ban_punto=False
            return bin(int(numero)).replace("0b","")
    
    def dec_oct(self, numero):
        if "." in numero:
            self.ban_punto=True
            return "Error"
        else:
            self.ban_punto=False
            return oct(int(numero)).replace("0o","")

    def dec_hex(self, numero):
        if "." in numero:
            self.ban_punto=True
            return "Error"
        else:
            self.ban_punto=False
            return hex(int(numero)).replace("0x","")
    
    def bin_dec(self, numero):
        if "." in numero:
            self.ban_punto=True
            return "Error"
        else:
            self.ban_punto=False
            return str(int(numero,2))
    
    def bin_oct(self, numero):
        if "." in numero:
            self.ban_punto=True
            return "Error"
        else:
            self.ban_punto=False
            return oct(int(numero)).replace("0o","")

    def bin_hex(self, numero):
        if "." in numero:
            self.ban_punto=True
            return "Error"
        else:
            self.ban_punto=False
            return hex(int(numero)).replace("0x","")

if __name__=="__main__":
        app=App()
        app.mainloop()