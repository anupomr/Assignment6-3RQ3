"""
Name : Anupom Roy
Assignment No: 6
Student No: 400350605
"""

import unittest
from PasswordManager import PasswordManager


class TestPasswordManager(unittest.TestCase):
    # Part A
    def test_save_password(self, password, website):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.retrive_login_password(website), password)
        self.assertNotEqual(passwordManager.retrive_login_password(website), password)

    def test_save_username(self, username, website):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.insert_login_username(website), username)
        self.assertNotEqual(passwordManager.insert_login_username(website), username)

    # Part B
    def test_retrieve_login_username(self, website):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.retrive_login_username(website), "username")
        self.assertNotEqual(passwordManager.retrive_login_username(website), "username")

    def test_retrieve_login_password(self, website):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.retrive_login_password(website), "password")
        self.assertNotEqual(passwordManager.retrive_login_password(website), "password")

    def test_insert_login_username(self, website):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.retrive_login_username(website), "username")
        self.assertNotEqual(passwordManager.retrive_login_username(website), "username")

    def test_insert_login_password(self, website):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.retrive_login_password(website), "password")
        self.assertNEqual(passwordManager.retrive_login_password(website), "password")

    # Part C
    def test_login_to_system(self, username, password):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.login_to_system(username, password), "True")
        self.assertNotEqual(passwordManager.login_to_system(username, password), "True")

    def test_logged_in_username(self):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.loged_in_username(), "username")
        self.assertNotEqual(passwordManager.loged_in_username(), "username")

    # Part D
    def test_request_user_consent(self, user_consented):
        passwordManager = PasswordManager()
        self.assertEqual(passwordManager.retrive_user_consent(user_consented), "True")
        self.assertNotEqual(passwordManager.retrive_user_consent(user_consented), "True")

