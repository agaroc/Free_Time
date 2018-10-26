from bs4 import BeautifulSoup
import re
import requests
import numbers

# Get Common answers from a website
def get_answers():
	website = requests.get("https://www.espressoenglish.net/100-answers-to-common-english-questions/)").text
	soup = BeautifulSoup(website, 'html.parser')
	response = soup.find_all('li')
	answer = []
	for word in response:
		txt = word.get_text()
		txt = re.sub('[ \t]+', ' ', txt).strip() #strips html tags
		answer.append(txt)
	l1 = u''.join(answer).encode('ascii', 'ignore').strip()
	with open('/users/agaro/desktop/Talk_bot/answers.txt', 'w') as f:
		f.write(l1)
# Get Common question starters from a website
def get_questions():
	website = requests.get('https://conversationstartersworld.com/good-questions-to-ask/').text
	soup = BeautifulSoup(website, 'html.parser')
	response = soup.find_all('p')
	question = []
	for word in response:
		txt = word.get_text()
		txt = re.sub('[ \t]+', ' ', txt).strip()  #strips html tags
		question.append(txt)
	with open('/users/agaro/desktop/Talk_bot/questions.txt', 'w') as j:
		j.write(u''.join(question).encode('ascii', 'ignore'))  

get_questions()
get_answers()
