class style():
	BLACK = lambda x: '\033[30m' + str(x)
	RED = lambda x: '\033[31m' + str(x)
	GREEN = lambda x: '\033[32m' + str(x)
	YELLOW = lambda x: '\033[33m' + str(x)
	BLUE = lambda x: '\033[34m' + str(x)
	CYAN = lambda x: '\033[36m' + str(x)
	WHITE = lambda x: '\033[37m' + str(x)
	UNDERLINE = lambda x: '\033[4m' + str(x)
	RESET = lambda x: '\033[0m' + str(x)
