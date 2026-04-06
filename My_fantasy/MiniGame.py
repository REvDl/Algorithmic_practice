import time
from typing import List
import keyboard


def menu():
	try:
		n, m = map(int, input("Размеры (ширина высота): ").split())
		char = input("Символ поля: ")
		person = input("Юнит: ")
		x, y = 0, 0
		print("Управление: WASD. Для выхода зажми 'ESC'")
		time.sleep(1)

		print("\033[H\033[J", end="")
		display(fill_out(n, m, char, person, x, y))
		print("Управление: WASD. ESC - выход.")

		while True:
			event = keyboard.read_event()
			if event.event_type == keyboard.KEY_DOWN:
				key = event.name.lower()
				if key == 'esc':
					print("\nВыход из игры...")
					break
				if key in controls:
					dx, dy = controls[key]
					x = (x + dx) % n
					y = (y + dy) % m
					print("\033[H\033[J", end="")
					display(fill_out(n, m, char, person, x, y))
					print(f"Координаты: {x}:{y} | ESC - выход")
		time.sleep(0.2)

	except ValueError:
		print("Ошибка данных")



def fill_out(n: int, m: int, char: str | int, person: str | int, x: int, y: int) -> List[List[str]]:
    matrix = [[str(char)] * n for _ in range(m)]
    matrix[y][x] = str(person)
    return matrix


def display(matrix: List[List[str]]):
	if not matrix: return
	n_width = len(matrix[0])
	tl, tr, bl, br, hd, vd = "┌", "┐", "└", "┘", "─", "│"

	print(tl + (hd * n_width) + tr)
	for row in matrix:
		print(f"{vd}{''.join(row)}{vd}")
	print(bl + (hd * n_width) + br)

controls = {
    "w": (0, -1),
    "s": (0, 1),
    "a": (-1, 0),
    "d": (1, 0)
}

def move_player(x, y, key):
    # Если нажатой клавиши нет в словаре — стоим на месте (0, 0)
    dx, dy = controls.get(key.lower(), (0, 0))
    return x + dx, y + dy

def main():
	menu()


main()