


# from numba import jit
import time
# start_time = time.time()

a = 2
b = 2
c = 2

# @jit(nopython = True)
def loops(n,m,p):
	for i in range(1,100000):
		for j in range(1,100000):
			for k in range(1,100000):
				n += i * j * k
	
	for i in range(1,100000):
		for j in range(1,100000):
			for k in range(1,100000):
				m += i * j + k

	for i in range(1,100000):
		for j in range(1,100000):
			for k in range(1,100000):
				p += i + j * k
	return n,m,p

start = time.time()
loops(a,b,c)
end = time.time()
print("with compilation : %s" % (end - start))

start = time.time()
loops(a,b,c)
end = time.time()
print("after compilation : %s" % (end - start))



# start = time.time()
# loops(a,b,c)
# end = time.time()
# print("after second compilation : %s" % (end - start))


# print("%s" % (time.time() - start_time))

#  for i in range(1,10000000):
	# 	for j in range(1,10000000):
	# 		for k in range(1,10000000):
	# 			print(m + p)

	# for i in range(1,10000000):
	# 	for j in range(1,10000000):
	# 		for k in range(1,10000000):
	# 			print(m * n)

	# for i in range(1,10000000):
	# 	for j in range(1,10000000):
	# 		for k in range(1,10000000):
	# 			print(p * n)
