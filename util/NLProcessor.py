#! /usr/bin/env python
import nltk


class nltkWord:
    def __init__(self, word):
        self.word = nltk.pos_tag([word])[0]

    def is_noun(self):
        return self.word[1].startswith('NN')

    def is_singular(self):
        return self.word[1] == 'NNP'

    def is_plural(self):
        return self.word[1] == 'NNS'

    def is_verb(self):
        return self.word[1].startswith('VB')

    def is_determiner(self):
        return self.word[1] == 'DT'

    def is_preposition(self):
        return self.word[1] == 'IN'

    def is_pronoun(self):
        return self.word[1].startswith('PRP')

    def is_To(self):
        return self.word[1] == 'TO'

    def is_adjective(self):
        return self.word[1].startswith('JJ')

    def is_adverb(self):
        return self.word[1].startswith('RB')

    def is_punctuation(self):
        return self.word[1] == '.'

    def is_existential(self):
        return self.word[1] == 'EX'

    def is_capitalized(self):
        return self.word[0].isupper() or self.word[0][0].isupper()

    def is_intransitive_verb(self):
        return self.word[0] in ['is', 'was', 'are', 'were', 'be', 'been', 'has', 'have', 'had', 'isnt',
                                    'wasnt', 'arnt', 'werent', 'hasnt', 'havent', 'hadnt']

    def is_stop_word(self):
        return self.is_preposition() or self.is_determiner() \
               or self.is_punctuation() or self.is_pronoun() or self.is_To() or self.is_existential() or self.is_intransitive_verb()

    def is_keep_word(self):
        return (self.is_noun() or self.is_adjective() or self.is_adverb() or self.is_verb()) and not self.is_intransitive_verb()

    def __str__(self):
        return self.word[0]


def find_special_names(text):
    """
    find all words that has capitalized character(s).
    also, find multi-word-combos such as "The Move", "Julius Caesar", "One Direction", etc...
    """
    nl_words = [nltkWord(word) for word in nltk.word_tokenize(text)]

    names = set()
    for i in range(len(nl_words) - 2):
        if nl_words[i].is_capitalized():
            if nl_words[i + 1].is_capitalized():
                names.add(str(nl_words[i]) + ' ' + str(nl_words[i + 1]))
            elif nl_words[i].is_noun():
                names.add(str(nl_words[i]))
    return names


def filter_stop_words(text):
    """
    filter out all stop words
    """
    # remove punctuations and whitespaces
    normalized_terms = [word for word in nltk.word_tokenize(text) if word.isalnum()]

    # actual filtering work
    return set(
        [str(nl_word) for nl_word in [nltkWord(word) for word in normalized_terms] if nl_word.is_keep_word()])


def process(text):
    """
    Normalize text to find special names and filter out stop words
    """

    # If the whole document contains all capitalized words or all lower-case
    # words, then no hope on detecting any special names.
    # Just filter out the stop words and that's it.
    if all([word.isupper() for word in nltk.word_tokenize(text)]) or all(
            [word.islower() for word in nltk.word_tokenize(text)]):
        return filter_stop_words(text)

    # If the document is sensibly formatted, such as capitalize the first
    # letter of the word in a sentence and any names, then lets find them
    # and collect them in conjunction to the list after filtering out stop words.
    return find_special_names(text) | filter_stop_words(text)


if __name__ == '__main__':
    print filter_stop_words('I did enact Julius Caesar: I was killed in the Capitol; Brutus killed me')
