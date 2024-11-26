import unittest

from test.test_bank_account import BankAccountTests


def bank_account_suite():
    suite = unittest.TestSuite()  # crea una suite
    # corre esta prueba en esa suite
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
