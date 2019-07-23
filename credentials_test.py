import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):
    """
    Class to test behaviour of the credentials class
    """
    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_credentials = Credentials("Github","tinatasha","blackfaff")

    def tearDown(self):
        """
        Method that cleans up after each test
        """
        Credentials.credentials_list = []

def test_init(self):
        """
        Test for correct initialization
        """
        self.assertEqual(self.new_credentials.account_name,"Github")
        self.assertEqual(self.new_credentials.username,"tinatasha")
        self.assertEqual(self.new_credentials.password,"blackfaffp1")

    def test_save_credentials(self):
        """
        Test to check whether app saves account credentials
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
		
