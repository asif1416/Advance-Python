def test(lst):
	result = {}
	for item in lst:
		result[item[0]] = item[1:]
	return result

students = [[1, 'Mahtab Uddin', 'V'], [2, 'Stephen boad', 'V'], [3, 'Benny luke', 'VI'], [4, 'Christian bell', 'VI'], [5, 'Levi Ackerman', 'VII']]

print("Original list of lists:")
print(students)
print("Converted  lists to a dictionary:")
print(test(students))