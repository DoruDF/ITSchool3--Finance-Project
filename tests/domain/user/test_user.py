import unittest
from domain.user.user import User


class UserTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # set up
        username = "random_generated"
        user = User(username)
        # execution
        actual_username = user.username
        # assertion
        self.assertEqual(username, actual_username)

    @unittest.skip("TODO: homework")
    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        pass

    @unittest.skip("TODO: homework")
    def test_it_sets_the_stocks_we_give(self):
        pass


if __name__ == "__main__":
    unittest.main()
