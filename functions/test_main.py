import os
import unittest
import unittest.mock
from unittest.mock import patch

import main


class TestHello(unittest.TestCase):
    def test_hello_world(self):
        req = unittest.mock.Mock()

        # Call tested function
        assert main.hello_world(req) == "Hello World!"

    def test_hello_name_no_name(self):
        req = unittest.mock.Mock(args={})

        # Call tested function
        assert main.hello_name(req) == "Hello World!"

    def test_hello_name_with_name(self):
        name = "test"
        req = unittest.mock.Mock(args={"name": name})

        # Call tested function
        assert main.hello_name(req) == "Hello {}!".format(name)

    @patch('main.flask')
    def test_python_powered(self, mock_flask):
        req = unittest.mock.Mock()

        # Call tested function
        main.python_powered(req)
        
        # Assert python_powered.jpg fil was sent
        mock_flask.send_from_directory.assert_called_with(os.getcwd(), "python_powered.jpg", mimetype="image/jpg")