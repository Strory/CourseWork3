import pandas as pd

df2010 = pd.read_stata('datasets/GSS2010.dta', convert_categoricals=False)
df2012 = pd.read_stata('datasets/GSS2012.dta', convert_categoricals=False)
df2014 = pd.read_stata('datasets/GSS2014.dta', convert_categoricals=False)
df2016 = pd.read_stata('datasets/GSS2016.dta', convert_categoricals=False)
df2018 = pd.read_stata('datasets/GSS2018.dta', convert_categoricals=False)
df2021 = pd.read_stata('datasets/GSS2021.dta', convert_categoricals=False)
df2022 = pd.read_stata('datasets/GSS2022.dta', convert_categoricals=False)

dataframes = {'2010': df2010, '2012': df2012, '2014': df2014, '2016': df2016,
              '2018': df2018, '2021': df2021, '2022': df2022}
