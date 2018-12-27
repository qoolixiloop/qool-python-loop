#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import os

import argparse
import codecs
from os import path
import regex
import sys


class SedPattern(object):
    """
    Class to handle sed-like s///g patterns.
    """

    def __init__(self, pattern):
        """
        Initializer for the SedPattern class.
        Args:
            pattern: A unicode string in the form s/re/text/g
        """

        self.pattern_string = pattern
        exprs = self._parse_pattern(pattern)
        self.search = exprs[0]
        self.replacement = exprs[1]

    def _parse_pattern(self, pattern):
        """
        Method to process a text pattern.
        Args:
            pattern: A unicode string in the form s/re/text/g
        Returns:
            A tuple of a regex object and the replacement unicode 
            string.
        """

        expr_parts = pattern.split(u'/')
        if not (expr_parts[0] == u's' and expr_parts[3] == u'g'):
            raise ValueError(u'Malformed command: {}, missing s...g'.format(
                self.pattern_string))
        search = regex.compile(expr_parts[1])
        replacement = expr_parts[2]
        return search, replacement
        
    def sub(self, text):
        """
        Applies pattern to text.
        Args:
            text: A unicode object to replace text in.
        Returns:
            The edited text.
        """

        nl = regex.sub(self.search, self.replacement, text)
        return nl


class SubstituteStream(object):
    """
    Class to handle the program input/output in an encoding-neutral
    manner. The class assumes that the input and output streams are
    both using the same text encoding.
    """

    def __init__(self, encstr, fpath=None, opath=None):
        """
        Initializer for the SubstituteStream class. When no filepaths
        are given as arguments, sets input and output to stdin and
        stdout, respectively.

        Args:
            encstr: Name of the stream's text encoding.
            fpath: Name of the file to read from.
            opath: Name of the file to write to.
        """

        self.standard_in = True
        self.standard_out = True
        self.encoding = encstr

        if fpath is None:
            self.infile = codecs.getreader(self.encoding)(sys.stdin)
        else:
            self.infile = codecs.open(fpath, 'r', self.encoding)
            self.standard_in = False
            
        if opath is None:
            self.outfile = codecs.getwriter(self.encoding)(sys.stdout)
        else:
            try:
                self.outfile = codecs.open(opath, 'r+', self.encoding)
            except IOError:
                self.outfile = codecs.open(opath, 'w', self.encoding)
            self.standard_out = False

        self.text = self.infile.read()

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        self.close()
        return False

    def apply(self, pattern):
        """
        Method to perform text substitution on the stream text.
        Pattern can be any object with a sub method.

        Args:
            pattern: A SedPattern, regex or other object 
                     with a sub method.
        """

        self.text = pattern.sub(self.text)

    def write(self):
        self.outfile.write(self.text)

    def close(self):

        if not self.standard_in:
            self.infile.close()
        if not self.standard_out:
            self.outfile.close()


def _get_args():

    parser = argparse.ArgumentParser(description=u'Substitute '
        'text in a file.')
    parser.add_argument(u'pattern')
    parser.add_argument(u'-e', u'--encoding', default=u'ascii', 
            help=u'Specify encoding of the input and output.')
    parser.add_argument(u'-f', u'--file', help=u'Read text from a file.')
    parser.add_argument(u'-o', u'--out', help=u'Write output to a file.')
    args = parser.parse_args()

    return args


def main():

    args = _get_args()
    try:
        decoded_pat = codecs.decode(args.pattern, args.encoding)
    except UnicodeDecodeError as ue:
        print >> sys.stderr, codecs.encode(u'Error: pattern given is not in '
        'encoding given\n{}'.format(unicode(ue)), args.encoding)
        if args.encoding == u'ascii':
            print >> sys.stderr, codecs.encode(u'You can try specifying '
            'the encoding with -e ENCODING', args.encoding)
        sys.exit(1)

    try:
        sub = SedPattern(decoded_pat)
    except ValueError as v:
        print >> sys.stderr, codecs.encode(u'Invalid pattern: '
                '{}'.format(unicode(v)), args.encoding)
        sys.exit(1)
    except regex.error as err:
        print >> sys.stderr, codecs.encode(u'Invalid pattern: '
                '{}'.format(unicode(err)), args.encoding)
        sys.exit(1)

    try:
        with SubstituteStream(args.encoding, args.file, args.out) as repltext:
            repltext.apply(sub)
            repltext.write()
    except IOError as err:
        print >> sys.stderr, codecs.encode(u'I/O Error: {}'.format(
            unicode(err)), args.encoding)
        sys.exit(1)


if __name__ == '__main__':
    main()
