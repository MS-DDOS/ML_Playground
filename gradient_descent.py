x_old = -3
x_new = 6
gamma = 0.01 # step size
precision = .00001

def df(x):
	y = 4 * x**3 - 9 * x**2
	return y

while abs(x_new - x_old) > precision:
	print x_old, x_new, abs(x_new - x_old)
	x_old = x_new
	x_new += -gamma * df(x_old)

print x_old, x_new, abs(x_new - x_old)
