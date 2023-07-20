class Stats:
    def __init__(self):
        self.info = []
        self.strength = 0 
        self.dex = 0
        self.con = 0
        self.intel = 0 
        self.wis = 0
        self.char = 0

    def __str__(self):
        return f"{self.info}"

    def add_info(self, stat, integer):
        for item in self.info:
            if stat in self.info:
                return f"Already archived"
            
        else:
            self.info.append(stat, integer)

    def edit_info(self, stat, integer):
        for item in self.info:
            if item == stat:
                self.info[item] = integer

    def delete_info(self, stat):
        for item in self.info:
            if item == stat:
                self.info.remove(item)

    def edit_info(self, stat, integer):
        for item in self.info:
            if item == stat:
                self.info[item] = integer

    def search_info(self, stat)
        for item in self.info:
            if item == stat:
                return self.info[item]