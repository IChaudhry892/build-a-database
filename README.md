# Build a Database (Python Key-Value Store)

A simple command-line key-value store written in Python.

## What It Does
- Stores key/value pairs in memory while the program runs.
- Persists every `SET` command to `data.db`.
- Rebuilds in-memory data from `data.db` on startup.

## Run
```bash
python3 main.py
```

## Commands
- `SET <key> <value>`: Save or update a key.
- `GET <key>`: Print the value for a key.
- `EXIT`: Quit the program.

## Example
```text
SET color blue
GET color
blue
EXIT
```

## Notes
- Data is stored in `data.db` using an append-only format.
- If a key is set multiple times, the latest value is used.
