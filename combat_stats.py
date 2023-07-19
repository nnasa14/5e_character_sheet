class Combat_stats:
    def __init__(self):
        self.info = []
        self.armor_class = armor_class 
        self.initiative = initiative
        self.speed = speed

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