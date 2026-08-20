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



description_two_sum = """
You are given an array of integers nums and an 
integer target, return indices of the 
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order."""


leetcode = Problem(number=1, name="Two Sum", description=description_two_sum, level="easy", categories={"Junior", "Array"})
print(leetcode)


class CatalogManager:
    def __init__(self):
        self._collection = []

    
    def add_problem(self, problem: Problem):
        self.collection.append(problem)


    def delete_by_number(self, number:int):
        initial_count = len(self._collection)
        self._collection = [p for p in self._collection if p.number != number]
