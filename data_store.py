class KVStore:
    def __init__(self):
        # Initialize the data store as an empty list of tuples (key, value)
        self.data = []

    def set(self, key: str, value: str) -> None:
        """
        Sets the value for a given key. Updates the value if the key already exists.
        """
        # Check if the key already exists in the data store
        for i, (k, v) in enumerate(self.data):
            if k == key:
                # If the key exists, update the value
                self.data[i] = (key, value)
                return
            
        # If the key does not exist, add a new key-value pair to the data store
        self.data.append((key, value))

    def get(self, key: str) -> str | None:
        """
        Retrieves the value for a given key. Returns None if the key does not exist.
        """
        # Search for the key in the data store
        for k, v in self.data:
            if k == key:
                return v
        
        # If the key is not found, return None
        return None