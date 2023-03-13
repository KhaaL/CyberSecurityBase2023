#!/usr/bin/env python3
import sys
import sqlite3


def add_agent(conn, aid, name):
	pass # write code here
	cur=conn.cursor()
	values = (aid, name)
	cur.execute("INSERT INTO agent (id, name) VALUES(?,?);", values)  # NB! Input is expected as a tuple
	#QUESTION: SQL insert string statements need to be in quotation marks. I did nothing of the sort here, yet it worked?
	conn.commit()
	return

"""
QUESTION: how does the SQLite functions know that its in the "agent" table that all updates, additions, deletions are supposed to be executed?
"""

def delete_agent(conn, aid):
	pass # write code here, don't forget to commit results once you execute the insert
	del_query = """DELETE FROM agent WHERE id = (?);"""
	cur=conn.cursor()
	cur.execute(del_query, (aid,)) # aid must be passed as a tuple, and the comma does just that: https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
	conn.commit()


def read_database(conn):
	agents = []
	cur=conn.cursor() # 🟡 READ UP ON CONN / CURSOR METHOD: https://peps.python.org/pep-0249/

	for t in cur.execute('SELECT id, name FROM Agent ORDER by id'):
		agents.append(t)

	return agents


def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	while True:
		agents = read_database(conn)
		print('\nActive agents:\n')
		for agent in agents:
			print(agent[0], agent[1])
		print()
		command = input('What would you like to do: [a]dd, [r]emove, or [q]uit? ')

		if command[0].startswith('a'):
			aid = input('id? ')
			name = input('name? ')
			add_agent(conn, aid, name)
			pass
		elif command[0].startswith('r'):
			aid = input('id? ')
			delete_agent(conn, aid)
			pass
		elif command[0].startswith('q'):
			break
	

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
