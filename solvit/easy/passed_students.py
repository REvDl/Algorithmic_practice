class Solution:
	def passed_students(self, students: dict[str, list[str]], value: int) -> list[str]:
		# Напишите здесь свой код
		result = []
		for student, balls in students.items():
			if all((int(b.split("/")[0]) / int(b.split("/")[1]) * 100 >= value) for b in balls):
				result.append(student)
		return result



ball = "3/10"
ball = ball.split("/")
print(ball)
print(int(ball[0]) / int(ball[-1]) * 100)

students = {
    "Иван": ["5/5", "10/10", "20/20"],
    "Мария": ["4/5", "9/10", "18/20"],
    "Алексей": ["5/5", "10/10", "19/20"],
    "Ольга": ["3/5", "7/10", "14/20"],
    "Дмитрий": ["5/5", "10/10", "20/20"],
}
value = 90
obj = Solution()
print(obj.passed_students(students, value))
# Вывод:
#
# ["Иван", "Алексей", "Дмитрий"]
# Объяснение:
#
# Иван → 100%, 100%, 100% ✅
# Мария → 80%, 90%, 90% ❌ (80 < 90)
# Алексей → 100%, 100%, 95% ✅
# Ольга → 60%, 70%, 70% ❌
# Дмитрий → 100%, 100%, 100% ✅