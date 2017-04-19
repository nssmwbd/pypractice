class GetMinStack():
	def __init__(self,stackData,stackMin):
		self.stackData = stackData 
		self.stackMin = stackMin
		print("stack Create")
		print("stackData is " + str(self.stackData)+"\nstackMin is " + str(self.stackMin) + "\n")
	def pop(self):
		print("do pop()")
		if(len(self.stackData) > 0):
			data = self.stackData.pop()
			self.stackMin.pop()
		     	print("stackData is " + str(self.stackData)+"\nstackMin is " + str(self.stackMin) + "\n")
			return data
		else: 
			print("stack is empty,pleas push number first!!")
	       	
	def push(self,num):
		print("do push() with num " + str(num))
		self.stackData.append(num)
		if(self.stackMin == []):
			self.stackMin.append(num)
		else:
			if(num <= self.stackMin[-1]):
				self.stackMin.append(num)
			else:
				self.stackMin.append(self.stackMin[-1])
		print("After Push() : \nstackData is " + str(self.stackData)+"\nstackMin is " + str(self.stackMin) + "\n")
	def getMin(self):
		print("do getMini()")
		if(len(self.stackData) > 0):
			print("stack Min is " + str(self.stackMin[-1]) + "\n")
			return self.stackMin[-1]
		else:
			print("stack is empty,pleas push number first !!")

stack = GetMinStack([],[]);
stack.pop()
stack.push(4)
stack.push(3)
stack.push(5)
stack.getMin()
stack.pop()
stack.getMin()
stack.pop()
stack.getMin()
##errors
##forget self, string concat forget str()
