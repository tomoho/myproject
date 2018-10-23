#!/usr/bin/python
# -*- coding: utf-8 -*-

# define shortcuts for command
# import configuation
from . import track as track
from . import staticfileoperation as stop
from . import message as msg

# contact operation 
LOADCONTACT=stop.loadcontact()
ADDCONTACT = stop.addcontact()
FINDCONTACT = stop.findcontact()

#tracking operation
LOADTRACKING =stop.loadtracking()
LOADTRACKED = stop.loadtracked()
FINDTRACKING = stop.findtracking()
FINDTRACKED = stop.findtracked()
FINDTRACK = stop.findtrack()

#msg queue
LOADMSG=stop.loadmsg()
ADDMSG=stop.addmsg()
CLEARMSG=stop.clearmsg()
