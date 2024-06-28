from word2number import w2n
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
    
    words = text.split()

    for i, word in enumerate(words):
        try:
            words[i] = str(w2n.word_to_num(word))
        except ValueError:
            pass
    
    text = ' '.join(words)
    
    # Encontrar todos los números en el texto
    numbers = [int(s) for s in re.findall(r'\d+', text)]
    
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
    
    return numbers, operation