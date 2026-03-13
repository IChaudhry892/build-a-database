from data_store import KVStore

# Initialize the in-memory data store
database_memory = KVStore()

def run_cli():
    """
    This function runs the command-line interface (CLI) for the key-value store.
    It continuously prompts the user for input until the user exits the program.
    """
    while True:
        try:
            # Prompt for user input
            input_line = input("database>> ").strip()

            # Skip empty input
            if len(input_line) == 0:
                print("No input detected. Please enter a command.")
                continue
                
            parse_and_execute_command(input_line)
        except EOFError:
            print("ERROR: End of input detected. Exiting program.")
            break

def parse_and_execute_command(input_line):
    """
    This function parses the user input and executes the corresponding command.
    It supports the following commands:
    - SET <key> <value>: Sets the value for the specified key in the in-memory data store.
    - GET <key>: Retrieves the value for the specified key from the in-memory data store and prints it. If the key does not exist, it prints an error message.
    - EXIT: Exits the program.
    """
    parts = input_line.split(" ", 2) # Split into at most 3 parts: action, key, value
    action = parts[0].upper()

    if action == "EXIT":
        print("Exiting program. Goodbye!")
        exit(0)
    elif action == "SET":
        # Check if we have enough parts for SET command
        if len(parts) >= 3:
            key = parts[1]
            value = parts[2]
            print(f"SET command received. Key: {key}, Value: {value}")
            # Save the key-value pair to the in-memory data store
            database_memory.set(key, value)
        else:
            print("SET USAGE: SET <key> <value>")
    elif action == "GET":
        # Check if we have enough parts for GET command
        if len(parts) >= 2:
            key = parts[1]
            print(f"GET command received. Key: {key}")
            value = database_memory.get(key)
            # Retrieve the value from the in-memory data store and print it
            if value:
                print(value)
            else:
                print("ERROR: Key not found")
        else:
            print("GET USAGE: GET <key>")

if __name__ == "__main__":
    # First, open data.db and replay the log to reconstruct the in-memory state (not implemented here)
    run_cli()