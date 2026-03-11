import json
import os
from pathlib import Path

PATH_DIR = [r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\codewars",
			r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\exercise",
			r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\leetcode",
			r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\My_fantasy",
			r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\solvit",]



def ProblemsCount(arr: list[str]) -> dict:
	result = dict()
	for i in arr:
		files = os.listdir(i)
		name_file = i.split(os.sep)[-1]
		result[name_file] = len(files)
	return result


def ProblemsCount_V2(arr: list[str]) -> dict:
	result = dict()
	for path in arr:
		path_obj = Path(path)
		all_subdirs = [f.name for f in path_obj.rglob('*') if f.is_dir()]
		print(all_subdirs)

		files = [f for f in path_obj.rglob("*.py") if f.is_file()]
		result[path_obj.name] = len(files)
	return result

#Write with AI
def scan_dir(path_obj: Path) -> int | dict:
	subdirs = [d for d in path_obj.iterdir() if d.is_dir()]
	if not subdirs:
		return sum(1 for f in path_obj.glob('*') if f.is_file())
	res = {}
	for sd in subdirs:
		res[sd.name] = scan_dir(sd)
	return res

#Also white with AI
def print_stats(paths: list[str]) -> None:
	"""Функция, которая отвечает ТОЛЬКО за вывод данных и подсчет итога."""
	final_stats = {}
	grand_total = 0

	for p in paths:
		path_obj = Path(p)
		if path_obj.exists():
			final_stats[path_obj.name] = scan_dir(path_obj)
			current_total = sum(1 for f in path_obj.rglob('*') if f.is_file())
			grand_total += current_total
	final_stats["TOTAL_PROBLEMS"] = grand_total
	print(json.dumps(final_stats, indent=4, ensure_ascii=False))


print_stats(PATH_DIR)