class N(object):
	def __init__(self,v):
		self._name = v
	@property
	def name(self):
		'Name Method'
		print 'Get name:',self._name
		return self._name
	@name.setter
	def name(self,v):
		print 'Change...'
		self._name = v
	@name.deleter
	def name(self):
		print 'Remove...'
		del self._name
		

if __name__ == '__main__':
	x = N('Jane')
	print x.name
	
	x.name = 'May'
	
	x.name
	
	del x.name