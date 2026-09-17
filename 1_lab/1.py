"""Початковий приклад об'єктно-орієнтованого програмування.

Приклад показує, як описати клас Student і створити на його основі
декілька незалежних об'єктів.
"""


class Student:
	"""Модель студента з ім'ям, групою та оцінками."""

	def __init__(self, name, group):
		self.name = name
		self.group = group
		self.grades = []

	def add_grade(self, grade):
		"""Додає оцінку до списку оцінок студента."""
		if not 1 <= grade <= 12:
			raise ValueError("Оцінка має бути від 1 до 12")
		self.grades.append(grade)

	def average_grade(self):
		"""Повертає середню оцінку або 0, якщо оцінок ще немає."""
		if not self.grades:
			return 0
		return sum(self.grades) / len(self.grades)

	def introduce(self):
		"""Повертає коротке представлення студента."""
		return f"{self.name}, група {self.group}"


def test_hello():
    print("Тестування функції виводу привітання")


def main():
	"""Створює об'єкти та демонструє роботу їхніх методів."""
	first_student = Student("Олена", "КН-32")
	second_student = Student("Максим", "КН-32")

	for grade in (11, 10, 12):
		first_student.add_grade(grade)

	for grade in (9, 10, 8):
		second_student.add_grade(grade)

	students = (first_student, second_student)
	for student in students:
		print(f"Студент: {student.introduce()}")
		print(f"Оцінки: {student.grades}")
		print(f"Середня оцінка: {student.average_grade():.2f}")
		print()


if __name__ == "__main__":
	main()
	test_hello()
