class Error(Exception):
  pass

class SyntaxError(Error):
  def __init__(self, message):
    self.message = "SyntaxError: " + message

  def __str__(self):
      return self.message