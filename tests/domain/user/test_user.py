import unittest

from domain.user.user import User


class UserMyTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # set up
        username = "random_generated"
        user = User(username)
        # execution
        actual_username = actual_username
        # assertion
        self.assertEqual((username, actual_username))

    def test_it_sets_empty_list_if_we_do_not_spcify_stock(self):
        pass

    @unittest.skip("TODO: homework")
    def test_it_sets_the_stocks_give(self):
        pass
