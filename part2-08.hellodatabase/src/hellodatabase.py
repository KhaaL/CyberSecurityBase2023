#!/usr/bin/env python3
import sys
import sqlite3


def read_database(conn):
	agents = []
	cur=conn.cursor()
#	cur.execute("SELECT id, name FROM Agent ORDER BY id")
#	rows = cur.fetchall()

	for t in cur.execute('SELECT id, name FROM Agent ORDER by id'):
		agents.append(t)

#	for row in rows:
#		agents.append(row)


	return agents



def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	agents = read_database(conn)
	print ("agents typeof is ", type(agents))
	for agent in agents:
		print(agent[0], agent[1])
	print ("total of agents ", agents)
# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
