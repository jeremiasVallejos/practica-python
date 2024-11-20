
def realizar_operacion(numero1, numero2, tipo_operacion):
    try:
       
        if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
            return "Error: Ambos números deben ser enteros o decimales."
        
        if not isinstance(tipo_operacion, str):
            return "Error: La operación debe ser una cadena de texto."
    
        operacion = tipo_operacion.strip().lower()

        if operacion == "suma":
            return f"El resultado de la suma es: {numero1 + numero2}"
        elif operacion == "resta":
            return f"El resultado de la resta es: {numero1 - numero2}"
        elif operacion == "multiplicacion":
            return f"El resultado de la multiplicación es: {numero1 * numero2}"
        elif operacion == "division":
            if numero2 == 0:
                return "Error: No se puede dividir entre cero."
            return f"El resultado de la división es: {numero1 / numero2}"
        else:
            return "Error: Operación no válida. Elige 'suma', 'resta', 'multiplicacion' o 'division'."

    except Exception as e:
        return f"Ha ocurrido un error: {e}"

resultado = realizar_operacion(1, 2, "suma")
print(resultado)
