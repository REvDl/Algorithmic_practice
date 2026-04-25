"""
Вариант 1
1. Даны 2 одномерных массива: А из N элементов и В из М элементов
(элементы в массиве не повторяются). Вычислить разность максимальных
элементов этих массивов. Для поиска максимального элемента использовать
функцию.
2. В матрице А(NхN) и в массиве В(М) заменить все отрицательные
значения нулями. Для замены написать одну функцию и использовать ее и
для массива, и для матрицы.
"""
import random


def random_array(size: int) -> list[int]:
	return random.sample(range(100), size)



def main():
	n, b = map(int, input("Input n, b: ").split())
	arr_A = random_array(n)
	arr_B = random_array(b)
	print(arr_A)
	print(arr_B)
	return max(arr_A) - max(arr_B)
matrix = [
    [10, -5, 3],
    [-1, 0, -8],
    [4, -2, 7]
]

def check_array(arr:list[int]) -> list[int]:
	for i in range(len(arr)):
		if arr[i] < 0:
			arr[i] = 0
	return arr

for i in matrix:
	print(check_array(i))

# def check_matrix(matrix: list[list[int]]) -> list[list[int]]:
# 	for i in range(len(matrix)):
# 		check_array(matrix[i])
# 	return matrix



array = [5, -3, 0]

print(f"{check_array(array)}\n")





