class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def __str__(self):
        return f'{self.error_name} : {self.details}'


class IllegalCharacterError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)
