def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            print("No se puede dividir por 0")
            return None
        return a / b
    else: 
        print("Operación no válida")
        return None