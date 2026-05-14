import json
from pathlib import Path

PATH_DIR = [
	r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\codewars",
	r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\exercise",
	r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\leetcode",
	r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\My_fantasy",
	r"C:\Users\revdos\PycharmProjects\Algorithmiс_practice\solvit",
]
DAYS = 83

IGNORE_NAMES = {".git", ".idea", "__pycache__", "venv", ".env", "README.md"}


def scan_dir(path_obj: Path) -> tuple[int | dict, int]:
	files_count = 0
	subdirs = []

	# 1. Проходим по текущей директории
	for item in path_obj.iterdir():
		if item.name in IGNORE_NAMES:
			continue

		if item.is_file():
			files_count += 1
		elif item.is_dir():
			subdirs.append(item)

	if not subdirs:
		return files_count, files_count
	res = {}
	total_in_this_dir = files_count
	if files_count > 0:
		res["_files"] = files_count

	for sd in subdirs:
		sd_res, sd_total = scan_dir(sd)

		if sd_total > 0:
			res[sd.name] = sd_res
			total_in_this_dir += sd_total

	if list(res.keys()) == ["_files"]:
		return res["_files"], total_in_this_dir

	if total_in_this_dir == 0:
		return 0, 0

	return res, total_in_this_dir


def print_stats(paths: list[str]) -> None:
	final_stats = {}
	grand_total = 0

	for p in paths:
		path_obj = Path(p)
		if path_obj.exists():
			folder_struct, folder_total = scan_dir(path_obj)

			if folder_total > 0:
				final_stats[path_obj.name] = folder_struct
				grand_total += folder_total

	final_stats["TOTAL_PROBLEMS"] = grand_total

	print(json.dumps(final_stats, indent=4, ensure_ascii=False))
	print(f"For: {DAYS} days")


if __name__ == "__main__":
	print_stats(PATH_DIR)