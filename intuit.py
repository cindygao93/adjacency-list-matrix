##intuit python 
## this project takes two csv files, one of a list of employees, with their employee id, name, and department, 
## the second csv file denotes pairs of friends within the company based on their employee ids.

## The programs prints off an adjacency list of employees and their corresponding friends at the company based off of these two files.

import csv

## parses the csv file and returns a list of lists. Each individual list in the list represents a line from the csv file.
def parser(csvfile_name, aList):
	with open(csvfile_name, 'rb') as csvfile:
	 reader = csv.reader(csvfile)
	 for row in reader:
	 	aList.append(row)

	 aList = aList[1:]
	return aList


## this function takes two lists of lists as parameteres, which were the outputs from parsing the csv files 
## it returns an adjacency matrix string that prints the employee id as the first column and subsequent 
## numbers in the row as the employee's friends' id

## example output:

## 1: 2, 3
## 2: 1, 4
## 3: 1
## 4: 2
## 6: None

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


## using the example csv files files in the same directory, this main function prints off the adjacency matrix mentioned in the beginning
def main():
	employees = parser('employees.csv', [])
	friendships = parser('friendships.csv', [])
	print friend_matrix(employees, friendships)

main()
