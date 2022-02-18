
class DevCofig:
    # local
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/horarios"

    # BD AWS 
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:admin12345678@database-horario.c2vgjhdyoli1.us-east-1.rds.amazonaws.com:3306/horarios"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {"devConfig": DevCofig}

