from logic import *

class Inferences():

	def __init__(self, knowledge_base):
		self.knowledge_base = knowledge_base
        
	def ModusPonens(self, implication):
		'''P implies Q. P is true. Therefore, Q must also be true.'''
		if isinstance(implication, Implication):
			antecedent = implication.antecedent
			consequent = implication.consequent
			if antecedent in self.knowledge_base.knowledge:
				print(f"Modus Ponens Applied: {antecedent} -> {consequent}")
				self.knowledge_base.add(consequent)
		else:
			raise ValueError("The sentence is not an implication.")

	def Elimination(self, and_statement):
		# Assuming and_statement is an instance of And class
		conjuncts = and_statement.get_conjuncts()  # This method should return the individual conjuncts
		for conjunct in conjuncts:
			self.knowledge_base.add(conjunct)

	def DoubleNegationElimination(self, sentence):
		'''If P is true, then not not P is also true.'''
		if isinstance(sentence, Not) and isinstance(sentence.operand, Not):
			self.knowledge_base.add(sentence.operand.operand)
		else:
			raise ValueError(f"The sentence '{sentence}' is not a double negation.")

	def CheckLogicalConsistency(self):
		"""Check if the knowledge base is logically consistent."""
		for sentence in self.knowledge_base.knowledge:
			if isinstance(sentence, Not) and sentence.operand in self.knowledge_base:
					return False
			return True
					