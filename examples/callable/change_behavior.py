class BilingualDog:

    def __init__(self, language='pt-br'):
        self.language = language

    def __call__(self):
        if self.language == 'pt-br':
            print('Au au au!')
        elif self.language == 'en':
            print('Hof hof hof!')
