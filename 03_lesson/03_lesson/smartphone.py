class Smartphone:
    def __init__(self, brend, model, number):
        self.brend = brend
        self.model = model
        self.number = number

    def get_brend(self):
        return self.brend

    def get_model(self):
        return self.model

    def get_number(self):
        return self.number
