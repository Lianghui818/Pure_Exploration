from matplotlib import pyplot as plt
import os
import sys
import copy
import pandas as pd
import numpy as np
sys.path.append('C:/Users/Administrator/Desktop/Async-LinUCB-master')
# from conf import sim_files_folder, save_Linear_Case, save_Linear_Movie_Case

from lib.LinGapE_sync import LinGapE_mult
from lib.LinGapE_full import LinGapE_full
# from lib.LinGapE import LinGapE
from lib.DisALinPE import DisALinPE


algorithms = {}
SampleComList_L_Hom = []
SampleComList_U_Hom = []
SampleComList_D_Hom = []
CommCostList_L = []
CommCostList_U = []
CommCostList_D = []

algorithms['gap=.1_data2_Hom_U'] = 0
algorithms['gap=.2_data2_Hom_U'] = 0
algorithms['gap=.3_data2_Hom_U'] = 0
algorithms['gap=.4_data2_Hom_U'] = 0
algorithms['gap=.5_data2_Hom_U'] = 0

algorithms['gap=.1_data2_Hom_L'] = 0
algorithms['gap=.2_data2_Hom_L'] = 0
algorithms['gap=.3_data2_Hom_L'] = 0
algorithms['gap=.4_data2_Hom_L'] = 0
algorithms['gap=.5_data2_Hom_L'] = 0

algorithms['gap=.1_data2_Hom_D'] = 0
algorithms['gap=.2_data2_Hom_D'] = 0
algorithms['gap=.3_data2_Hom_D'] = 0
algorithms['gap=.4_data2_Hom_D'] = 0
algorithms['gap=.5_data2_Hom_D'] = 0

# for alg_name in algorithms.keys():
# 	if alg_name[17] == 'L' and alg_name[13:16] == 'Hom':
# 		SampleComList_L_Hom[alg_name] = []
# 		CommCostList_L[alg_name] = []
# 	if alg_name[17] == 'U' and alg_name[13:16] == 'Hom':
# 		SampleComList_U_Hom[alg_name] = []
# 		CommCostList_U[alg_name] = []
# 	if alg_name[17] == 'D' and alg_name[13:16] == 'Hom':
# 		SampleComList_D_Hom[alg_name] = []
# 		CommCostList_D[alg_name] = []
# 	print(alg_name)
# exit(0)

with open('C:/Users/Administrator/Desktop/Async-LinUCB-master/MovLinear/AccCommCost_dataset0_05_23_01_16.csv', 'r') as f:
# with open('C:/Users/Administrator/Desktop/Async-LinUCB-master/SimLinear/AccCommCost_dataset2_05_17_08_09.csv', 'r') as f:
	# C:\Users\Administrator\Desktop\Async-LinUCB-master\SimLinear
	num = 0
	for line in f:
		if num == 0:
			num += 1
			continue
		elif num <= 5:
			num += 1
			continue
		elif num <= 10:
			CommCostList_L.append(int(line))
			num += 1
		else:
			CommCostList_D.append(int(line))
			num += 1

with open('C:/Users/Administrator/Desktop/Async-LinUCB-master/MovLinear/SampleComplex_dataset0_05_23_01_16.csv', 'r') as f:
# with open('C:/Users/Administrator/Desktop/Async-LinUCB-master/SimLinear/AccCommCost_dataset2_05_17_08_09.csv', 'r') as f:
	num = 0
	for line in f:
		if num == 0:
			num += 1
			continue
		elif num <= 5:
			num += 1
			SampleComList_U_Hom.append(int(line))
		elif num <= 10:
			SampleComList_L_Hom.append(int(line))
			num += 1
		else:
			SampleComList_D_Hom.append(int(line))
			num += 1


# print(CommCostList_L)

