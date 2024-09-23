from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox 

#Funcionamiento
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_b(n):
    print(n)
    global operador
    operador=operador+n
    visor.delete(0,END)
    visor.insert(END,str(operador))


def borrar():
    visor.delete(0,END)
    global operador
    operador=""

def res():
    global operador
    result = str(eval(operador))
    visor.delete(0,END)
    visor.insert(END,str(result))
    operador = ""

def revisar_ch():
    x=0
    print("a")
    for c in cuadros_comida:
        if var_comida[x].get() != 0:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get()==0:
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x+=1

    x=0
    print("a")
    for c in cuadros_bebida:
        if var_bebida[x].get() != 0:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get()==0:
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set("0")
        x+=1
    
    x=0
    print("a")
    for c in cuadros_postres:
        if var_postres[x].get() != 0:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get()==0:
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set("0")
        x+=1

def total():
    subtotal_comida=0
    p = 0
    for cant in texto_comida:
        subtotal_comida=subtotal_comida+(float(cant.get()) * precios_comida[p])
        p+=1
    

    p = 0
    subtotal_bebida=0
    for cant in texto_bebida:
        subtotal_bebida=subtotal_bebida+(float(cant.get()) * precios_bebida[p])
        p+=1


    p = 0
    subtotal_postres=0
    for cant in texto_postres:
        subtotal_postres=subtotal_postres+(float(cant.get()) * precios_postres[p])
        p+=1
    subtotal = subtotal_bebida+subtotal_comida+subtotal_postres
    impuestos= subtotal* 0.21
    total = subtotal + impuestos

    var_costo_comida.set(str(round(subtotal_comida, 2)))
    var_costo_bebida.set(str(round(subtotal_bebida, 2)))
    var_costo_postres.set(str(round(subtotal_postres, 2)))
    var_subtotal.set(str(round(subtotal, 2)))
    var_impuestos.set(str(round(impuestos, 2)))
    var_total.set(str(round(total, 2)))

def recivo():
    texti_recivo.delete(1.0, END)
    num_recivo=f"N# - {random.randint(1000,9999)}"
    fecha= datetime.datetime.now()
    f_rec=f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texti_recivo.insert(END, f"Datos:\t{num_recivo}\t\t{f_rec}\n")
    texti_recivo.insert(END,F"*"*47+"\n")
    texti_recivo.insert(END, "Items\t\tCant.\tCoste\n")
    texti_recivo.insert(END, f"-"*60+"\n")
    x=0
    for comida in texto_comida:
        if comida.get() != "0":
            texti_recivo.insert(END,f"{lista_comida[x]}\t\t{comida.get()}\t {int(comida.get())*precios_comida[x]}\n")
            x+=1

    x=0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texti_recivo.insert(END,f"{lista_bebida[x]}\t\t{bebida.get()}\t {int(bebida.get())*precios_bebida[x]}\n")
            x+=1

    x=0
    for postres in texto_postres:
        if postres.get() != "0":
            texti_recivo.insert(END,f"{lista_postres[x]}\t\t{postres.get()}\t {int(postres.get())*precios_postres[x]}\n")
            x+=1
    texti_recivo.insert(END, f"-"*60+"\n")
    texti_recivo.insert(END,f"Coste comida: \t\t\t{var_costo_comida.get()}\n")
    texti_recivo.insert(END,f"Coste bebida: \t\t\t{var_costo_bebida.get()}\n")
    texti_recivo.insert(END,f"Coste postres: \t\t\t{var_costo_postres.get()}\n")
    texti_recivo.insert(END, f"-"*60+"\n")
    texti_recivo.insert(END,f"Coste subtotal: \t\t\t{var_subtotal.get()}\n")
    texti_recivo.insert(END,f"Coste impuestos: \t\t\t{var_impuestos.get()}\n")
    texti_recivo.insert(END,f"Coste total: \t\t\t{var_total.get()}\n")
    texti_recivo.insert(END,F"*"*47+"\n")

def guarda():
    info = texti_recivo.get(1.0,END)
    archivo=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    archivo.write(info)
    archivo.close()
    messagebox.showinfo("Información","Recivo guardado")

