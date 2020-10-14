class Settings:
    def __init__(self, name):
        self.name = name

SETTINGS = Settings('PyATL')

def get_settings():
    return SETTINGS
    