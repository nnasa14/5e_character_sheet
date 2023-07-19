import stats

class Skills:
    def __init__(self):
        self.info = []
        self.acrobatics = acrobatics 
        self.animal_handling = animal_handling
        self.arcana = arcana
        self.deception = deception 
        self.history = history
        self.insight = insight
        self.intimidation = intimidation 
        self.investigation = investigation
        self.medicine = medicine
        self.nature = nature 
        self.perception = perception
        self.performance = performance
        self.persuasion = persuasion
        self.religion = religion 
        self.sleight_of_hand = sleight_of_hand
        self.stealth = stealth
        self.survival = survival 

    def __str__(self):
        return f"{self.info}"

    def add_info(self, skill, integer):
        for item in self.info:
            if skill in self.info:
                return f"Already archived"
            
        else:
            self.info.append(skill, integer)

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