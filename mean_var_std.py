import numpy as np

def calculate(list):
  def calculate(list):
      try:
          
          num_array=np.array(list).reshape(3,3)

          #calculating mean across Row, column and mean of matrix
          mean_row=num_array.mean(axis=0)
          mean_col=num_array.mean(axis=1)
          mean_val=num_array.mean()

          #calculating variance across Row, column and variance of matrix
          variance_row=num_array.var(axis=0)
          variance_col=num_array.var(axis=1)
          variance_val=num_array.var()

          #calculating standard deviation across Row, column and standard deviation of matrix
          sd_row=num_array.std(axis=0)
          sd_col=num_array.std(axis=1)
          sd_val=num_array.std()

          #calculating maximum across Row, column and maximum of matrix
          max_row=num_array.max(axis=0)
          max_col=num_array.max(axis=1)
          max_val=num_array.max()

          #calculating minimum across Row, column and minimum of matrix
          min_row=num_array.min(axis=0)
          min_col=num_array.min(axis=1)
          min_val=num_array.min()

          #calculating sum across Row, column and sum of matrix
          sum_row=num_array.sum(axis=0)
          sum_col=num_array.sum(axis=1)
          sum_val=num_array.sum()
          calculation = {'mean': [mean_row, mean_col, mean_val],
                      'variance': [variance_row, variance_col, variance_val],
                      'standard deviation': [sd_row, sd_col, sd_val],
                      'max' : [max_row, max_col, max_val],
                      'min' : [min_row, min_col, min_val],
                      'sum' : [sum_row, sum_col, sum_val]
                      }
          return calculation

      except ValueError:
          print('List must contain nine numbers.')
