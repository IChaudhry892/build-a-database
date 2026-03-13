def run_cli():
    while True:
        # Prompt for user input
        print("database>> ", end="")
        input_line = input().strip()
        print(f"Received input: {input_line}")

        if len(input_line) == 0:
            print("No input detected. Please enter a command.")
            continue
            
        parse_and_execute_command(input_line)

def parse_and_execute_command(input_line):
    # Check for exit command
    if input_line.lower() == "exit":
        print("Exiting the program. Goodbye!")
        exit(0)

    parts = input_line.split()
    action = parts[0]

    if action == "SET":
        print("SET command received.")
        pass  # Implement SET command logic here
    elif action == "GET":
        print("GET command received.")
        pass  # Implement GET command logic here

if __name__ == "__main__":
    run_cli()