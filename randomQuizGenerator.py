#! /usr/bin/python3

# random quiz generator for generating 30 quiz files
# with randomized questions and answers

import random,os

#creating a directory for storing files
parentdir = os.path.abspath('..')
try:
    os.makedirs(parentdir+'/quizes')
except FileExistsError:
    print('quizes folder refreshed')

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
 Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# generate 30 quiz files
for quizNum in range(30):
    # create quiz and answer files
    quizFile = open(parentdir + '/quizes/capitalsquiz%s.txt' % (quizNum + 1), 'w')
    ansFile = open(parentdir + '/quizes/quiz%sanswers.txt' % (quizNum + 1), 'w')

    # header for quiz
    quizFile.write('Name:\t\t Date:\t\t \n\n\n')
    quizFile.write((' '*20)+'State Capitals Quiz %s' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # make question for each state
    for quesNum in range(50):
        # get right and wrong answers
        correctAnswer = capitals[states[quesNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # writing question and options to quiz file
        quizFile.write('%s. What is the capital of %s?\n' % ((quesNum + 1),states[quesNum]))
        for i in range(4):
            quizFile.write('\t %s. %s \n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        # write answer key to file
        ansFile.write('%s. %s\n' % ((quesNum + 1), 'ABCD'[answerOptions.index(correctAnswer)]))

    # close the files
    quizFile.close()
    ansFile.close()
