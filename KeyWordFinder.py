from FileNotSetError import FileNotSetError
import DictionaryHelper as dictionary
from docx import Document


class KeyWordFinder(object):
    """docstring for KeyWordFinder"""

    def __init__(self, filename, words={}):
        super(KeyWordFinder, self).__init__()
        self.filename = filename
        self.words = words

    def contains_keywords(self):
        words_in_file = []
        if self.filename is None:
            raise FileNotSetError("NO FILE SET!")
        with open(self.filename) as dataf:
            for words in self.words:
                for line in dataf:
                    if words in line:
                        words_in_file.append(words)
        return words_in_file

    def find_keywords(self):
        keywords = {}
        if ".doc" in self.filename:
            return (self.keywords_from_word())
        with open(self.filename) as dataf:
            for line in dataf:
                for word in line:
                    if not dictionary.value_exists(keywords, word):
                        keywords[word] = 1
                    else:
                        keywords[word] = keywords.get(word, 0) + 1
        return keywords

    def keywords_from_word(self):
        document = Document(self.filename)
        print(document)
        for paragraph in document.paragraphs:
            print(paragraph.text)
        return document.core_properties.keywords

if __name__ == '__main__':
    temp_key = KeyWordFinder(
        "/Users/jea/Documents/Organized_Downloads/Word_Documents/PoliticalArgument.docx")
    print(temp_key.find_keywords())
