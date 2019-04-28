import unittest

import tests


def suite():
    theSuite = unittest.TestSuite()
    theSuite.addTest(unittest.makeSuite(StartMenuTests1))
    return theSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    #runner = unittest.TextTestRunner(descriptions=True, verbosity=2)
    test_suite = suite()
    runner.run(test_suite)
