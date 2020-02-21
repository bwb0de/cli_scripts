#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="m@r1anell4")
cursor = db.cursor()
cursor.execute("CREATE DATABASE opa")
