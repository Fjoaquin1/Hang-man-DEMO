import getpass
import pygame
import sys

pygame.init()

# Pedir al usuario que ingrese la palabra a adivinar.
word = getpass.getpass("Ingrese la palabra a adivinar: ")
# Contador de errores.
errors = 0
# Letras adivinadas.
guessed_letters = []
game_over = False
correct_guesses = 0
hidden_word = "_" * len(word)

# Inicializar la ventana de juego.
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ahoracado en Pygame")

# Establecer los colores.
black = (0, 0, 0)
white = (255, 255, 255)

# Establecer la fuente.
font = pygame.font.Font(None, 24)

# Establecer las coordenadas para dibujar las partes del cuerpo.
head_x = 200
head_y = 50
body_x = 200
body_y = 100
arm1_x = 150
arm1_y = 100
arm2_x = 250
arm2_y = 100
leg1_x = 150
leg1_y = 150
leg2_x = 250
leg2_y = 150

# Crear una superficie para dibujar las partes del cuerpo.
body_surface = pygame.Surface((400, 300))
body_surface.fill(black)

while errors < 7 and not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Pedir al usuario que ingrese una letra.
    letter = input("Ingrese una letra: ")
    if len(letter) != 1:
        print("Ingrese solo una letra: ")
    if letter in guessed_letters:
        print("Letra ya ingresada, intenta con otra.")
    else:
        guessed_letters.append(letter)
    # Verifica si la letra esta en la palabra.
        if letter in word:
            # Si la letra esta en la palabra, se reemplaza por el guion.
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word = hidden_word[:i] + letter + hidden_word[i+1:]
                    correct_guesses += 1
            print(hidden_word)
            if correct_guesses == len(word):
                game_over = True
                print("¡Felicitaciones! Adivinaste la palabra.")
                break
        else:
            # Si la letra no esta en la palabra, suma 1 en el contador de errores.
            errors += 1
        
        
        
        if errors == 1:
            text = font.render("O", True, white)
            body_surface.blit(text, (head_x, head_y))
            

        elif errors == 2:
            text = font.render("|", True, white)

            body_surface.blit(text, (body_x, body_y))
            

        elif errors == 3:
            text = font.render("/", True, white)
            body_surface.blit(text, (arm1_x, arm1_y))
            

        elif errors == 4:
            text = font.render("\\", True, white)
            body_surface.blit(text, (arm2_x, arm2_y))


        elif errors == 5:
            text = font.render("/", True, white)
            body_surface.blit(text, (leg1_x, leg1_y))
            

        elif errors == 6:
            text = font.render("\\", True, white)
            body_surface.blit(text, (leg2_x, leg2_y))
            

        # Si el usario se equivoca demasiadas veces, mostra mensaje  de derrota.
        elif errors == 7:
            print("¡Perdiste! La palabra correcta era: ", word)


        window.blit(body_surface, (0, 0))
        pygame.display.update()