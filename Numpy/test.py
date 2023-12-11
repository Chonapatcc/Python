import numpy as np;

income = ["20K", "3M", "12K", "0.04M"
          , "0.023K", "-", "16K", "740K"
          , "15K", "40K","-", "17K", "-"
          , "120K", "56K", "-", "42K", "2M"
          , "0.14M", "60K"]


income_number = np.array([eval(v.replace('M','*1'+'0'*6)) if v[-1]=='M' else eval(v.replace('K','*1'+'0'*3)) if v[-1]=='K' else eval(v) if v!='-' else np.nan for v in income])

print(income_number)