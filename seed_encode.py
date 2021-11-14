#!/usr/bin/env python3

import sys
from random import randint
from itertools import product

import click
import requests


class Encoder:
    """
    Easy to use class for encoding your multi word seed phrase
    """

    def __init__(self, secret_words, set_file, repeat=2):
        """
        Set our seed words
        """

        self.set_file = set_file
        self.repeat = repeat

        # get our character set from disk
        self.__get_set()
        self.combos = self.__generate_combos()

        # read in our word list
        with open('words.txt') as f:
            self.words = [ w for w in f.read().split('\n') if w ]

        self.secret_words = list(secret_words)

    def __get_set(self):
        """
        Get characters from our inputs
        """

        with open(self.set_file) as f:
            self.characters = [i for i in f.read().split('\n') if i]

    def __generate_combos(self):
        """
        Get 2048 combos from our products.
        """

        combos_list = list(set(product(self.characters, repeat=self.repeat)))
        combos_text = [''.join(i) for i in combos_list]

        if len(combos_text) < 2048:
            print('[ERROR] Not enough combos to map 2048 seed words, increase repeat.')
            sys.exit(1)

        # sort the unique products for a bit of portability.
        # return the first 2048 combos for easy zipping with our 2048 seed words
        return sorted(combos_text)[:2048]

    def set_characters(self, charas):
        """
        Overwrite the current character set with a new list of characters
        """

        self.characters = list(charas)

    def all(self):
        """
        Return entire decode sheet
        """

        return dict(zip(self.words, self.combos))

    def get_word(self, combo):
        """
        Get a word from our words list matching a combo
        """

        return dict(zip(self.combos, self.words))[combo]

    def get_words(self, combos):
        """
        Get secret_words from combos
        """

        return [self.get_word(c) for c in combos]

    def get_combo(self, word):
        """
        Get a combo from a word in our words list
        """

        return dict(zip(self.words, self.combos))[word]

    def get_combos(self):
        """
        Get combo for entire secret_words
        """

        return [self.get_combo(w) for w in self.secret_words]

    def encode(self):
        """
        Print out combos for your words
        """
        return [self.get_combo(i) for i in self.secret_words]

    def decode(self, encoded_secret_words):
        """
        Decode the encoded seed words
        """

        return [self.get_word(i) for i in encoded_secret_words if i]


@click.command()
@click.argument('set_file', type=click.Path(exists=True))
@click.option('--repeat', default=2, type=click.INT, help='Number of characters needed to decode a seed word')
def main(set_file, repeat):
    """
    """

    # general warning
    print('[WARNING] MAKE SURE THIS IS A SAFE COMPUTER, AND NO ONE IS WATCHING !!\n')
    secret_words = input('Seed phrase: ').split()
    print('')

    encoder = Encoder(secret_words, set_file, repeat=repeat)

    # pick a random word and confirm th match
    i = randint(0, len(secret_words) - 1)
    word_pick = secret_words[i]
    print('[DEBUG] random word from secret_words is "%s"' % (word_pick))

    combo_pick = encoder.get_combo(word_pick)
    print('[DEBUG] word "%s" encodes as combo "%s"' % (word_pick, combo_pick))

    word_pick_decoded = encoder.get_word(combo_pick)
    print('[DEBUG] combo "%s" decodes as word "%s"' % (combo_pick, word_pick_decoded))

    if word_pick != word_pick_decoded:
        raise Exception('Words do not match')
    else:
        print('[DEBUG] passed!\n')

    print('[DEBUG] secret_words is: %s' % secret_words)

    combos = encoder.get_combos()
    print('[DEBUG] combos for your secret_words: %s' % combos)

    words = encoder.get_words(combos)
    print('[DEBUG] secret_words from your combos: %s' % words)

    if secret_words != words:
        raise Exception('Words do not match')
    else:
        print('[DEBUG] passed!\n')

    print('------------------------------------\n')
    for word in encoder.secret_words:
        print('%s => %s' % (encoder.get_combo(word), word))
    print('\n')

    secret_string = ''.join(encoder.encode())
    secret_string_with_spaces = ' '.join(encoder.encode())
    print('[DEBUG] Secret is length %s without spaces.\n%s\n' % (len(secret_string), secret_string_with_spaces))

    # general warning
    print('[WARNING] MAKE SURE THIS IS A SAFE COMPUTER, AND NO ONE IS WATCHING !!\n')
    encoded_secret_words = input('Encoded seed phrase: ').split()

    print('[DEBUG] Encoded seed phrase decoded to:\n %s' % encoder.decode(encoded_secret_words))
    print('')

    answer = input('Save to combos.txt (y/n): ')
    if answer == 'y':
        print('[DEBUG] Saving full sheet combos.txt')
        with open('combos.txt', 'w') as f:
            for key, value in encoder.all().items():
                f.write('%s: %s\n' % (value, key))


if __name__ == '__main__':
    main()