def reset():
    texti_recivo.delete(0.1,END)
    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_postres:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)
    
    for v in var_comida:
        v.set(0)
    for v in var_bebida:
        v.set(0)
    for v in var_postres:
        v.set(0)
    
    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postres.set("")
    var_subtotal.set("")
    var_impuestos.set("")
    var_total.set("")
#inicio
app = Tk()

#tamaño
app.geometry("1020x630+0+0")
app.resizable(0,0)

#titulo
app.title("Aplicación")

#Color de fondo
app.config(bg="grey")

#Panel
panel_superior = Frame(app, bd = 1, relief = FLAT)
panel_superior.pack(side=TOP)

#eqtiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema Facturación", fg="cyan", font=("Dosis",58),bg="grey", width=27)
etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo
panel_i = Frame(app, bd=1,relief=FLAT)
panel_i.pack(side=LEFT)

#costes
panel_costes = Frame(panel_i, bd=1, relief=FLAT, bg="grey")
panel_costes.pack(side=BOTTOM)

#comidas
panel_comidas = LabelFrame(panel_i, text = "Comida", font=("Dosis",28, "bold"), bd = 1, relief=FLAT, fg = "cyan")
panel_comidas.pack(side=LEFT)

#bebidas
panel_bebidas = LabelFrame(panel_i, text = "Bebida", font=("Dosis",28, "bold"), bd = 1, relief=FLAT, fg = "cyan")
panel_bebidas.pack(side=LEFT)

#postres
panel_postres = LabelFrame(panel_i, text = "Postres", font=("Dosis",28, "bold"), bd = 1, relief=FLAT, fg = "cyan")
panel_postres.pack(side=LEFT)

#panel derecha
panel_d = Frame(app, bd=1, relief=FLAT)
panel_d.pack(side=RIGHT)

#Calculadora
panel_calc = Frame(panel_d, bd=1, relief=FLAT, bg = "grey")
panel_calc.pack()

#Recivo
panel_recivo = Frame(panel_d, bd=1, relief=FLAT, bg = "grey")
panel_recivo.pack()

#boton
panel_boton = Frame(panel_d, bd=1, relief=FLAT, bg = "grey")
panel_boton.pack()

# lista productos
lista_comida=["Pollo","Pescado","Cerdo","Pizza"]
lista_bebida=["Agua","Vino","Zumo","Cacaolat"]
lista_postres=["Flan","Contesa", "Helado","Tarta"]
#generar comida
var_comida=[]
var_bebida=[]
var_postres=[]
cuadros_comida=[]
texto_comida=[]
cuadros_bebida=[]
texto_bebida=[]
cuadros_postres=[]
texto_postres=[]
#checkbotom
contador=0
for comida in lista_comida:
    #crear botones
    var_comida.append("")
    var_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(),font=("Dosis",10, "bold"),onvalue=1,offvalue=0, var=var_comida[contador],command=revisar_ch)
    comida.grid(row=contador, column=0, sticky=W)

    #crear cuadro de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador]= StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(panel_comidas,font=("Dosis",10, "bold"),bd=1,width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador +=1

contador=0
for bebida in lista_bebida:
    var_bebida.append("")
    var_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(),font=("Dosis",10, "bold"),onvalue=1,offvalue=0, var=var_bebida[contador],command=revisar_ch)
    bebida.grid(row=contador, column=0, sticky=W)

    #crear cuadro de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador]= StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(panel_bebidas,font=("Dosis",10, "bold"),bd=1,width=6, state=DISABLED, textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)

    contador +=1

contador=0
for postres in lista_postres:
    var_postres.append("")
    var_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(),font=("Dosis",10, "bold"),onvalue=1,offvalue=0, var=var_postres[contador],command=revisar_ch)
    postres.grid(row=contador, column=0, sticky=W)

    #crear cuadro de entrada
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[contador]= StringVar()
    texto_postres[contador].set("0")
    cuadros_postres[contador] = Entry(panel_postres,font=("Dosis",10, "bold"),bd=1,width=6, state=DISABLED, textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)

    contador +=1

#variables
var_costo_comida=StringVar()
var_costo_bebida=StringVar()
var_costo_postres=StringVar()
var_subtotal=StringVar()
var_impuestos=StringVar()
var_total=StringVar()

#etiquetas coste y campos entrada

