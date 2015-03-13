#遇到的问题
	
	
	>>> string="['你好',2]"
	>>> l=['你好',2]
	>>> print l
	['\xe4\xbd\xa0\xe5\xa5\xbd', 2]
	>>> print string
	['你好',2]
	>>> print str(l)
	['\xe4\xbd\xa0\xe5\xa5\xbd', 2]
	
其实也就是编码坑…

被这几个题弄得神烦，感觉花费了太多时间了