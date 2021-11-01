import unittest

from Logger import Logger
from Lot import Lot
from User import User

class LoggerMock(Logger):
  def __str__(self):
    return ''

class UserMock(User):
  def __str__(self):
    return ''

class TestUser(unittest.TestCase):
  def test_user_balance_initial(self):
    """
    Test that User.balance is 0 after constructor
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    self.assertEqual(user1.balance, 0)

  def test_user_balance_increase_negative(self):
    """
    Test that User.increase_balance raises when called with a negative amount
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    with self.assertRaises(ValueError):
      user1.increase_balance(-2)

  def test_user_balance_increase_none(self):
    """
    Test that User.increase_balance raises when called with None
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    with self.assertRaises(TypeError):
      user1.increase_balance(None)

  def test_user_balance_increase_float(self):
    """
    Test that User.increase_balance raises when called with a float
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    with self.assertRaises(TypeError):
      user1.increase_balance(2.0)

  def test_user_balance_deduct(self):
    """
    Test that User.balance decreases by amount after calling deduct_balance
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    user1.increase_balance(3)
    self.assertEqual(user1.balance, 3)
    user1.deduct_balance(2)
    self.assertEqual(user1.balance, 1)

  def test_user_balance_deduct_negative(self):
    """
    Test that User.deduct_balance raises when called with a negative amount
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    with self.assertRaises(ValueError):
      user1.deduct_balance(-2)

  def test_user_balance_increase_none(self):
    """
    Test that User.deduct_balance raises when called with None
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    with self.assertRaises(TypeError):
      user1.deduct_balance(None)

  def test_user_balance_increase_float(self):
    """
    Test that User.deduct_balance raises when called with a float
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    with self.assertRaises(TypeError):
      user1.deduct_balance(2.0)

  def test_user_balance_deduct_overflow(self):
    """
    Test that User.balance raises when calling deduct_balance with an amount greater than the previous balance
    """
    log1 = LoggerMock()
    user1 = User(logger=log1)
    with self.assertRaises(RuntimeError):
      user1.deduct_balance(2)


class TestLot(unittest.TestCase):
  def test_lot_high_bid_initial(self):
    """
    Test that Lot.high_bid is None after constructor
    """
    log1 = LoggerMock()
    lot1 = Lot(logger=log1)
    self.assertEqual(lot1.high_bid, None)

  def test_lot_bid(self):
    """
    Test that Lot.high_bid is a list and increases by 1 element after Lot.bid
    """
    log1 = LoggerMock()
    lot1 = Lot(logger=log1)
    user1 = UserMock(logger=log1)
    user1.increase_balance(4)
    user_balance_before = user1.balance
    lot1.bid(user1)
    high_bid_user_after = lot1.high_bid['user_id'] if lot1.high_bid is not None else None
    high_bid_amount_after = lot1.high_bid['amount'] if lot1.high_bid is not None else None
    user_balance_after = user1.balance
    self.assertEqual(high_bid_amount_after, 1)
    self.assertEqual(user_balance_before - user_balance_after, 1)


if __name__ == '__main__':
    unittest.main()
