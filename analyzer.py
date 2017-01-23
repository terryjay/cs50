import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # gets passed in positive-words.txt as 'positives' and negative-words.txt as 'negatives'

        # TODO
        # loads positive and negative words into memory in such a way that analyze can access them
        
        # list of all positive words
        self.positives = []
        self.negatives = []
        bad_chars = " \n"
        
        # loads in the positive words
        file = open("positive-words.txt", "r")
        for line in file:
            if not line.startswith(";"):
                self.positives.append(line.strip(bad_chars))
        file.close()
        
        # loads in negative words
        file = open("negative-words.txt", "r")
        for line in file:
            if not line.startswith(";"):
                self.negatives.append(line.strip(bad_chars))
        file.close()
        
        
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        score = 0
        
        # TODO
        # analyzes the sentiment of text, returning a positive score if text is more positive than negative, 
        # a negative score if text is more negative than positive, and 0 otherwise, whereby that score is computed as follows:
            # assign each word in text a value: 1 if the word is in positives, -1 if the word is in negatives, and 0 otherwise
            # consider the sum of those values to be the entire text’s score
        
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        # see if the word is in either self.positives[] or self.negatives[]
        for line in self.positives:
            if line == tokens[0]:
                score += 1
            else:
                score += 0
        for line in self.negatives:
            if line == tokens[0]:
                score -= 1
            else:
                score += 0
                
        return score
