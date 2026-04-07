import os                                                                                                                                    
from dotenv import load_dotenv
                                                                                                                                            
load_dotenv()                                                                                                                                

class Config:                                                                                                                                
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'                                                                          
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False                                                                                                   
    SQLALCHEMY_ECHO = False
                                                                                                                                            
class DevelopmentConfig(Config):                                                                                                             
    DEBUG = True
    SQLALCHEMY_ECHO = True                                                                                                                   
                                                                                                                                            
class ProductionConfig(Config):
    DEBUG = False

config_map = {                                                                                                                               
    'development': DevelopmentConfig,
    'production': ProductionConfig,                                                                                                          
    'default': DevelopmentConfig                                                                                                           
}