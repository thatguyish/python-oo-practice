"""Word Finder: finds random words from a dictionary."""
from random  import randint

class WordFinder:
    """Finds all words from a new line seperated doc"""

    def __init__(self, path):
        self.list_of_words = []
        self.get_path_words(path)


    def get_path_words(self,path):
        words = open(path, "r")
        for word in words:
            editted_word = word[:-2]
            self.list_of_words.append(editted_word)
        print(f"{len(self.list_of_words)} words read")

    def random_word(self):
        random_number = randint(0,235886)
        return self.list_of_words[random_number]


class SpecialWordFinder(WordFinder):
    """Finds all words from a new line seperated doc that does not contain hash or empty lines"""

    def __init__(self, path):
        super().__init__(path)
    
    def get_path_words(self, path):
        words = open(path,"r")
        for word in words:
            if word[0]==" " or word[0]=="#":
                continue
            else:
                editted_words = word[:-1]
                self.list_of_words.append(editted_words)
        print(f"{len(self.list_of_words)}")

        
new_words = SpecialWordFinder("words.txt")
print(new_words.random_word())