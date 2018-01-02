import function
import random

GREETING_WORD = ['hai', 'HAI', 'Hai', 'Halo', 'halo', 'hei', 'Hey', 'Hei', 'hey', 'woi', 'WOI']
STOP_WORD_PATH = './id.stopwords.02.01.2016.txt'
TEXT = 'Jadi aku adalah orang yang enggak guna dalam mempelajari Natural Language Processing, Ganbatte to me! Kan wibu gajelas.' 

def isGreeting(texts):
  for text in texts:
    if text in GREETING_WORD:
      return True

def getGreetingResponse():
  return random.choice(['Apa lu jing?', 'Iya apa?', 'Oit bro kenapa', 'Oit', 'Y', 'KZL', 'OI BROBRO', 'WAZZUP MATE?'])

# Read the stopwords from a file
stop_words = []
with open(STOP_WORD_PATH) as f:
  stop_words = f.readlines()
stop_words = [x.strip() for x in stop_words]

user_say = ''
while user_say.lower() != 'exit':
  user_say = raw_input('You: ')
  sentences = function.tokenizer(user_say)  
  sentences = function.remove_stop_words(stop_words, sentences)
  if isGreeting(sentences):
    print('Bot: ' + getGreetingResponse())
  elif user_say.lower() == 'exit':
    print('Bot: Oke bro, gw pergi dulu ya!')
  else:
    print('Bot: Iya bro gw setuju sama lu')