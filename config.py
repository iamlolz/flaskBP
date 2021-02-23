# -*- coding: utf-8 -*-

# import OS
import os
basedir = os.path.abspath(os.path.dirname(__file__))


# define class so we can easily access options
class Config(object):
    # Administrator List
    ADMINS = ['alex@coded.cc']
