import re



def menu_calories():
	while True:
		print("Введи данные о себе (вес) через запятую/пробел:\n")
		data = input()
		valid_data = re.split(r'[ ,;.]+', data.strip())
		try:
			if len(valid_data) == 1 and all(x.isdigit() for x in valid_data):
				return int(valid_data[0])
			raise ValueError
		except Exception:
			print("Данные введены некоректно, повторите попытку")


WEIGHT_GAIN = ["массанабор", "масанабор", "маса", "масса", "набор", "кач"]
WEIGHT_LOSS = ["похудение", "сушка", "сброс", "худеть", "диета", "жиросжигание"]
WEIGHT_MAINTAIN = ["поддержание", "норма", "статика", "сохранение", "баланс"]
TARGETS = {
    "gain": WEIGHT_GAIN,
    "loss": WEIGHT_LOSS,
    "maintain": WEIGHT_MAINTAIN
}

MACROS = {
    "gain": {"calories": 40, "protein": 1.9, "fat": 1.1},
    "loss": {"calories": 27, "protein": 2.3, "fat": 0.9},
    "maintain": {"calories": 32, "protein": 1.7, "fat": 1.1},
}


def detect_goal(user_input: str):
    user_input = re.sub(r'[^a-zA-Zа-яА-ЯёЁ]', '', user_input.lower().strip())

    for goal_key, keywords in TARGETS.items():
        for word in keywords:
            if word in user_input:
                return goal_key

    return None


def calculate_macros(goal_key: str, weight: int = 1):
    data = MACROS[goal_key]

    calories = data["calories"] * weight
    protein = data["protein"] * weight
    fat = data["fat"] * weight

    carbs = (calories - (protein * 4 + fat * 9)) / 4
    carbs = round(carbs, 2)

    return {
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "carbohydrates": carbs
    }


def goal_definition():
	weight = menu_calories()
	goal_input = input("Введи свою цель: ")

	goal_key = detect_goal(goal_input)

	if not goal_key:
		return "Сорян, но ко мне только по спортивным вопросам"

	return calculate_macros(goal_key, weight)



print(goal_definition())
