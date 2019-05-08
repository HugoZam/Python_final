fields = ('Patient Name', 'Days Spent', 'Surgery Type', 'Medication', 'Total Charge')


class hospital(object):
    def __init__(self, days, surgery, medication):
        self.Days = days
        self.Surgery = surgery
        self.Medication = medication


class PatientAccount(hospital):
    def __init__(self, days, surgery, medication):#gets the input an calculates in the methods
        super().__init__(days, surgery, medication)

    def days(self):
        staycharge = self.Days * 10400
        return staycharge

    def chargetotal(self, days, surgery, meds):
        d = days
        s = surgery
        m = meds
        total = d + s + m
        return total


class Surgery(hospital):
    def __init__(self, days, surgery, medication):
        super().__init__(days, surgery, medication)

    def searchsurgery(self):

        if self.Surgery == 'heart surgery':
            cost = 40000
            return cost
        elif self.Surgery == 'brain surgery':
            cost = 25856
            return cost
        elif self.Surgery == 'stomach surgery':
            cost = 30000
            return cost
        elif self.Surgery == 'liposuction':
            cost = 5000
            return cost
        elif self.Surgery == 'hear bypass':
            cost = 40000
            return cost
        else:
            print('error not valid')


class Medication(hospital):
    def __init__(self, days, surgery, medication):
        super().__init__(days, surgery, medication)

    def searchmeds(self):

        if self.Medication == 'morphine':
            return 20
        elif self.Medication == 'cannabis':
            cost = 40
            return cost
        elif self.Medication == 'zoloft':
            cost = 15
            return cost

        elif self.Medication == 'omeprazole':
            cost = 3
            return cost
        else:
            print('error not valid')

