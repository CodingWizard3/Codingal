import pandas as pd
ha={'Name':['Pankaj','Meghna','David','Lisa'],
    'Role':['CEO','','',''],
    'Salary':['100','200','','']}

myvar=pd.DataFrame(ha) 
print(myvar.head(2))
print(myvar.tail(2))
print(myvar.info())
myvar.fillna({'Salary':130},inplace=True)
print(myvar.to_string())