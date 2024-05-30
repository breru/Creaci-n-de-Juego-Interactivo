from random import choice

def elegir_palabra(lista_palabras):
    palabra_aleatoria = choice(lista_palabras)
    return palabra_aleatoria.upper()

lista_palabra_oculta = ["almohada" , "guitarra" , "monitor" , "mate" , "espejo" , "tambor" , "telefono" , "sol" , "frambuesa" , "mochila" , "casa" , "ladrillo"]

palabra_oculta = elegir_palabra(lista_palabra_oculta)

#vidas = 6
#aciertos = 0

print("*~*~*~*~*~*~*~*~*~*~*~*")

print("Bienvenidx al Juego.")

print("*~*~*~*~*~*~*~*~*~*~*~*")

print("Deberás adivinar la palabra oculta. \n\n Comencemos")

#letra_a_adivinar = set(palabra_oculta)

#lista_incorrectas []
#if letra_seleccionada (no está):
#   lista_incorrectas.append(letra_seleccionada)

#if letra_seleccionada in lista_incorrectas:
#   print("Esa letra ya fue elegida y no se encuentra en la palabra")
#(no tiene que restar vida)

#while vidas >=1 and aciertos < len(letra_a_adivinar):
#   pass
      