# exit(0)
# # plot the results
fig, axa = plt.subplots(2, 1, sharex='all')
# Remove horizontal space between axes
fig.subplots_adjust(hspace=0.2)
# path = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/MovLinear/'
# path = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/SimLinear/'
# file_name = ['SampleComplex_dataset2_05_17_08_16', 'SampleComplex_dataset2_05_17_08_15','SampleComplex_dataset2_05_17_08_13',
# 			 'SampleComplex_dataset2_05_17_08_09', 'SampleComplex_dataset2_05_17_08_09']
# file_name = ['SampleComplex_dataset0_05_23_01_16']
# file_name = ['SampleComplex_dataset2_05_17_08_09']
# suffix = '.csv'

# values_L = [[] for _ in range(5)]  
# values_U = [[] for _ in range(5)]  
# values_D = [[] for _ in range(5)]

# for file in file_name:
# 	full_path = path+file+suffix
# 	df = pd.read_csv(full_path)
# 	for i in range(5):
# 		values_L[i].append(df.iloc[i + 0, 0])
# 		values_U[i].append(df.iloc[i + 5, 0])
# 		values_D[i].append(df.iloc[i + 10, 0])

# values_L = np.array(values_L).astype(float)
# values_U = np.array(values_U).astype(float)
# values_D = np.array(values_D).astype(float)

# mean_L = np.mean(values_L, axis=1)
# std_L = np.std(values_L, axis=1)

# mean_U = np.mean(values_U, axis=1)
# std_U = np.std(values_U, axis=1)

# mean_D = np.mean(values_D, axis=1)
# std_D = np.std(values_D, axis=1)

# print("#########0",values_L,values_U, values_D )
# print("@@@@@@@@@@@@@@@@@@@@@@22",mean_L, mean_U, mean_D)


sx = []
# syl = []
# syu = []
sylh = []
syuh = []
sydh = []

print("=====Sample Complexity=====")
# for alg_name in algorithms.keys():
# 	# if alg_name[17] == 'U' and alg_name[13:16] == 'Sin':
# 	# 	syu.append(SampleComList_U[alg_name])
# 	# 	sx.append(float(alg_name[5])/10)
# 	# 	print('%s: %.2f' % (alg_name,SampleComList_U[alg_name][-1]))
# 	# if alg_name[17] == 'L' and alg_name[13:16] == 'Sin':
# 	# 	syl.append(SampleComList_L[alg_name])
# 	# 	print('%s: %.2f' % (alg_name, SampleComList_L[alg_name][-1]))

		
# 		sylh.append(SampleComList_L_Hom)
# 		# print('%s: %.2f' % (alg_name, SampleComList_L_Hom[alg_name][-1]))
# 	if alg_name[17] == 'U' and alg_name[13:16] == 'Hom':
# 		sx.append(float(alg_name[5])/10)
# 		syuh.append(SampleComList_U_Hom)
# 		# print('%s: %.2f' % (alg_name, SampleComList_U_Hom[alg_name][-1]))
# 	if alg_name[17] == 'D' and alg_name[13:16] == 'Hom':
# 		sydh.append(SampleComList_D_Hom)
		# print('%s: %.2f' % (alg_name, SampleComList_D_Hom[alg_name][-1]))

sx = [0.1, 0.2, 0.3, 0.4, 0.5]
sylh = copy.deepcopy(SampleComList_L_Hom)
syuh = copy.deepcopy(SampleComList_U_Hom)
sydh = copy.deepcopy(SampleComList_D_Hom)

# axa[0].plot(sx, syu, marker='o', linestyle='dotted', label='UGapE')
# axa[0].plot(sx, syl, marker='o', linestyle='dotted', label='LinGapE')
axa[0].plot(sx, sylh, marker='v', linestyle='dotted', label='LinGapE-Sync')
# axa[0].fill_between(sx, mean_L-std_L, mean_L+std_L, color='red', alpha=0.2)
axa[0].plot(sx, syuh, marker='o', linestyle='dotted', label='LinGapE-Single')
# axa[0].fill_between(sx, mean_U-std_U, mean_U+std_U, color='blue', alpha=0.2)
axa[0].plot(sx, sydh, marker='s', linestyle='dotted', label='FALinPE')
# axa[0].fill_between(sx, mean_D-std_D, mean_D+std_D, color='green', alpha=0.2)
axa[0].legend(loc='upper right')
axa[0].set_xlabel("Expected Reward Gap")
axa[0].set_ylabel("SampleComplexity")



