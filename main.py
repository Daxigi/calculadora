from audio_recognition import recognize_audio_from_file
from grammar_parser import parse_expression
from calculator import calculate

def main():
    file_path = "audio_file5.wav"
    text = recognize_audio_from_file(file_path)

    if text:
        expression_result = parse_expression(text)
        if expression_result:
            numbers, operation = expression_result
            
            # Se establece to_binary en True para convertir siempre el resultado a binario
            to_binary = True
            
            result = calculate(numbers, operation)
            if result is not None:
                # Asegúrate de que la función calculate devuelva el resultado en binario cuando to_binary es True
                print(f"El resultado de la operación es: {result}")

if __name__ == "__main__":
    main()