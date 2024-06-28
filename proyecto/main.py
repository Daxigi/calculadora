from audio_recognition import recognize_audio_from_file
from grammar_parser import parse_expression
from calculator import calculate

def main():
    file_path = "audio_file.wav"
    text = recognize_audio_from_file(file_path) 

    if text: a,b, operation = parse_expression(text)
    if a is not None and b is not None and operation is not None:
        result = calculate(a,b,operation)
        if result is not None:
            print(f"El resultado de la operación es: {result}")

if __name__ == "__main__":
    main()