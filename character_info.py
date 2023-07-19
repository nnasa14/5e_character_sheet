class Char_info:
    def __init__(self):
        self.info = []
        self.name = name 
        self.player_class = player_class
        self.level = level
        self.race = race 
        self.alignment = alignment
        self.xp = xp

    def __str__(self):
        return f"{self.info}"

    def add_info(self, info, description):
        for item in self.info:
            if info in self.info:
                return f"Already archived"
            
        else:
            self.info.append(info, description)

    def edit_info(self, info, description):
        for item in self.info:
            if item == info:
                self.info[item] = description

    def delete_info(self, info, description):
        for item in self.info:
            if item == info:
                self.info.remove(item)

    def edit_info(self, info, description):
        for item in self.info:
            if item == info:
                self.info[item] = description

    def search_info(self, info)
        for item in self.info:
            if item == info:
                return self.info[item]