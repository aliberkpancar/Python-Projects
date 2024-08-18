from knowledge_base import *
from logic import *
from inference_engine import *
from knowledge_base import *

class Query:
	
	def  __init__(self, knowledge_base):
		self.knowledge_base = knowledge_base
	
	def	queryCertainProposition(self, sentence):
		'''Query whether a certain proposition is true, false, or indeterminate based on the knowledge base.'''
		Sentence.validate(sentence)
		if self.knowledge_base.contains(sentence):
			return f"The sentence '{sentence.formula()}' is True."
		elif self.knowledge_base.contains(Not(sentence)):
			return f"The sentence '{sentence.formula()}' is False."
		else:
			return f"The truth value of the sentence '{sentence.formula()}' is indeterminate."
			
	
	def	display_inference_rules():
		"""Display the available inference rules."""
		rules = {
			'Modus Ponens': "If P → Q and P is true, then Q must be true.",
			'And Elimination': "If P ∧ Q is true, then both P and Q are true.",
			'Double Negation Elimination': "¬¬P implies P."
		}
		print("Available Inference Rules:")
		for rule_name, description in rules.items():
			print(f"{rule_name}: {description}")
	