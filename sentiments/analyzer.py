import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        self.positives = set()
        
        with open(positives) as lines:  # populate postive word set
            for line in lines:
                if line.startswith(';') == False:
                    line = line.strip()
                    self.positives.add(line)
                    
        self.negatives = set()      
        with open(negatives) as lines:  # populate negative words set
            for line in lines:
                if line.startswith(";") == False:
                    line = line.strip()
                    self.negatives.add(line)
                
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        score = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            if token.lower() in self.positives:
                score = score + 1
            if token.lower() in self.negatives:
                score = score - 1
        return score
