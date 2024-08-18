import sympy as sp
from logic import *

P = sp.symbols('P')
Q = sp.symbols('Q')
R = sp.symbols('R')

class KnowledgeBase():

	def __init__(self):
		self.knowledge = []
		
	def add(self, sentence):
		"""Add a propositional statement to the knowledge base."""
		Sentence.validate(sentence)
		self.knowledge.append(sentence)

	def remove(self, sentence):
		"""Remove a propositional statement from the knowledge base."""
		Sentence.validate(sentence)
		if sentence in self.knowledge:
			self.knowledge.remove(sentence)
		else:
			raise ValueError("The sentence is not in the knowledge base.")

	def contains(self, sentence):
		"""Check if a propositional statement is in the knowledge base."""
		Sentence.validate(sentence)
		return sentence in self.knowledge

	def display(self):
		"""Display all propositional statements in the knowledge base."""
		for sentence in self.knowledge:
			print(sentence.formula())

	def evaluate(self, model):
		"""Evaluate the entire knowledge base with the given model."""
		return all(sentence.evaluate(model) for sentence in self.knowledge)

	def symbols(self):
		"""Return all symbols used in the knowledge base."""
		return set.union(*[sentence.symbols() for sentence in self.knowledge])