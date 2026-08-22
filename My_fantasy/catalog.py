from dataclasses import dataclass, field


class Problem:
    def __init__(self, number: int, name: str, description: str, level: str, categories: set):
        self.number = number
        self.name = name
        self.description = description
        self.level = level
        self.categories = categories



    @property
    def level(self) -> str:
        return self._level
    

    @level.setter
    def level(self, complexity: str):
        valid_levels = ["easy", "medium", "hard"]
        complexity_clean = complexity.lower().strip()
        if complexity_clean not in valid_levels:
            raise ValueError(f"Level can't be {complexity}, choose from {valid_levels}.")
        self._level = complexity_clean
    

    def __str__(self):
        clean_lines = [line.strip() for line in self.description.strip().split("\n")]
        clean_desc = "\n   ".join(clean_lines) 
        tags = f" | Tags: {', '.join(self.categories)}" if self.categories else ""
        return (
            f"┌{'─'*78}┐\n"
            f"│ PROBLEM #{self.number}: {self.name} [{self.level.upper()}]{tags}\n"
            f"├{'─'*78}┤\n"
            f"  Description:\n   {clean_desc}\n"
            f"└{'─'*78}┘"
        )


    def __repr__(self):
        return f"Problem(number={self.number}, name={self.name!r}, level={self.level!r}), description={self.description!r}"


    def short_info(self) -> str:
        tags = f"({', '.join(sorted(self.categories))})" if self.categories else ""
        return f"#{self.number:<4} | {self.name:<25} | [{self.level.upper():<6}] | {tags}"


class CatalogManager:
    def __init__(self):
        self._collection: dict[int, Problem] = {}

    
    def add_problem(self, problem: Problem) -> None:
        self._collection[problem.number] = problem

    
    def read_problem_by_number(self, number: int) -> Problem | str:
        return self._collection.get(number) or "Problem not found."


    def read_all_problems(self) -> str:
        if not self._collection:
            return "Catalog is empty."
        
        problems = self._collection.values() if isinstance(self._collection, dict) else self._collection
        return "\n".join(p.short_info() for p in problems)


    def delete_by_number(self, number:int) -> None:
        self._collection.pop(number, None)

    def sort_by_categories(self, categories: set) -> list[Problem]:
        return [p for p in self._collection.values()
            if categories <= p.categories
        ]



leetcode = CatalogManager()

description_two_sum = """
You are given an array of integers nums and an 
integer target, return indices of the 
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order."""


problem_two_sum = Problem(
    number=1, 
    name="Two Sum",
    description=description_two_sum,
    level="easy", 
    categories={"Junior", "Array"}
)


description_add_two_numbers = """
You are given two non-empty linked lists
representing two non-negative integers.
The digits are stored in reverse order, 
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
"""


problem_add_two_numbers = Problem(
    number=2, 
    name="Add Two Numbers", 
    description=description_add_two_numbers, 
    level="Medium", 
    categories={"Principal", "Linked List", "Math", "Recursion"}
)

leetcode.add_problem(problem_two_sum)
leetcode.add_problem(problem_add_two_numbers)
print(leetcode.read_all_problems())

