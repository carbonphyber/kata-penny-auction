import Logger
import Lot
import User

if __name__ == '__main__':
  log1 = Logger()
  user1 = User(logger=log1)
  user2 = User(logger=log1)
  lot1 = Lot(logger=log1)
  user1.increase_balance(2)
  lot1.bid(user1)
  user2.increase_balance(3)
  lot1.bid(user2)
  print(lot1)
  print(user1)
  print(user2)
  print(log1)
