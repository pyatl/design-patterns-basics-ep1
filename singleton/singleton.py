#!/usr/bin/env python3

# The singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance. 
# This is useful when exactly one object is needed to
# coordinate actions across the system. 
# Ref: https://en.wikipedia.org/wiki/Singleton_pattern


# Let's say we have a web application with a specific set of settings
class Settings:
    def __init__(self, domain, database_connection, admin_email_address):
        self.domain = domain
        self.database_connection = database_connection
        self.admin_email_address = admin_email_address


# Wee need to make those settings available throughout the whole application.
# Why? Because the web application needs to know the information in the settings file
# in order to work properly.



# settings.py

settings = Settings(
    'pyatl.dev',
    'db.sqlite3',
    'admin@pyatl.dev'
)


# email.py
from settings import settings

send_email(email_address=settings.admin_email_address)



"""
Another example
"""

# Let's say that you want log issues, bug, and erros in your program.

# First you define the logger settings

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'general': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}


# You create one instance of a logger and share that across.
import logging
logger = logging.getLogger('general')

logger.info('I want to say something')

