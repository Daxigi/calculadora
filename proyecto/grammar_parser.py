import re

def parse_expression(text):
    # Definir la gramática
    operations = {
        'más': '+',
        'suma': '+',
        'sumar': '+',
        'menos': '-',
        'resta': '-',
        'restar': '-',
        'multiplica': '*',
        'multiplicar': '*',
        'por': '*',
        'divide': '/',
        'dividir': '/',
        'entre': '/'
    }
    
    # Dividir el texto en palabras
    words = text.lower().split()

    # Encontrar todos los números en el texto
    numbers = [int(s) for s in re.findall(r'\b\d+\b', text)]
    
    if len(numbers) < 2:
        print("No se encontraron suficientes números para realizar una operación.")
        return None, None, None
    
    # Encontrar la palabra clave de la operación en el texto
    operation = None
    for word in words:
        if word in operations:
            operation = operations[word]
            break
    
    if not operation:
        print("No se encontró una operación válida en el texto.")
        return None, None, None
    
    return numbers[0], numbers[1], operation