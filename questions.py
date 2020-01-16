
'''
Questions format:
An array of objects in the form
{'id': id of the question,
'text': text of the question,
'answers': an array of answers where each answer is an array with
text of the answer in zeroth index and proceeding action based on
asnwer in first index, where the proceeding action is an array with
action in the zeroth index and ID in the first index }
'''

questions = [
    {'id': 1,
    'text': "This is my first question?",
    'answers': [
        ['Question 1 answer 1', ['question', 2]],
        ['Question 1 answer 2', ['question', 3]],
        ['Question 1 answer 3', ['video', 1]]
            ]
        },
    {'id': 2,
    'text': "This is my second question?",
    'answers': [
        ['Question 2 answer 1', ['question', 0]],
        ['Question 2 answer 2', ['question', 3]],
        ['Question 2 answer 3', ['question', 1]]
            ]
    },
    {'id': 3,
    'text': "This is my third question?",
    'answers': [
        ['Question 3 answer 1', ['video', 1]],
        ['Question 3 answer 2', ['question', 3]],
        ['Question 3 answer 3', ['question', 0]]
            ]
    },
    {'id': 4,
    'text': "This is my fourth question?",
    'answers': [
        ['Question 4 answer 1', ['video', 1]],
        ['Question 4 answer 2', ['question', 2]],
        ['Question 4 answer 3', ['question', 0]]
            ]
    }
]