cx = []
cyl = []
cyu = []
cyd = []

cx = [0.1, 0.2, 0.3, 0.4, 0.5]
cyl = copy.deepcopy(CommCostList_L)
cyd = copy.deepcopy(CommCostList_D)

# path = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/MovLinear/'
# path = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/SimLinear/'
# file_name = ['AccCommCost_dataset0_05_22_17_47', 'AccCommCost_dataset0_05_23_01_16','AccCommCost_dataset0_05_23_01_16',
# 			 'AccCommCost_dataset0_05_22_21_26', 'AccCommCost_dataset0_05_23_02_17']
# file_name = ['AccCommCost_dataset2_05_17_08_16', 'AccCommCost_dataset2_05_17_08_15','AccCommCost_dataset2_05_17_08_13',
# 			 'AccCommCost_dataset2_05_17_08_09', 'AccCommCost_dataset2_05_17_08_09']
# file_name = ['SampleComplex_dataset0_05_23_01_16']
# file_name - ['AccCommCost_dataset2_05_17_08_09']

# suffix = '.csv'

# values_L2 = [[] for _ in range(5)]  
# values_U2 = [[] for _ in range(5)]  
# values_D2 = [[] for _ in range(5)]

# for file in file_name:
# 	full_path = path+file+suffix
# 	df = pd.read_csv(full_path)
# 	for i in range(5):
# 		values_L2[i].append(df.iloc[i + 0, 0])
# 		values_U2[i].append(df.iloc[i + 5, 0])
# 		values_D2[i].append(df.iloc[i + 10, 0])

# values_L2 = np.array(values_L2).astype(float)
# values_U2 = np.array(values_U2).astype(float)
# values_D2 = np.array(values_D2).astype(float)

# mean_L2 = np.mean(values_L2, axis=1)
# std_L2 = np.std(values_L2, axis=1)

# mean_U2 = np.mean(values_U2, axis=1)
# std_U2 = np.std(values_U2, axis=1)

# mean_D2 = np.mean(values_D2, axis=1)
# std_D2 = np.std(values_D2, axis=1)


print("=====Comm Cost=====")
# for alg_name in algorithms.keys():
# 	if alg_name[17] == 'L' and alg_name[13:16] == 'Hom':
# 		cx.append(float(alg_name[5])/10)
# 		cyl.append(CommCostList_L)
# 		# print('%s: %.2f' % (alg_name, CommCostList_L[alg_name][-1]))
# 	if alg_name[17] == 'U' and alg_name[13:16] == 'Hom':
# 		cyu.append(CommCostList_U)
# 		# print('%s: %.2f' % (alg_name, CommCostList_U[alg_name][-1]))
# 	if alg_name[17] == 'D' and alg_name[13:16] == 'Hom':
# 		cyd.append(CommCostList_D)
		# print('%s: %.2f' % (alg_name, CommCostList_D[alg_name][-1]))
axa[1].plot(cx, cyl, marker='v', linestyle='dotted', label='LinGapE-Sync')
# axa[1].fill_between(cx, mean_U2-std_U2, mean_U2+std_U2, color='blue', alpha=0.2)
# axa[1].plot(cx, cyu, marker='o', linestyle='dotted', label='LinGapE-Single')
axa[1].plot(cx, cyd, marker='s', linestyle='dotted', label='FALinPE')
# axa[1].fill_between(sx, mean_D2-std_D2, mean_D2+std_D2, color='red', alpha=0.2)
axa[1].set_xlabel("Expected Reward Gap")
axa[1].set_ylabel("Communication Cost")
axa[1].legend(loc='upper right')
# plt.savefig(os.path.join(save_Linear_Case, "SamConAndCommCost_dataset" + self.dataset + str(timeRun) + '.pdf'), dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.savefig('test.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.show()


