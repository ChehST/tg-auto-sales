import os


class Config():
    def __init__(self):
        pass

    def get_admins(self) -> int:
        if os.environ.get('ENVIRONMENT') == 'production':
            return int(os.getenv('KOSVLAS'))
        else:
            return int(os.getenv('CHEH'))

        
cfg = Config()

ADMIN = cfg.get_admins()