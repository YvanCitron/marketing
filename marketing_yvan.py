import datetime
import numpy as np
import pandas as pd
R_complement_individu_2016=pd.read_csv("donnee/R_COMPLEMENT_INDIVIDU_2016.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'DATE_NAISS_A':'str','DATE_NAISS_M':'str','DATE_NAISS_J':'str','EAN':'str'})
R_individu_2016=pd.read_csv("donnee/R_INDIVIDU_2016.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'DATE_NAISS_A':'str','DATE_NAISS_M':'str','DATE_NAISS_J':'str','EAN':'str'})
R_magasin=pd.read_csv("donnee/R_MAGASIN.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
R_referentiel=pd.read_csv("donnee/R_REFERENTIEL.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
R_tickets_2016=pd.read_csv("donnee/R_TICKETS_2016.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
R_typo_produit=pd.read_csv("donnee/R_TYPO_PRODUIT.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})

print(R_complement_individu_2016)
print(R_individu_2016)
print(R_magasin)
print(R_referentiel)
print(R_tickets_2016)
print(R_typo_produit)



DF_fusion = pd.merge(R_individu_2016,R_complement_individu_2016,on='INDIVIDUS_ID',how='left')
print(type(DF_fusion.iloc[1]['DATE_CREATION_CARTE']))
DF_fusion['date_naissance']=pd.to_datetime(DF_fusion[['DATE_NAISS_A','DATE_NAISS_M','DATE_NAISS_J']].astype(str).apply(lambda x: '-'.join(x),axis=1),format='%Y-%m-%d',errors='coerce')
DF_fusion['AGE']=(datetime.datetime.strptime('2016-08-31','%Y-%m-%d')-DF_fusion['date_naissance'])//datetime.timedelta(days=365.2425)
DF_fusion['Anciennete']=[(datetime.datetime.strptime('2016-08-31','%Y-%m-%d'))-datetime.datetime.strptime(i,'%d/%m/%Y') for i in DF_fusion['DATE_CREATION_CARTE']]
print(DF_fusion)

print(R_tickets_2016.columns)
print(R_magasin.columns)
print(R_referentiel.columns)
print(R_typo_produit.columns)