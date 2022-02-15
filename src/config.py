
class DevCofig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/horarios"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {"devConfig": DevCofig}

