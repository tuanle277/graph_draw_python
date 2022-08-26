class Graph:
	def __init__(self):
		print("graph object created")

	def draw_column_bar(self, column):
		num_column, space = len(column), 26 - len(column)

		for i in range(max(column), 0, -1):
			print(i, end = ' ' * (space - len(str(i)) + 1))
			for j in range(num_column):
				if i - column[j]  <= 0:
					print("|", end = ' ' * space)
					column[j] -= 1
				else:
					print('', end = ' ' * (space + 1))
			print("")

	def draw_row_bar(self, row):
		num_row, space = len(row), 26 - len(row)
		print(' ', end = '')
		for i in range((space + 1) * num_row):
			print("-", end = '')
		print(">", end = '')
		print("")

		print(' ', end = ' ' * space)
		for i in row:
			if len(str(i)) == 1:
				print(i, end = ' ' * space)
			else:
				print(i, end = ' ' * (space - len(str(i)) + 1))


	def draw_graph_bar_row_column(self, row, column):
		self.draw_column_bar(column)
		self.draw_row_bar(row)
		print("")

	def draw_graph_point_row_column(self, coordinates):
		x_coordinates, y_coordinates = [], []
		for i in coordinates:
			x_coordinates.append(i[0])
			y_coordinates.append(i[1])

		i, num_column, space, y_coordinates, x_coordinates, num_coor = max(y_coordinates), len(y_coordinates), 26 - int(max(x_coordinates)), sorted(y_coordinates)[::-1], sorted(x_coordinates), 0

		while i > 0:
			print("{0:.1f}".format(i), end = ' ' * (space - len(str(i)) + 1))
			# print("")
			for j in range(int(max(x_coordinates)) + 1):
				if (j, i) in coordinates:
					print("o", end = ' ' * space)
				else:
					print(' ', end = ' ' * space)
			i -= 0.5
			print("")

		num_row, space = max(x_coordinates) + 1, 26 - max(x_coordinates)
		print(' ', end = '')
		for i in range((int(space) + 1) * int(num_row)):
			print("-", end = '')
		print(">", end = '')
		print("")

		print(' ', end = ' ' * int(space))
		for i in range(int(max(x_coordinates)) + 1):
			print(i, end = ' ' * (int(space) - len(str(i)) + 1))



# calculate the sum of the digits in a range, the results in represented using the class
def sum_digits(n):
	if n <= 0:
		return 0
	else:
		return n % 10 + sum_digits(n // 10)

has, max_column = {}, 0
for i in range(50):
	current_sum_digit = sum_digits(i)
	has[sum_digits(i)] = 1 + has.get(current_sum_digit, 0)
	max_column = max(max_column, has[current_sum_digit])



graph =  Graph()
graph.draw_graph_bar_row_column(["house", "gym", "office", "school"], [1, 5, 4, 7])
graph.draw_graph_bar_row_column(list(has.keys()), list(has.values()))
x = [0.020,0.050,0.070,0.100,0.150,0.200]
y = [0.28, 0.70, 0.97, 1.39, 2.12, 2.79]
points = []
for i in range(len(x)):
	points.append((x[i], y[i]))

	
graph.draw_graph_point_row_column([(1, 2), (3, 4), (9, 6), (12, 13), (21, 9), (6, 9), (4, 5), (9, 10)])
graph.draw_graph_point_row_column(points)
# graph.draw_graph_point_row_column([(1.3, 2.4), (3.1, 4.9), (5.3, 6.5)])




