"""
1.Дана вещественная матрица Z размером 4х5 и число X. Поменять местами
минимальный элемент матрицы и элемент, значение которого равно
заданному X. Если указанный элемент в матрице отсутствует, вывести
сообщение об этом.
2. В заданной целочисленной квадратной матрице Y порядка n*n (n<=8),
определить, номера строк, все элементы которых четны.



"""



def min_matrix(matrix: list[list[int]]) -> tuple[int, int, int]:
	min_element = float("inf")
	min_i, min_j = -1, -1
	if not matrix or len(matrix[0]) == 0:
		raise ValueError("Matrix is empty")
	for i in range(len(matrix)):
		if not matrix[i]:
			raise ValueError(f"Row {i} is empty")
		for j in range(len(matrix[i])):
			if matrix[i][j] < min_element:
				min_element = matrix[i][j]
				min_i, min_j = i, j
	return min_element, min_i, min_j





def replace_matrix(matrix:list[list[int | float]], x:int | float) -> str:
	min_element, i_min, j_min = min_matrix(matrix)
	replace = False
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == x:
				matrix[i_min][j_min], matrix[i][j] = matrix[i][j], matrix[i_min][j_min]
				replace = True
				break
	if replace:
		return "Matrix has been replaced"
	else:
		return f"{x} not found in matrix"




def find_even_rows(matrix: list[list[int]]):
	result = []
	for i in range(len(matrix)):
		if all(matrix[i][x] % 2 == 0 for x in range(len(matrix[0]))):
			result.append(i)
	return result


matrix = [
    [5, 1, 5],
    [2, 3, 4],
    [5, 6, 7]
]
x = 5
print(replace_matrix(matrix, x))


two_matrix = [
    [2, 4, 6],  # Строка 0: все четные (ПОДХОДИТ)
    [1, 2, 3],  # Строка 1: есть нечетные (НЕТ)
    [8, 10, 0]  # Строка 2: все четные (ПОДХОДИТ)
]

print(find_even_rows(two_matrix))












# tests = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[-5, -2, -8], [0, -1, -3], [10, -20, 30]], [[42]], [[1], [1, 2, 3], [4, 5]], ]
#
# for test in tests:
# 	print(min_matrix(test))