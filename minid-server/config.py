class BaseConfig(object):
    DEBUG = False
    TESTING = False
    
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/minid.db"
    HOSTNAME = "http://localhost:5000/minid"

    EZID_SERVER =  "https://ezid.cdlib.org"
    EZID_SCHEME = "ark:/"
    EZID_SHOULDER = "99999/fk4"
    EZID_USERNAME = "apitest"
    EZID_PASSWORD = "apitest"

class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = "<DATABASE_URL>"
    HOSTNAME = "<HOSTNAME>"
    
    EZID_SERVER =  ""
    EZID_SCHEME = ""
    EZID_SHOULDER = ""
    EZID_USERNAME = ""
    EZID_PASSWORD = ""
