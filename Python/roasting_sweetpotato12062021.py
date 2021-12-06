

class SweetPotato(object):
    def __init__(self):
        self.status = 'raw'
        self.total_roasted_time = 0
        self.condiments = []

    def roast(self, t):
        self.total_roasted_time += t
        # 0~3min: raw，>3min: half raw，>5min: well done，>8min: burnt，>10min: charcoal
        if self.total_roasted_time < 3:
            self.status = 'raw, '
        elif self.total_roasted_time < 5:
            self.status = 'half raw, '
        elif self.total_roasted_time < 8:
            self.status = 'well done, '
        elif self.total_roasted_time < 10:
            self.status = 'burnt, '
        else:
            self.status = 'charcoal, '

    def addCondiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        print()
        s = f'roasted {self.total_roasted_time}min, ' + self.status
        s += 'added condiments are following: '
        for condiment in self.condiments:
            s += (condiment + ' ')
        return s + '\n'


sp = SweetPotato()

sp.roast(2)
sp.addCondiments('honey')
print(sp)

sp.roast(2)
sp.addCondiments('ketchup')
print(sp)

sp.roast(2)
sp.addCondiments('salt')
print(sp)

sp.roast(2)
sp.addCondiments('pepper')
print(sp)

sp.roast(3)
sp.addCondiments('garlic')
print(sp)
