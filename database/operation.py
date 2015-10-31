#!/usr/bin/env python
#coding:utf8
import time
import MySQLdb
import sys

def con():
	conn = MySQLdb.connect(host="localhost",user="fabian",passwd="fabian",db="fabian",charset="utf8")
	return conn

class Operition():
	def __init__(self):
		self.con=con()
	
	def delete(self):
		cursor = self.con.cursor()
		try:
		    sql = "drop table if exists message"
		    cursor.execute(sql)
		finally:
			cursor.close()
	
	def creat(self):
		cursor = self.con.cursor()
		try:
		    sql = "create table if not exists message(name varchar(128) primary key,phone varchar(50))"
		    cursor.execute(sql)
		finally:
			cursor.close()
	
	def inser(self):
		cursor = self.con.cursor()
		try:
		    sql = "insert into message(name,phone) values(%s,%s)"
		    param = ("fabian",'18215546753')
		    n = cursor.execute(sql,param)
		    print 'insert',n
		finally:
			cursor.close()
	
	def sec(self):
		cursor = self.con.cursor()
		try:
		    n = cursor.execute("select * from message")
		    for row in cursor.fetchall():
			    print row
			    for r in row:
				    print r
		finally:
			cursor.close()
	
SELECT = """
###################################################
Please select operation:
###################################################
		1、Database Table Delete
		2、Database Table Create
		3、Database Table Insert
		4、Database Table Select
		5、Exit
"""

def main():
	try:
		while True:
			print SELECT
			n = raw_input("Please Select Operation: ")
			op = Operition()
			try:
				if n == "1":
					op.delete()
					continue
				elif n == "2":
					op.creat()
					continue
				elif n == "3":
					op.inser()
					continue
				elif n == "4":
					op.sec()
					continue
				elif n == "5":
					sys.exit()
					break
			except Exception as e:
				print "Input Error: %s" % e
	except Exception as e:
		print "error: " +str(e)
	finally:
		conn = con()
		conn.close()

if __name__ == '__main__':
	main()


