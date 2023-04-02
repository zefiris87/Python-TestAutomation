class KeyValueStorage:

    def __init__(self, filepath):
        self.filepath = filepath
        # check if key is acceptable as attribute
        with open(self.filepath, 'r') as f:
            for line in f:
                if (line.partition('=')[0].strip()).isdigit():
                    raise ValueError('Wrong attribute: ', line.partition('=')[0].strip())

    def __getitem__(self, item):
        with open(self.filepath, 'r') as f:
            for line in f:
                if item == line.partition('=')[0].strip():
                    return line.partition('=')[2].strip()
        raise KeyError(item)

    def __getattr__(self, item):
        with open(self.filepath, 'r') as f:
            for line in f:
                # check if attribute exists
                if hasattr(KeyValueStorage, line.partition('=')[0].strip()):
                    return getattr(KeyValueStorage, line.partition('=')[0].strip())
                if item == line.partition('=')[0].strip():
                    return line.partition('=')[2].strip()

    def keys(self):
        with open(self.filepath, 'r') as f:
            return [line.partition('=')[0].strip() for line in f]

    def values(self):
        with open(self.filepath, 'r') as f:
            return [line.partition('=')[2].strip() for line in f]
