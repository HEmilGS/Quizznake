#Programa de aprendizaje con snake
""" iniciado el 29 de Agosto del 2022

    Snake
    cambio final 18/10/2022
"""


#Librerias


from pydoc import doc
import turtle
import time
import random
from tqdm import tqdm
import winsound
import tkinter 
import random
from datetime import datetime


def iniciar_juego():
    menu_principal.destroy()
      
      
def validar_score(puntaje, nombre, EN):
    nombreu=nombre.get()
    fecha = datetime.now()
    fecha=str(fecha)
    mejores_puntajes = open('proyecto_final\Mejores_puntajes.txt','a')
    mejores_puntajes.writelines(f'\nFecha del juego: {fecha}')
    mejores_puntajes.writelines(f'\nPuntaje conseguido por: {nombreu} ')
    mejores_puntajes.writelines(f'\nPuntaje alcanzado: {puntaje}')
    mejores_puntajes.close
    EN.destroy()



def archivos(pregunta_a, respuesta_u, respuesta_c):
    doc_preguntas=open("proyecto_final\Doc_preguntas.txt", "a")
    fecha=datetime.now()
    fecha=str(fecha)
    doc_preguntas.write("\n ")
    doc_preguntas.write("Fecha de juego: " + fecha)
    doc_preguntas.write("\n Pregunta asignada: "+ pregunta_a)
    doc_preguntas.write("\n Respuesta del usuario: "+ respuesta_u)
    doc_preguntas.write("\n Respuesta correcta: "+ respuesta_c + "\n")
    doc_preguntas.close

    

def ventana_topscore():
    menu_principal.destroy()
    doc_preguntas=open("proyecto_final\mejores_puntajes.txt", "r")
    ventana_score=tkinter.Tk()
    ventana_score.geometry("600x400")
    titulo_score=tkinter.Label(ventana_score, text="Mejroes puntajes:")
    espaciador=tkinter.Label(ventana_score, text=" ")
    titulo_score.config(font=("Helvetica",20))
    scores=doc_preguntas.readlines()
    scoresl=tkinter.Label(ventana_score, text=scores)
    titulo_score.pack()
    scoresl.pack()
    turtle.bye()
    



def validar_respuestas(caja_respuestaf, preguntasf,respuestasf, indicef, ventana_practicaf, score, high_score, segmentose):
    
    respuesta_usuario=caja_respuestaf.get()
    respuesta_usuario= respuesta_usuario.lower()
    pregunta_asignada = preguntasf[indicef]
    pregunta_a=pregunta_asignada
    respuesta_u=respuesta_usuario
    respuesta_c=respuestasf[indicef]
    boton_siguiente=tkinter.Button(ventana_practicaf, text="Siguiente pregunta", bg="green", command=lambda: ventana_preguntas(score, high_score, segmentose))
    if respuesta_usuario == respuestasf[indicef]:
        anuncioc=tkinter.Label(ventana_practicaf, text="¡Respuesta correcta, sal de esta ventana y continúa! \n o puedes seguir practicando")
        anuncioc.pack()
        boton_siguiente.pack()

        archivos(pregunta_a, respuesta_u, respuesta_c)

        snake(score, high_score, [])
    else:
        anuncioi=tkinter.Label(ventana_practicaf, text="¡Respuesta incorrecta!, intenta de nuevo o sigue practicando")
        anuncioi.pack()
        boton_siguiente.pack()
        print(pregunta_a)
        print(respuesta_u)
        print(respuesta_c)
        archivos(pregunta_a, respuesta_u, respuesta_c)
        snake(0,high_score,[])    

        



#Definicion de ventanas externas
def ventana_preguntas(scoree, high_score, segmentose):  
    #creacion de listas con preguntas y respuestas
    #Listas de preguntas
    preguntas = ["¿Cuanto es la raiz de 121?","¿Cuanto es 1^9?","¿Como se llama el triangulo de lados igiuales?","¿Tiene centro de simetría un triángulo equilátero?","¿Cual es la probabilidad de sacar un número sobre mil en una extracción?","¿Cuál es la grafica del trinomio de segundo grado?","¿Cuál es el valor de la potencia de exponente cero?","¿Aproxima el número 58 a la decena?","¿Escribe el número ordinal trigésimo quinto en cifras?","¿Qué cantidad expresa el número romano VII?","¿Qué número resulta si divides 56 entre 7?","¿Cómo escribirías en cifras seiscientos veinticinco mil doscientos dos?","¿Si en una carrera vas tres puestos por detrás del vigésimo segundo, ¿en qué puesto vas? ?","¿ ¿Verdadero o falso? Una división entera es aquella en la que el resto es cero?","¿Un perro pesa 20 kilos y un cachorro pesa 10 kilos menos que él, ¿cuánto pesa la cría? ?","¿Cómo se llama el polígono de siete lado?","¿Cuál es el nombre del triángulo que tiene dos lados iguales y uno desigual?","¿Cuántos metros es un hectómetro?","¿Expresa 7 kg y 670 g en gramos?","¿Cálculo mental rápido: cuánto es 12 menos 7?","¿Cálculo mental rápido: cuánto es 14000 entre 10?","¿Escribe con números esta fracción: cinco séptimos?","¿Cálculo mental rápido: cuánto es 6x8 menos cuatro?"]
    respuestas = ["11","1","equilatero","no","1/1000","parabola","Uno","60","35","7","9","625202","decimonoveno","falso","10","heptagono","isosceles","100","7670","5","1400","5/7","44"]
    indice=random.randint(0,22) 
    ventana_practica=tkinter.Tk()
    ventana_practica.geometry("600x400")
    instruccion_practica=tkinter.Label(ventana_practica, text="Contesta las siguientes preguntas")
    espaciador=tkinter.Label(ventana_practica, text=" \n")
    instruccion_practica.config(font=("Helvetica",20))
    etiqueta_pregunta=tkinter.Label(ventana_practica, text=preguntas[indice])
    etiqueta_pregunta.config(font=("Helvetica", 15))
    caja_respuesta=tkinter.Entry(ventana_practica)
    boton_enviar=tkinter.Button(ventana_practica, text="Revisar respuesta", bg="green", command=lambda: validar_respuestas(caja_respuesta,preguntas, respuestas,indice, ventana_practica, scoree, high_score,segmentose))
    boton_salir=tkinter.Button(ventana_practica,text="salir", bg="green", command=lambda: ventana_practica.destroy())
    

    instruccion_practica.pack()
    espaciador.pack()
    etiqueta_pregunta.pack()
    espaciador.pack()
    caja_respuesta.pack()

    espaciador.pack()
    boton_salir.place(x=500, y=350)
    boton_enviar.pack()
    


    ventana_practica.mainloop()


