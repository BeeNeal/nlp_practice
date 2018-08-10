# Task: implement graph and do a BFS on it
import nltk

#FIXME
def removed_punctuation(s):
    """takes in a string and removes all punctuation  """

    # punctuation = set(['.', ','])
    # for char in s:
    #     if char in

def tokenize(s):
    """Takes in a string, and puts it into a list of strings based on spaces
    
    >>> tokenize('This is a very practical sentence')
    ['This', 'is', 'a', 'very', 'practical', 'sentence']

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
            index = i + 1  # incrementing index cuts off the space

    return tokenized_sent


class WordNode(object):
    """Word node for graph"""

    def __init__(self, word, left=None, right=None):
        self.word = word 
        self.left = left
        self.right = right
        self.pos = None

    def assign_pos(self):
        """Uses nltk pos tagger and assigns POS

        """

        pos = nltk.pos_tag(self.word)
        self.pos = pos[1]

        # FIXME the below is a test
        # >>> print(assign_pos('blueberry'))
        # 'NN'
        # pos = nltk.pos_tag(word)
        # self.pos = pos[1]

    def insert_left(self, left):
        self.left = left

    def insert_right(self, right):
        self.right = right

s = 'This is a very practical sentence'


def lines_to_graph(sent):
    """Takes lines/sents/phrases and makes graphs from them"""

    sentence_graph = []
    sent = tokenize(s)

    sent_head = WordNode(sent[0], None, sent[1])
    sentence_graph.append(sent_head)

    for i in range(1, len(sent) - 1):
        w = WordNode(sent[i], sent[i-1], sent[i+1])
        sentence_graph.append(w)

    sent_tail = WordNode(sent[-1], sent[-2])
    sentence_graph.append(sent_tail)

    return sentence_graph

# print (tokenize(s))
sample = lines_to_graph(s)
for word in sample:
    print(word.word, word.right)

x = WordNode('blueberry')
print(x)
WordNode.assign_pos
print(x.pos)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("passed all tests!")

