from datetime import datetime
import hydrofunctions as hf
import matplotlib
import matplotlib.pyplot as plt


site = ['04087440', '05536121']
start = '2020-05-10'
end = '2020-05-17'
days = 'P7D'

df = hf.NWIS(site, 'iv', period=days, parameterCd='00065').get_data().df()

## or:
##df = hf.NWIS(site, 'iv', start, end, parameterCd='00065').get_data().df()

df.rename(columns={df.columns[0]: 'Lake Michigan at Chicago Lock', 
                  df.columns[2]: 'Chicago River at Chicago Lock'}, inplace=True)
df.plot()
plt.legend(edgecolor='black', facecolor='white', framealpha=1)
plt.ylabel('Gage height in feet (Chicago City Datum)')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
plt.savefig('./images/gauge.png')
plt.close()


