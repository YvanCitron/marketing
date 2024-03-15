from datetime import datetime
import numpy as np
import pandas as pd
R_complement_individu_2016=pd.read_csv("donnee/R_COMPLEMENT_INDIVIDU_2016.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
R_individu_2016=pd.read_csv("donnee/R_INDIVIDU_2016.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
R_magasin_2016=pd.read_csv("donnee/R_MAGASIN.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
R_referentiel=pd.read_csv("donnee/R_REFERENTIEL.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
R_tickets_2016=pd.read_csv("donnee/R_TICKETS_2016.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
R_typo_produit=pd.read_csv("donnee/R_TYPO_PRODUIT.csv",delimiter=";",encoding= 'iso-8859-1',dtype={'EAN':'str'})
if __name__ == "__main__": 
    print(R_complement_individu_2016)
    print(R_individu_2016)
    print(R_magasin_2016)
    print(R_referentiel)
    print(R_tickets_2016)
    print(R_typo_produit)


    DF_indiv = pd.DataFrame(R_individu_2016)
    DF_compl = pd.DataFrame(R_complement_individu_2016)
    DF_fusion = pd.merge(DF_indiv,DF_compl,on='ID_INDIVIDU',how='left')
    DF_fusion