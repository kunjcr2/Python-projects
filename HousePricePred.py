from matplotlib.patches import Rectangle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_unweighted, venn3_circles

# Data
homes = [[2000, 5, 1, 2804500],
 [2000, 4, 1, 2803600],
 [2000, 3, 1, 2802700],
 [2000, 2, 1, 2801800],
 [2000, 1, 1, 2800900],
 [3000, 5, 1, 3704500],
 [3000, 4, 1, 3703600],
 [3000, 3, 1, 3702700],
 [3000, 2, 1, 3701800],
 [3000, 1, 1, 3700900],
 [4000, 5, 1, 4604500],
 [4000, 4, 1, 4603600],
 [4000, 3, 1, 4602700],
 [4000, 2, 1, 4601800],
 [4000, 1, 1, 4600900],
 [2000, 5, 0, 1804500],
 [2000, 4, 0, 1803600],
 [2000, 3, 0, 1802700],
 [2000, 2, 0, 1801800],
 [2000, 1, 0, 1800900],
 [3000, 5, 0, 2704500],
 [3000, 4, 0, 2703600],
 [3000, 3, 0, 2702700],
 [3000, 2, 0, 2701800],
 [3000, 1, 0, 2700900],
 [4000, 5, 0, 3604500],
 [4000, 4, 0, 3603600],
 [4000, 3, 0, 3602700],
 [4000, 2, 0, 3601800],
 [4000, 1, 0, 3600900],
 [1000, 5, 1, 1904500],
 [1000, 4, 1, 1903600],
 [1000, 3, 1, 1902700],
 [1000, 2, 1, 1901800],
 [1000, 1, 1, 1900900],
 [1000, 5, 0, 904500],
 [1000, 4, 0, 903600],
 [1000, 3, 0, 902700],
 [1000, 2, 0, 901800],
 [1000, 1, 0, 900900]]

mv = pd.DataFrame(homes, columns=['SquareFeets', 'Rooms', 'Parking', 'Prices'])

mv['>2000 sqft'] = mv['SquareFeets'] > 2000
mv['>2 rooms'] = mv['Rooms'] > 2
mv['parkInc'] = mv['Parking'] == 1

mv['bit'] = np.nan

# Generate the bitstream for each row
for index, row in mv.iterrows():
    mv.loc[index, 'bit'] = str(int(row['>2000 sqft'])) + str(int(row['>2 rooms'])) + str(int(row['parkInc']))

# Create the dictionary with the bitstream as keys and average prices as values
dict_avg_prices = mv.groupby('bit')['Prices'].mean().to_dict()

tpl = ()

for key,val in dict_avg_prices.items():
    tpl = tpl + (val,)

venn = venn3(subsets=(30, 30, 15, 30, 15, 15, 10),set_labels=['>2000 Sq Ft','>2 Rooms','Has Parking'])
venn_circles = venn3_circles(subsets= (30, 30, 15, 30, 15, 15, 10),linestyle='solid',linewidth=2,color='black')

for venn_id, val in dict_avg_prices.items():
    if venn_id=='000':
        plt.annotate(f'${val}',xy=(0.5,-0.5))
        continue
    venn.get_label_by_id(venn_id).set_text(f'${str(val)}')
    venn.get_label_by_id(venn_id).set_fontsize(9)

plt.title("House Price Estimator", loc='center')
ax = plt.gca()
ax.set_facecolor('lightgrey')
ax.set_autoscalex_on(False)
ax.set_xlim(-0.9,0.9)
ax.set_autoscaley_on(False)
ax.set_ylim(-0.8,0.7)
plt.text(-0.69, 0.63, 'U= {}'.format(len(homes)))
plt.axis('on')

plt.show()