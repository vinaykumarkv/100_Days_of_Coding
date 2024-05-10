inputs = (4, 5, 6)

def logging_decorator(func):
	def wrapper(*args, **kwargs):
		print(f"The name of the function called is : {func.__name__}{inputs}")
		print(f" it returned: {func(*args, **kwargs)}")

	return wrapper

@logging_decorator
def a_function(a,b,c):
	return a*b*c

a_function(inputs[0], inputs[1], inputs[2])


