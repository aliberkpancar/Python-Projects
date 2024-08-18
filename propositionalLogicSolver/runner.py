from sympy import Symbol
from knowledge_base import KnowledgeBase
from inference_engine import Inferences
from query import Query
from logic import *


P = Symbol('P')
Q = Symbol('Q')
R = Symbol('R')

kb = KnowledgeBase()
kb.add(P)
kb.add(Implication(P, Q))


# Inference Engine
inference = Inferences(kb)

print("-----------------")
# Apply Modus Ponens (P -> Q, P is true, therefore Q must be true)
inference.ModusPonens(Implication(P, Q))
print("-----------------")

# Check knowledge base state
kb.display()
print("-----------------")
# # And Elimination Example
and_statement = And(P, Q)
kb.add(and_statement)
inference.Elimination(and_statement)
kb.display()
print("-----------------")

# Double Negation Elimination Example
double_negation = Not(Not(P))
kb.add(double_negation)
inference.DoubleNegationElimination(double_negation)
kb.display()
print("-----------------")

# Check Consistency
is_consistent = inference.CheckLogicalConsistency()
query_system = Query(kb)
print(query_system.queryCertainProposition(P))
print(query_system.queryCertainProposition(Implication(Q, P)))
print(query_system.queryCertainProposition(Not(P)))
print(query_system.queryCertainProposition(Symbol('R')))
print("-----------------")
print(f"Knowledge Base Consistent: {is_consistent}")