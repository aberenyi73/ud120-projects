res_met = {}
n_components = 10

cr = '''                   precision    recall  f1-score   support

     Ariel Sharon       0.10      0.15      0.12        13
     Colin Powell       0.43      0.53      0.48        60
  Donald Rumsfeld       0.26      0.33      0.30        27
    George W Bush       0.66      0.58      0.62       146
Gerhard Schroeder       0.17      0.20      0.18        25
      Hugo Chavez       0.25      0.13      0.17        15
       Tony Blair       0.50      0.39      0.44        36

      avg / total       0.49      0.46      0.47       322'''

for line in cr.splitlines():
    if 'Ariel Sharon' in line:
        res_met[n_components] = line.split()[-2]

print res_met
