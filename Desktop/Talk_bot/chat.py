from markov_python.cc_markov import MarkovChain


q = MarkovChain()
a = MarkovChain()
q.add_file('/users/agaro/desktop/Talk_bot/questions.txt')
a.add_file('/users/agaro/desktop/Talk_bot/answers.txt')
counter = 0
while counter <= 10:
	question = q.generate_text(13)
	question = ' '.join(question)
	print ('Bot A: ')
	print question
	answer = a.generate_text(14)
	print('Bot B: ' )
	answer = ' '.join(answer)
	print answer
	counter += 1

	
