import pandas as pd
import LoadData


q1 = pd.Series({'SPECIES' : 'Cods, hakes, haddocks',
                'QUOTA' : 50145 + 111785 + 55563})

q2 = pd.Series({'SPECIES' : 'Herrings, sardines, anchovies',
                'QUOTA' : 509274 + 45500})

q3 = pd.Series({'SPECIES' : 'European sprat - Sprattus sprattus',
                'QUOTA' : 27923})

q4 = pd.Series({'SPECIES' : 'Tunas, bonitos, billfishes',
                'QUOTA' : 404815})

q5 = pd.Series({'SPECIES' : 'Salmons, trouts, smelts',
                'QUOTA' : 10000 + 5985})

fishingQuotas = pd.DataFrame([q1, q2, q3, q4, q5])
fishingQuotas = fishingQuotas.set_index('SPECIES')
print(fishingQuotas.head())




