import time


def speed_calc_decorator(function):
	def wrapper():
		start_time = time.time()
		function()
		end_time = time.time()
		passed_time = end_time - start_time
		return print(f"the {function} is : {passed_time}")
	return wrapper()


@speed_calc_decorator
def fast_function():
	for i in range(100000):
		i * i


@speed_calc_decorator
def slow_function():
	for i in range(1000000):
		i * i


fast_function()
slow_function()
