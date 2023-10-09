from typing import Any


class Dictionary:

    def __init__(self, capacity: int = 8, load_factor: float = 2 / 3) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.hash_table: list = [None] * capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_key = hash(key) % self.capacity

        while True:
            if self.hash_table[hash_key] is not None:
                if self.hash_table[hash_key][0] == key:
                    self.hash_table[hash_key][1] = value
                    break
            elif self.hash_table[hash_key] is None:
                self.hash_table[hash_key] = [key, value]
                break

            hash_key = (hash_key + 1) % self.capacity

        if len(self) > self.capacity * self.load_factor:
            self.resize()

    def __getitem__(self, key: Any) -> Any:
        hash_key = hash(key) % self.capacity
        i = 0
        while i < len(self):
            for i in range(len(self.hash_table)):
                h = (hash_key + i) % self.capacity
                if self.hash_table[h] is not None:
                    if self.hash_table[h][0] == key:
                        return self.hash_table[h][1]

            i += 1

        raise KeyError(f"Invalid key: {key}")

    def __len__(self) -> int:
        return len([elem for elem in self.hash_table if elem])

    def resize(self) -> None:
        capacity2 = 2 * self.capacity
        hash_table2 = [None] * capacity2

        for elem in self.hash_table:
            if elem is not None:
                hash_key2 = hash(elem[0]) % capacity2
                while True:
                    if hash_table2[hash_key2] is None:
                        hash_table2[hash_key2] = [elem[0], elem[1]]
                        break
                    hash_key2 = (hash_key2 + 1) % self.capacity

        self.hash_table = hash_table2
        self.capacity = capacity2
