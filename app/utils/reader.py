import os
import pandas as pd

class Reader:
  
  colspecs = [(0, 37), (37, 47), (47, 58), (58, 70), (70, 78)]
  
  def __init__(self, path:str):
      self.path = path
      self.path_files = os.listdir(path)
      self.data_file = []
      
  def get_file_items(self):
      for key, file in enumerate(self.path_files):
        list_extracted = self.extract_to_list(file)
        count_rows = len(list_extracted['NOME'])
        
        for i in range(count_rows): 
          if i > 0: # pular 1 linha
              item = self.mapObj(list_extracted, i)
              self.data_file.append(item)

      return self.data_file
  
  def extract_to_list(self, file):
    return pd.read_fwf(self.path + file, colspecs=self.colspecs)
  
  
  def mapObj(self, arr, i):
    return ({
            "name": arr['NOME'][i],
            "quantidade": int(arr['QUANTIDADE'][i]),
            "proteinas": int(arr['PROTEINAS'][i]),
            "carboidratos": int(arr['CARBOIDRATOS'][i]),
            "gorduras": int(arr['GORDURA'][i]),
  })