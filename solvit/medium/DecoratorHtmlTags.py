from functools import wraps
from typing import Callable


def add_div(func):
	def wrapper(*args, **kwargs):
		content = func(*args, **kwargs)
		return f"<div>{content}</div>"
	return wrapper

def add_tag(tag:str):
	def wrapper(func:Callable):
		def html_tag(*args, **kwargs):
			content = func(*args, **kwargs)
			return f"<{tag}>{content}</{tag}>"
		return html_tag
	return wrapper


@add_tag("h1")
def greeting(name: str) -> str:
    return f"Hello, {name}!"

@add_div
def greeting_2(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("Anton"))
print(greeting_2("Anton"))



