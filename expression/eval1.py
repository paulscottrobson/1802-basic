#
#	Reduced shunting yard algorithm.
#
import re

class Shunter:
	def __init__(self,expression):
		self.stack = []
		self.tokens = [x for x in expression]
		self.precedence = { "*":3,"/":3,"+":2,"-":2,"=":1 }
		self.process()

	def output(self,item):
		print(">> "+item)

	def process(self):
		for token in self.tokens:											# token is a value.
			if re.match("[0-9]",token) is not None:
				self.output(token)

			elif token in self.precedence:									# operator. 
																			# tos is operator and token-prec <= tos-prec
				while len(self.stack) > 0 and self.stack[-1] != "(" and self.precedence[token] <= self.precedence[self.stack[-1]]:
					self.output(self.pop())
				self.push(token)

			elif token == "(":
				self.push(token)

			elif token == ")":
				while len(self.stack) > 0 and self.stack[-1] != "(":
					self.output(self.pop())
				junk = self.pop()

			else:
				assert False,"???? "+self.tokens

		while len(self.stack) > 0:
			self.output(self.pop())

	def push(self,v):
		self.stack.append(v)

	def pop(self):
		r = self.stack[-1]
		self.stack = self.stack[:-1]
		return r

x = Shunter("4=(1+2)+(3+4)")