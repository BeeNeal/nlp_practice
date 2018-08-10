# Task: implement graph and do a BFS on it
import nltk

#FIXME
def removed_punctuation(s):
    """takes in a string and removes all punctuation  """

    punctuation = set(['.', ','])
    for char in s:
        if char in

def tokenize(s):
    """Takes in a string, and puts it into a list of strings based on spaces
    
    >>> tokenize('This is a very practical sentence')
    ['This', ' is', ' a', ' very', ' practical', ' sentence']

    """

    tokenized_sent = []
    index = 0

    for i in range(len(s)):
        if i == len(s) - 1:
            word = s[index:i+1]
            tokenized_sent.append(word)

        elif s[i] == ' ':
            word = s[index:i]
            tokenized_sent.append(word)
            index = i

    return tokenized_sent


class WordNode():
    """Word node for graph"""

    def __init__(self, word, left=None, right=None):
        self.word = word 
        self.left = left
        self.right = right

    def insert_left(self, left):
        self.left = left

    def insert_right(self, right):
        self.right = right

s = 'This is a very practical sentence'


def lines_to_graph(sent):
    """Takes lines/sents/phrases and makes graphs from them"""

    sent = tokenize(s)
    

for word in sent:






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("passed all tests!")

