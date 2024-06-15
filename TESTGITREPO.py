import random
import string
import pyfiglet
from colorama import *
init()

text=pyfiglet.figlet_format(text="TEST",
                            font="big") 
print(Fore.GREEN + text)

def generate_secure_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a secure random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print(Fore.YELLOW + "        [=] Generador de Contraseñas Seguras [=]\n")
    
    while True:
        # Solicitar la longitud de la contraseña
        while True:
            try:
                length = int(input("[+] Introduce la longitud de la contraseña (entre 8 y 64 caracteres): "))
                if 8 <= length <= 64:
                    break
                else:
                    print("Por favor, introduce un número entre 8 y 64.\n")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número.\n")
        
        # Generar y mostrar la contraseña segura
        secure_password = generate_secure_password(length)
        print(Fore.GREEN +"[=] Contraseña segura generada:", secure_password)
        
        # Preguntar si el usuario desea generar otra contraseña o salir
        while True:
            choice = input(Fore.YELLOW +"[+] ¿Deseas generar otra contraseña? (s/n): ").lower()
            if choice in ('s', 'n'):
                break
            else:
                print("Por favor, introduce 's' para sí o 'n' para no.")
        
        if choice == 'n':
            print("[+_+] Gracias por usar WRD-SECURE.\n")
            print(Fore.RED +"     Hecho por Rodrigo Lopez")
            break

if __name__ == "__main__":
    main()