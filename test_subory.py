import os
from typing import List, Dict

class FileHandlingP:
  def __init__(self):
    self.score = 0
    self.total_questions = 0
    
    def read_file(self, filename: str) -> str:
      # read and return file content
      try:
        with open(filename,'r',encoding= 'utf-8'):
          return file.read()
      except FileNotFoundError:
        raise FileNotFoundError("File not found")
      except Exception as e:
        raise Exception(f"Error reading file:{str(e)}")
      
      