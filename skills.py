import stats

class Skills:
    def __init__(self):
        self.info = []
        self.acrobatics = 0 
        self.animal_handling = 0
        self.arcana = 0
        self.deception = 0 
        self.history = 0
        self.insight = 0
        self.intimidation = 0 
        self.investigation = 0
        self.medicine = 0
        self.nature = 0 
        self.perception = 0
        self.performance = 0
        self.persuasion = 0
        self.religion = 0 
        self.sleight_of_hand = 0
        self.stealth = 0
        self.survival = 0 

    def __str__(self):
        return f"{self.info}"

    def generate_skill(self, skill):
        if skill == "STR":
            pass

        if skill == "INT":
            pass

        if skill == "WIS":
            pass
        
        if skill == "DEX":
            pass

        if skill == "CON":
            pass

        if skill == "CHA":
            pass

    def add_skill(self, skill):
        for item in self.info:
            if skill in self.info:
                return f"Already archived"
        
        skill = Skills.generate_skill(skill)
            
        self.info.append(skill)

    def edit_info(self, skill, integer):
        for item in self.info:
            if item == skill:
                self.info[item] = integer

    def delete_info(self, skill):
        for item in self.info:
            if item == skill:
                self.info.remove(item)

    def edit_info(self, skill, integer):
        for item in self.info:
            if item == skill:
                self.info[item] = integer

    def search_info(self, skill)
        for item in self.info:
            if item == skill:
                return self.info[item]