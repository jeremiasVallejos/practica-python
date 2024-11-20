lenguajes = ["Python", "JavaScript", "Java", "C++", "Ruby"]
sistemas_operativos = ["Windows", "Linux", "macOS", "Android", "iOS"]
stacks_tecnologicos = ["MERN", "LAMP", "MEAN", "Django", "Spring Boot"]

while True:
    print("\nMenú de opciones:")
    print("1. Visualizar lenguajes de programación")
    print("2. Visualizar sistemas operativos")
    print("3. Visualizar stacks tecnológicos")
    print("0. Salir")
    
    opcion = input("Por favor, selecciona una opción (0-3): ")
    
    if opcion == "1":
        print("\nLenguajes de programación:")
        for lenguaje in lenguajes:
            print(f"LENGUAJE DE PROGRAMACION {lenguaje}")
    elif opcion == "2":
        print("\nSistemas operativos:")
        for so in sistemas_operativos:
            print(f"SISTEMA OPERATIVO {so}")
    elif opcion == "3":
        print("\nStacks tecnológicos:")
        for stack in stacks_tecnologicos:
            print(f"STACK DE TECNOLOGIA {stack}")
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona un número entre 0 y 3.")
