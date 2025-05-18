# 让mysql以mysqldb的方式来对接orm
from pymysql import install_as_MySQLdb

install_as_MySQLdb()