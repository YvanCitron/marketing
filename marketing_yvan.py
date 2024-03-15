from datetime import datetime
import numpy as np
import pandas as pd

indiv = pd.read_csv('donnee/R_COMPLEMENT_INDIVIDU_2016.csv',delimiter = ";",encoding="iso-8859-1",dtype={'EAN':'str'})
compl = pd.read_csv('donnee/R_INDIVIDU_2016.csv',delimiter = ";",encoding="iso-8859-1",dtype={'EAN':'str'})


DF_indiv = pd.DataFrame(indiv)
DF_compl = pd.DataFrame(compl)
DF_fusion = pd.merge(DF_indiv,DF_compl)