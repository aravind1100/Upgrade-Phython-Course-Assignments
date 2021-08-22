#Using Decoraters

def mod_div(func):
	def secondfunc(a,b):
		if a < b :
			a,b = b,a
		func(a,b)
	return secondfunc
	
@mod_div
def div(a,b):
	print(a / b)
	
div(1,2)
			



		