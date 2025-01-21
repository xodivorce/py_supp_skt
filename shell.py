import basic
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        text = input('shell_skt > ')
        if text.strip().lower() == 'clear':
            clear()
            continue
        result, error = basic.run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            print(result)
    except KeyboardInterrupt:
        print("\nExiting shell...")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
