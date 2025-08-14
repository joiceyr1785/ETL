def asteriscos(func):
        def envoltura():
            print('*' * 10)
            func()
            print('*' * 10)
        return envoltura

@asteriscos
def saludo():
        print("Hola, mundo!")

#saludo = asteriscos(saludo)
saludo()