etiqueta_costo_comida = Label(panel_costes,
                              text="Coste comida",
                              font=("Dosis",10, "bold"),
                              bg="grey",
                              fg="black")
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida=Entry(panel_costes,
                        text="Coste comida",
                        font=("Dosis",10, "bold"),
                        bg="grey",
                        state="readonly",
                        textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_comida = Label(panel_costes,
                              text="Coste postres",
                              font=("Dosis",10, "bold"),
                              bg="grey",
                              fg="black")
etiqueta_costo_comida.grid(row=2,column=0)

texto_costo_postres=Entry(panel_costes,
                        font=("Dosis",10, "bold"),
                        bg="grey",
                        state="readonly",
                        textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costes,
                              text="Coste bebidas",
                              font=("Dosis",10, "bold"),
                              bg="grey",
                              fg="black")
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida=Entry(panel_costes,
                        font=("Dosis",10, "bold"),
                        bg="grey",
                        state="readonly",
                        textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_subtotal = Label(panel_costes,
                              text="Subtotal",
                              font=("Dosis",10, "bold"),
                              bg="grey",
                              fg="black")
etiqueta_subtotal.grid(row=0,column=3)

texto_subtotal=Entry(panel_costes,
                        font=("Dosis",10, "bold"),
                        bg="grey",
                        state="readonly",
                        textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=4, padx=41)

etiqueta_impuestos = Label(panel_costes,
                              text="Impuestos",
                              font=("Dosis",10, "bold"),
                              bg="grey",
                              fg="black")
etiqueta_impuestos.grid(row=1,column=3)

texto_impuestos=Entry(panel_costes,
                        font=("Dosis",10, "bold"),
                        bg="grey",
                        state="readonly",
                        textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=4, padx=41)

etiqueta_total = Label(panel_costes,
                              text="Total",
                              font=("Dosis",10, "bold"),
                              bg="grey",
                              fg="black")
etiqueta_total.grid(row=2,column=3)

texto_total=Entry(panel_costes,
                        font=("Dosis",10, "bold"),
                        bg="grey",
                        state="readonly",
                        textvariable=var_total)
texto_total.grid(row=2, column=4, padx=41)

#botones
botones=["Total","Recibo","Guardar","Resetear"]
botones_creados = []
columna = 0
for boton in botones:
    boton = Button(panel_boton, text=boton.title(),font=("Dosis",10, "bold"), fg="white", bg="black",bd=1,width=9 )
    botones_creados.append(boton)
    boton.grid(row=0,column=columna)
    columna+=1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recivo)
botones_creados[2].config(command=guarda)
botones_creados[3].config(command=reset)
#area recivo
texti_recivo=Text(panel_recivo,font=("Dosis",10, "bold"),bd=1,width=42,height=10)
texti_recivo.grid(row=0,column=0)

#calculadora
visor = Entry(panel_calc,font=("Dosis",10, "bold"),bd=1, width=32)
visor.grid(row=0,column=0,columnspan=4)

b_calc=["7","8","9","+","4","5","6","-","1","2","3","*","CE","Borrar","0","/"]
b_gua=[]
fila=1
columna=0
for b in b_calc:
    b=Button(panel_calc,text=b.title(),font=("Dosis",10, "bold"),fg="white",bg="black",bd=2,width=8)
    b.grid(row=fila,column=columna)
    columna+=1

    if columna ==4:
        fila+=1
        columna=0

    b_gua.append(b)

conta=0

b_gua[0].config(command=lambda : click_b("7"))
b_gua[1].config(command=lambda : click_b("8"))
b_gua[2].config(command=lambda : click_b("9"))
b_gua[3].config(command=lambda : click_b("+"))
b_gua[4].config(command=lambda : click_b("4"))
b_gua[5].config(command=lambda : click_b("5"))
b_gua[6].config(command=lambda : click_b("6"))
b_gua[7].config(command=lambda : click_b("-"))
b_gua[8].config(command=lambda : click_b("1"))
b_gua[9].config(command=lambda : click_b("2"))
b_gua[10].config(command=lambda : click_b("3"))
b_gua[11].config(command=lambda : click_b("*"))
b_gua[12].config(command=lambda : res())
b_gua[13].config(command=lambda : borrar())
b_gua[14].config(command=lambda : click_b("0"))
b_gua[15].config(command=lambda : click_b("/"))


#evitar cierre
app.mainloop()