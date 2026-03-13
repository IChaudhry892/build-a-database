from data_store import KVStore
import os
import sys

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
            input_line = input().strip()

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

            # Save the key-value pair to the in-memory data store
            database_memory.set(key, value)

            # Persist to disk using append-only writes
            with open("data.db", "a") as file:
                file.write(f"{key},{value}\n")
        else:
            print("SET USAGE: SET <key> <value>")
    elif action == "GET":
        # Check if we have enough parts for GET command
        if len(parts) >= 2:
            key = parts[1]

            # Retrieve the value from the in-memory data store and print it
            value = database_memory.get(key)
            if value is not None:
                print(value)
            else:
                print("ERROR: Key not found", file=sys.stderr)
        else:
            print("GET USAGE: GET <key>")

def replay_log():
    """
    This function replays the log from the data.db file to rebuild the in-memory state of the key-value store.
    It reads each line from the file, parses the key and value, and correctly updates the in-memory data store.
    """
    if os.path.exists("data.db"):
        with open("data.db", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",", 1) # Split into key and value
                    if len(parts) == 2:
                        key, value = parts
                        database_memory.set(key, value)

if __name__ == "__main__":
    replay_log()
    run_cli()