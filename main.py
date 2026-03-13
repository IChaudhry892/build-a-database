import os
from data_store import KVStore
from cli import run_cli, parse_and_execute_command

def replay_log(database_memory: KVStore) -> None:
    """
    Replays the log from data.db to rebuild the in-memory state of the key-value store.

    Example:
        If data.db contains "color,blue" this function will call database_memory.set("color", "blue").
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
    """
    Main entry point of the program.
    """
    # Initialize the in-memory data store
    database_memory = KVStore()

    # Replay the log to rebuild the in-memory state then start the CLI
    replay_log(database_memory)
    run_cli(database_memory)