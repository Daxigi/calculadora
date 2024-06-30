def calculate(numbers, operation):
    if operation == "+":
        result = sum(numbers)
    elif operation == "-":
        result = numbers[0] - sum(numbers[1:])
    elif operation == "*":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "/":
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
        except ZeroDivisionError:
            print("No se puede dividir por 0")
            return None
    else:
        print("Operación no válida")
        return None

    
    return result
