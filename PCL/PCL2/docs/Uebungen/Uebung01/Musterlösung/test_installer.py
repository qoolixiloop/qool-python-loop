# -*- coding: utf-8 -*-

import aufgabe_2_muster as a2

class Installer(object):
    """
    Mockup package installer class.
    """

    def __init__(self, cfgpath):

        self.cfg = a2.ConfigReader(cfgpath)

    def install(self):

        print 'Processing package: {}'.format(self.cfg['name'])

        if self.cfg['signed'] != 'yes':
            if raw_input('Untrusted package! Do you want to continue? (Y/N) '
                    ).lower().startswith('y'):
                pass
            else:
                print 'Aborting install.'
                return None

        print 'Installing to {}...'.format(self.cfg['path'])

        #some installation functionality goes here


def test():

    for path in ['test.ini', 'test.json']:
        inst = Installer(path)
        inst.install()

if __name__ == '__main__':
    test()

