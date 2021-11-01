# 
class Logger:
  """
  A Logger object
  """

  # 
  def __init__(self):
    self.entries = []

  # 
  def add_entry(self, entry):
    self.entries.append(entry)

  # 
  def __str__(self):
    return "Log:\n\t" + "\n\t".join(self.entries)
