class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])

    def match(self, word_list):
        match_anagram = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_anagram.append(word)         

        return match_anagram