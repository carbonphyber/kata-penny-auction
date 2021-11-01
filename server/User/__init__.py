from datetime import datetime
import json
from uuid import uuid4

from Logger import Logger


# 
class User:
  """
  A User object
  """

  # 
  def __init__(self, **kwargs):
    self.id = uuid4()
    self.balance = 0.0
    self.time_created = datetime.now()
    logger = kwargs.get('logger', None)
    if not isinstance(logger, Logger):
      raise ValueError('User.__init__ requires instance of Logger (%s)' % (logger))
    self.logger = logger

  # 
  def deduct_balance(self, amount):
    if not isinstance(amount, int):
      self.logger.add_entry('deduct_balance recieved a bad amount')
      raise TypeError('User.deduct_balance accepts only an integer')
    if amount < 0:
      self.logger.add_entry('deduct_balance recieved a bad amount')
      raise ValueError('User.deduct_balance accepts only a positive integer')
    if self.balance - amount < 0.0:
      self.logger.add_entry('deduct_balance negative balance')
      raise RuntimeError('Insufficient balance')
    self.logger.add_entry('deduct_balance changed %d by %d to %d' % (self.balance, amount, self.balance - amount))
    self.balance -= amount

  # 
  def increase_balance(self, amount):
    if not isinstance(amount, int):
      self.logger.add_entry('User.increase_balance recieved a bad amount')
      raise TypeError('User.increase_balance accepts only an integer')
    if amount < 0:
      self.logger.add_entry('User.increase_balance recieved a bad amount')
      raise ValueError('User.increase_balance accepts only a positive integer')
    self.logger.add_entry('User.increase_balance changed %d by %d to %d' % (self.balance, amount, self.balance + amount))
    self.balance += amount

  # 
  def __str__(self):
    return 'User: %s' % (json.dumps({
                                     'id': str(self.id),
                                     'balance': self.balance,
                                     'time_created': self.time_created.isoformat(),
                                    }))
