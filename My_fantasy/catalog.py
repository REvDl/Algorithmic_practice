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
            raise ValueError(f"Level can't be {complexity}, choose from {valid_levels}")
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



class CatalogManager:
    def __init__(self):
        self._collection: dict[int, Problem] = {}

    
    def add_problem(self, problem: Problem) -> None:
        self._collection[problem.number] = problem

    
    def read_problem_by_number(self, number: int) -> set:
        return self._collection.get(number) or "Problem not found"


    def delete_by_number(self, number:int) -> None:
        self._collection.pop(number, none)

    def sort_by_categories(self, categories: set) -> list[set]:
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


problem_two_sum = Problem(number=1, name="Two Sum", description=description_two_sum, level="easy", categories={"Junior", "Array"})
leetcode.add_problem(problem_two_sum)
print(leetcode.read_problem_by_number(2))

