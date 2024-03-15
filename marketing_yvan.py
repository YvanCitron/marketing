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



DF_INDIVIDU = pd.merge(R_individu_2016,R_complement_individu_2016,on='INDIVIDUS_ID',how='left')
print(type(DF_INDIVIDU.iloc[1]['DATE_CREATION_CARTE']))
DF_INDIVIDU['date_naissance']=pd.to_datetime(DF_INDIVIDU[['DATE_NAISS_A','DATE_NAISS_M','DATE_NAISS_J']].astype(str).apply(lambda x: '-'.join(x),axis=1),format='%Y-%m-%d',errors='coerce')
DF_INDIVIDU['AGE']=(datetime.datetime.strptime('2016-08-31','%Y-%m-%d')-DF_INDIVIDU['date_naissance'])//datetime.timedelta(days=365.2425)
DF_INDIVIDU['Anciennete']=[(datetime.datetime.strptime('2016-08-31','%Y-%m-%d'))-datetime.datetime.strptime(i,'%d/%m/%Y') for i in DF_INDIVIDU['DATE_CREATION_CARTE']]
print(DF_INDIVIDU)
print(R_tickets_2016.columns)
print(R_tickets_2016.iloc[1])
print(R_magasin.columns)
print(R_magasin.iloc[1])
print(R_referentiel.columns)
print(R_referentiel.iloc[1])
print(R_typo_produit.columns)
print(R_typo_produit.iloc[1])
R_tickets_2016['date_achat']=[(datetime.datetime.strptime(i,'%d/%m/%Y')) for i in R_tickets_2016['DATE_ACHAT']]
R_tickets_2016_2=R_tickets_2016.query('date_achat>datetime.datetime.strptime("2014-09-01","%Y-%m-%d")')
df_matrice_travail= R_tickets_2016_2.merge(R_magasin,on='CODE_BOUTIQUE').merge(R_referentiel,on='EAN').merge(R_typo_produit,on='MODELE')
print(df_matrice_travail)