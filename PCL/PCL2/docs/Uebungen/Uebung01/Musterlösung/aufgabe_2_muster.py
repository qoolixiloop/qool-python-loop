# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import json
import ConfigParser
from os import path

class ConfigReader(object):

    def __new__(cls, fpath):

        if cls == ConfigReader:
            (root, ext) = os.path.splitext(fpath)
            if ext == ".json":
                return JsonReader(fpath)
            elif ext == ".ini":
                return IniReader(fpath)
            else:
                raise ValueError('Unrecognized file format: '
                                 'must be .json or .ini')
        else:
            return object.__new__(cls, fpath)

    def _read(self, fpath):

        return self._parser(fpath)


class JsonReader(ConfigReader):

    def __init__(self, fpath):

        def load_json_from_file(fp):
            with open(fp) as f:
                return json.load(f)

        self._parser = load_json_from_file
        self._cfg = self._read(fpath)

    def __getitem__(self, key):

        return self._cfg[key]


class IniReader(ConfigReader):

    def __init__(self, fpath):

        def _init_parser(parser, fpath):
            parser.read(fpath)
            return parser.get

        self._parser = ConfigParser.ConfigParser()
        self._cfg = _init_parser(self._parser, fpath)

    def __getitem__(self, key):

        return self._cfg('package', key)

