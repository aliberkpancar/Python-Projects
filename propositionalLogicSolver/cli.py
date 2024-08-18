import argparse
from knowledge_base import KnowledgeBase, Inferences
from logic import Symbol, Implication, And, Not

def main():
	parser = argparse.ArgumentParser(description="Propositional Logic Solver CLI")
	parser.add_argument('command', choices=['add', 'remove', 'query', 'display'], help='Command to execute')
	parser.add_argument('statement', nargs='?', help='Propositional statement')
	args = parser.parse_args()

	kb = KnowledgeBase()
	inferences = Inferences(kb)

	if args.command == 'add':
		# Example for adding a statement (you will need to parse and create Sentence objects)
		statement = args.statement
		kb.add(statement)
		print("Added: {}".format(statement))

	elif args.command == 'remove':
		# Example for removing a statement
		statement = args.statement
		kb.remove(statement)
		print("Removed: {}".format(statement))

	elif args.command == 'query':
		# Example for querying a statement
		statement = args.statement
		result = kb.contains(statement)
		print("Contains '{}': {}".format(statement, result))

	elif args.command == 'display':
		kb.display()

if __name__ == '__main__':
	main()
