class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.sqlite"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://gaalaaxy:5247@localhost:5432/ITI-Flask"


project_config = {
    'dev': DevelopmentConfig,
    "prd": ProductionConfig
}
