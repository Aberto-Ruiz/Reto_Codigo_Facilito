def main():
    # Solicitar al usuario que ingrese su información
    nombres = input("Ingrese su(s) nombre(s): ")
    apellidos = input("Ingrese su(s) apellido(s): ")
    telefono = input("Ingrese su número de teléfono: ")
    correo = input("Ingrese su correo electrónico: ")

    # Construir el mensaje de bienvenida
    mensaje_bienvenida = f"Hola {nombres} {apellidos}, en breve recibirás un correo a {correo}"

    # Imprimir el mensaje de bienvenida
    print(mensaje_bienvenida)

if __name__ == "__main__":
    main()