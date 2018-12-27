#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-II: Uebung 01 - Aufgabe 2, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'	: '97-923-163',
#									 'Linus Manser' : '13-791-132'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: run in PyCharm
# Version 2: python test_installer.py
#            (with: import Aufgabe2.py)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## debug
# set to 1 for debugging purposes
DEBUG_FLAG=0

## import packages
# import <your solution to task 2 here> as a2
import Aufgabe2

## class definitions
#
class Installer(object):
    """
    Mockup package installer class.
    """

    def __init__(self, file_path):

        """
        Functionality:
            Calling instance is the function test()
            Reads file_path and initializes object
            Creates instance variable self.cfg of type ConfigReader
        Input:
            file_path of data file of type .ini or .json
            Aufgabe2 module/package as "global variable"
        Output:
            instance variable self.CR contains a ConfigReader object
            which contains the data structures of parsed .ini or .json file
        Exceptions:
        """
        # instance variable CR
        self.CR = Aufgabe2.ConfigReader(file_path)

    def install(self):
        """
        Functionality:
            Calling instance is the function test()
            Checks the field signed of .json or .ini file data structure
            Installs signed package automatically, if unsigned asks user
            (not implemented)
        Input:
            instance variable self.CR
        Output:
            Console output, about mock installation (simulation)
        Exceptions:
            the instance variable of the json parser is a 1-dim dictionary
            he instance variable of the ini parser is a 2-dim dictionary
            used try and except instead of dimension check
        """

        try:
            #json
            cr_name=self.CR['name']
            cr_signed=self.CR['signed']
            cr_path=self.CR['path']
        except:
            #ini
            cr_name=self.CR["package",'name']
            cr_signed=self.CR["package",'signed']
            cr_path=self.CR["package",'path']

        print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print 'Processing package: {}'.format(cr_name)

        ## Install signed package automatically, if unsigned ask user
        # check field signed of .ini or .json file
        # signed is a field in the data structure
        if cr_signed != 'yes':
            if raw_input(
                    'Untrusted package! Do you want to continue? (Y/N) '
                    ).lower().startswith('y'):
                pass
            else:
                print 'Aborting install.'
                return None

        print 'Installing to {}...'.format(cr_path)
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

        #some installation functionality goes here
            # (not implemented)
            #
            #

## test case for Aufgabe2.py
def test(file_json, file_ini):
    """
    Functionality:
        Creates Installer instance
        Calls mock install method
    Input:
        Configuration files of type .json and .ini
    Output:
        Indirectly:
        Console output, about mock installation (simulation)
    Exceptions:
    """

    ## instantiate defined Installer object for each data file
    for file_path in [file_json, file_ini]:

        if DEBUG_FLAG: print " info from I.2.1:", file_path

        #new instance of Installer
        #has instance variable ConfigReader
        my_installer = Installer(file_path)

        #call mock package installern (simulation)
        my_installer.install()

## main procedure
if __name__ == '__main__':

    print "\n######################################################"
    print 'Hi, From Test_Installer : '
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    ## data files
    # json file
    file_json = "/media/benzro/OS/Users/benzro/Desktop/Studium Uni/" \
                "2)ZweitesSemester/27)PCL-2/Uebungen/Uebung01/test.json"
    # ini file
    file_ini = "/media/benzro/OS/Users/benzro/Desktop/Studium Uni/" \
               "2)ZweitesSemester/27)PCL-2/Uebungen/Uebung01/test.ini"

    # invoke defined test installer
    if DEBUG_FLAG: print " info from I.1.1:", __name__
    test(file_json, file_ini)


    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Bye Bye from Test_Installer! :-)"
    print "######################################################"

