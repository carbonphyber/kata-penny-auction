from datetime import datetime
import json
from uuid import uuid4

from Logger import Logger
from User import User

# 
class Lot:
  """
  A Lot object
  """
  # 
  def __init__(self, **kwargs):
    self.id = uuid4()
    self.high_bid = None
    self.time_created = datetime.now()
    if not isinstance(kwargs.get('logger', None), Logger):
      raise ValueError('User.__init__ requires instance of Logger')
    self.logger = kwargs.get('logger', None)

  # 
  def bid(self, user):
    if not isinstance(user, User):
      raise TypeError('Lot.bid did not receive a user')
    bid_amount = 1
    user.deduct_balance(bid_amount)
    new_bid_amount = bid_amount if self.high_bid == None else self.high_bid['amount'] + bid_amount
    time_started = datetime.now()
    self.logger.add_entry('Lot.bid by %s by %d to %d at %s' % (user.id, bid_amount, new_bid_amount, time_started))
    self.high_bid = {
      'user_id': str(user.id),
      'amount': new_bid_amount,
      'time_started': time_started.isoformat(),
    }

  # 
  def __str__(self):
    return 'Lot: %s' % (json.dumps({
                                    'id': str(self.id),
                                    'high_bid': self.high_bid,
                                    'time_created': self.time_created.isoformat(),
                                  }))
