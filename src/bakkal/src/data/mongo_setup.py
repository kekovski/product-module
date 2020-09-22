from mongoengine import connect
import mongoengine

def global_init():
    # mongoengine.connect('test_database')
    # mongoengine.register_connection(alias='core', db='test_database', name='test_database', host='localhost', port='27017')
    mongoengine.register_connection(alias='core', name='bakkal')