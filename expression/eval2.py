import re
#
#	Dummy execution pipeline which just records what it is sent.
#
class PipeLine:
	def __init__(self):
		self.pipeline = []
	def pushValue(self,n):
		self.pipeline.append("#"+str(n))
	def execute(self,operand):
		self.pipeline.append(operand)
	def get(self):
		return ",".join(self.pipeline)

#
#	Breaks down a tokenised string and applies modified version of shunting algorithm to it
#	Results and commands are passed to an execution pipeline.
#
#	Note, there is no lazy evaluation here.
#
class ExpressionSourcePipeLine:
	def __init__(self,tokenList,pipeline):
		self.wordSize = 2
		self.tokens = tokenList 											# save tokens.
		self.pipeline = pipeline 											# save calculation pipeline.
		self.endMarker = "[TOP]"
		self.stack = [ self.endMarker ]										# operator stack

		self.precedence = { }												# precedence of various tokens.
		self.precedenceAdd(0,"and,or,xor")									# logical operators
		self.precedenceAdd(1,"==,>=,<=,!=")									# 2 character conditionals
		self.precedenceAdd(2,">,<") 										# 1 character conditionals
		self.precedenceAdd(3,"+,-")											# additive
		self.precedenceAdd(4,"*,/,%") 										# multiplicative
		self.precedenceAdd(5,"!,?,$") 										# memory accessing.
	#
	#	Set up the precedence list. Note, precedence is going to be held in bits 2,3,4 of the opcode.
	#	so and/or/xor are 128..131 , == >= <= != are 132..135 and so on. This is technically wrong as
	#	a >= b has a higher precedence than a > b but this will only apply if you write a > b >= c
	#	which won't work.
	#
	def precedenceAdd(self,level,tokenList):
		for t in tokenList.split(","):								
			self.precedence[t] = level

	#
	#	Process the whole lot.
	#
	def process(self):
		self.mode = 'T'														# start in TERM mode this sort of GOTOs
		tCount = 0
		while self.mode != 'Q': 											# until quit.
			token = self.tokens[tCount]
			tCount+= 1

			print("DBG:",token,self.stack,self.pipeline.get())
			if self.mode == 'T':											
				self.term(token)
			elif self.mode == 'O':
				self.operand(token)

		print("DBG:Post",self.stack,self.pipeline.get())
		print("DBG:End",self.stack,self.pipeline.get())
	#
	#	Process a term.
	#
	def term(self,token):
		if re.match("^[0-9]+$",token):										# found a number
			self.pipeline.pushValue(int(token))								# push its value on the pipeline.
			self.mode = 'O' 												# and expect operator

		elif re.match("^[a-z]$",token[0]):									# found a stand alone variable.
			self.pipeline.pushValue((ord(token[0])-ord('a')) * self.wordSize + 10000) 	# push address on the stack
			if len(token) == 1:												# just A-Z
				self.pipeline.execute("@")									# read it.
			else: 															# now check for A-ZA-Z<n>
				assert token[0] == token[1] and re.match("^[0-9]+$",token[2:]) is not None, "Bad array quick access "+token
				self.pipeline.pushValue(int(token[2:])*self.wordSize)		# push the offset on the stack.
				self.pipeline.execute("!") 									# do add word indirect.
			self.mode = 'O' 												# and expect operator

		elif token == "(":													# open bracket.
			self.stack.append("(")											# append parenthesis marker.
		else:
			assert False,"Unknown term : "+token
	#
	#	Process an operand.
	#
	def operand(self,token):

		if token in self.precedence:										# check we actually have an operator.
			tokenPrecedence = self.precedence[token]						# get its precedence
																			# while precedence(token) < precedence(tos)
			while len(self.stack) > 1 and self.stack[-1] != "(" and tokenPrecedence < self.precedence[self.stack[-1]]:
				self.pipeline.execute(self.stack[-1])						# destack tokens.
				self.stack = self.stack[:-1]
			self.stack.append(token)										# stack the new token.
			self.mode = 'T'

		else:
			while self.stack[-1] != "(" and self.stack[-1] != self.endMarker: # do ops back to open bracket/end marker
				self.pipeline.execute(self.stack[-1])						# destack tokens.
				self.stack = self.stack[:-1]
			self.stack = self.stack[:-1]									# dump the (/# on the TOS.
			if token != ")":												# is it an unknown operator, e.g. the end ?
				assert len(self.stack) == 0,"Too many open brackets" 		# have we closed everything.
				self.mode = 'Q' 											# if so, quit.
			else:
				assert len(self.stack) > 0,"Too many close brackets"		# pulled the ending '#'
				self.mode = 'O'

expr = "len a + 2 , "
expr = [x for x in expr.lower().split(" ") if x.strip() != ""]			

es = ExpressionSourcePipeLine(expr,PipeLine())
es.process()

#
#	+ @ ? save their retrieved values as can be used to save result.
#
#
#	Todo: 1 parameter system functions.
#

# 	Tokenising :-
#
#	Operators first
#	Keywords that execute things
#	Anything else.
#	AA-ZZ
#	A-Z
#
#	255 :					end of line (cannot search forward because of tokenised constants)
#	254 : 254 low high 		16 bit constant.
#	253 : 253 low 			8 bit constant (range 0-255)
# 	252 : 252 <string> 0 	quoted string
#