def snake(score, high_score, segmentos):

    cabeza.goto(0,0)
    cabeza.direction = "stop"
    segmentos.clear()

    while True:
        
        wn.update()
        
        #Bordes #importante 
        if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
            winsound.Beep(1000,400)
            winsound.Beep(1500,400)
            for segmento in segmentos:
                segmento.goto(1000,1000)   
            ventana_preguntas(score, high_score, segmentos)
            
            #Esconder segmento
            for segmento in segmentos:
                segmento.goto(2000,2000)
                
            #Limpiar lista de segmentos
                segmentos.clear()
            
            #Reset marcador
            score = 0
            texto.clear()   
            texto.write("Score: {}    High Score: {}".format(score,high_score), align = "center", font = ("Courier", 10, "normal"))
                
        #Colision comida
        if cabeza.distance(comida) < 20:
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            comida.goto(x,y)
            
            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square")
            nuevo_segmento.color("grey")
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento)
            winsound.Beep(3200,400)
            #Aumentar marcador
            score += 1
        
        
        if score > high_score:
            high_score = score
            
            texto.clear()   
            texto.write("Score: {}    High Score: {}".format(score,high_score), align = "center", font = ("Courier", 10, "normal"))

        
        #Movimiento del cuerpo
        totalSeg = len(segmentos)
        for index in range(totalSeg -1, 0, -1):
            x = segmentos[index - 1].xcor()
            y = segmentos[index - 1].ycor()
            segmentos[index].goto(x,y) 
            
        if totalSeg > 0 :
            x = cabeza.xcor()
            y = cabeza.ycor()
            segmentos[0].goto(x,y)
            
            
            
        mov()
        
        #Colisiones con el cuerpo
        for segmento in segmentos:
            if segmento.distance(cabeza) < 20: 
                winsound.Beep(1000,400)
                winsound.Beep(1500,400)
                for segmento in segmentos:
                    segmento.goto(1000,1000) 
                if score>1:
                    entrada_nombre=tkinter.Tk()
                    entrada_nombre.geometry("600x400")
                    nombre=tkinter.Entry(entrada_nombre)
                    inst=tkinter.Label(entrada_nombre, text="Felicidades, rompiste tu record! \n ingresa tu nombre de usuario")
                    inst.config(font=("Helvetica",20))
                    boton_enviars=tkinter.Button(entrada_nombre, text="Enviar score", bg="green", command=lambda: validar_score(score, nombre, entrada_nombre))
                    
                    inst.pack()
                    nombre.pack()
                    boton_enviars.pack()

                ventana_preguntas(score, high_score, segmentos)
               
        time.sleep(posponer)
    turtle.mainloop()
    turtle.bye
   


    

#Creacion y configuracion de elementos del menu principal
menu_principal=tkinter.Tk()
menu_principal.geometry("600x400")
menu_principal.title("Menú principal - Snake")

logo=tkinter.PhotoImage(file="proyecto_final\logoN.png")
mostrar_logo=tkinter.Label(menu_principal, image=logo)

saludo=tkinter.Label(menu_principal, text="Bienvenido!")
saludo.config(font=("Helvetica",50))
instruccion=tkinter.Label(menu_principal, text="Elige una opcion para comenzar")
instruccion.config(font=("Helvetica", 15))




practicar=tkinter.Button(menu_principal, text="Practicar", bg="green", padx=20,pady=10,command=lambda:ventana_preguntas(0,0,[]))


jugar=tkinter.Button(menu_principal, text="Jugar", bg="green", padx=20,pady=10, command=lambda: iniciar_juego())

score=tkinter.Button(menu_principal, text="Top score", bg="green", padx=20,pady=10,command=lambda:ventana_topscore())


#llamada de objetos
mostrar_logo.pack()
saludo.pack()
instruccion.pack()
practicar.place(x=200, y=250)
jugar.place(x=315, y=250)
score.place(x=250, y=300)



menu_principal.mainloop()




#Marcador
posponer = 0.1
score =0
high_score=0


#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

segmentos=[]

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("cyan")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0    High Score: 0", align = "center", font = ("Courier", 10, "normal"))



#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"
    
    
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
#Teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")

snake(0,0,[])

