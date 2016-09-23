##intuit python 

import csv

def parser(csvfile_name, aList):
	with open(csvfile_name, 'rb') as csvfile:
	 reader = csv.reader(csvfile)
	 for row in reader:
	 	aList.append(row)

	 aList = aList[1:]
	return aList


def friend_matrix(employ, friend):

	friendList = []
	matrix = ""
	for record in employ:
		matrix = matrix + record[0] + ": "
		friend_connect = []
		for item in friend:
			if record[0] == item[0]:
				friend_connect.extend(item[1])

			elif (record[0] == item[1]):
				friend_connect.extend(item[0])

		if friend_connect == []:
			matrix = matrix + 'None' + '\n'
		else:
			i=0
			while i<len(friend_connect) - 1:
				matrix = matrix + friend_connect[i] + ', '
				i = i+1

			matrix = matrix + friend_connect[i] + '\n'


		friendList.append(friend_connect)
	
	return matrix 



def main():
	employees = parser('employees.csv', [])
	friendships = parser('friendships.csv', [])
	print friend_matrix(employees, friendships)

main()
