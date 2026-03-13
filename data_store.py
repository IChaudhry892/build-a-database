class KVStore:
    def __init__(self):
        # Initialize the data store as an empty list of tuples (key, value)
        self.data = []

    def set(self, key, value):
        """
        This method sets the value for a given key in the data store. If the key already exists, it updates the value. If the key does not exist, it adds a new key-value pair to the data store.
        """
        # Check if the key already exists in the data store
        for i, (k, v) in enumerate(self.data):
            if k == key:
                # If the key exists, update the value
                self.data[i] = (key, value)
                return
            
        # If the key does not exist, add a new key-value pair to the data store
        self.data.append((key, value))

    def get(self, key):
        """
        This method retrieves the value for a given key from the data store. If the key does not exist, it returns None.
        """
        # Search for the key in the data store
        for k, v in self.data:
            if k == key:
                return v
        
        # If the key is not found, return None
        return None