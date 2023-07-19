class Saving_throws:
    def __init__(self):
        self.info = []
        self.strength = strength 
        self.dex = dex
        self.con = con
        self.intel = intel 
        self.wis = wis
        self.char = char

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