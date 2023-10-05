class Dictionary:

    def __init__(self) -> None:
        self.capacity = 8
        self.hash_table: list = [None] * 8

    def set(self, key: int, value: object, hash_table: list[object]) -> None:
        self.hash_key = hash(int(key)) % self.capacity
        loop = True

        while loop:
            if hash_table[self.hash_key] is None:
                hash_table[self.hash_key] = f"|key:{key},value:{value} "
                loop = False
                break
            elif hash_table[self.hash_key] is not None:
                if self.hash_key < self.capacity - 1:
                    self.hash_key += 1
                elif self.hash_key == self.capacity - 1:
                    self.hash_key = 0

    def resize(self) -> None:
        self.threshold = 2 * self.capacity / 3

        if self.__len__() > self.threshold:
            self.capacity = 2 * self.capacity

            self.hash_table2 = [None] * 16

            for i in range(len(self.hash_table)):
                if self.hash_table[i] is not None:
                    self.set(
                        self.hash_table[i][self.hash_table[i].index(":") + 1:
                                           self.hash_table[i].index(",")],
                        self.hash_table[i][self.hash_table[i].index(":", 8, -1)
                                           + 1: -1],
                        self.hash_table2
                    )
            self.hash_table = self.hash_table2
            del self.hash_table2

    def __setitem__(self, key: int, value: object) -> None:
        self.set(key, value, self.hash_table)
        self.resize()

    def __getitem__(self, item: int) -> object | None:
        self.item = item
        self.hash_key = hash(item) % self.capacity
        loop = True
        while loop:
            if self.hash_table[self.hash_key] is not None:
                td_tab = self.hash_table[self.hash_key]
                td_key_tab = td_tab[td_tab.index(":") + 1: td_tab.index(",")]

                if str(self.item) != td_key_tab:

                    if self.hash_key < self.capacity - 1:
                        self.hash_key += 1
                    else:
                        self.hash_key = 0

                elif str(self.item) == td_key_tab:
                    loop = False
                    return td_tab[td_tab.index(":", 8, -1) + 1: -1]
            else:
                return None

    def __len__(self) -> int:
        return len([elem for elem in self.hash_table if elem])
