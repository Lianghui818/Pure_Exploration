'''
Created on May 12, 2015
'''
import os

save_LinGapE_address = "C:/Users/Administrator/Desktop/Async-LinUCB-master/LinGapE_Simulations"
Singe_UGapE_address = "C:/Users/Administrator/Desktop/Async-LinUCB-master/Sin_UGapE_Simulations"
sim_files_folder = "C:/Users/Administrator/Desktop/Async-LinUCB-master/Simulation_MAB_files"
save_address = "C:/Users/Administrator/Desktop/Async-LinUCB-master/SimulationResults"
LastFM_save_address = "C:/Users/Administrator/Desktop/Async-LinUCB-master/LastFMResults"
Delicious_save_address = "C:/Users/Administrator/Desktop/Async-LinUCB-master/DeliciousResults"
MovieLens_save_address = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/MovieLensResults'
save_Single_Agent = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/SimSingleAgent'
save_Tabular_Case = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/SimTabular'
save_Linear_Case = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/SimLinear'
save_Linear_Movie_Case = 'C:/Users/Administrator/Desktop/Async-LinUCB-master/MovLinear'

save_addressResult = "C:/Users/Administrator/Desktop/Async-LinUCB-master/Results/Sparse"

datasets_address = 'C:/Users/Administrator/Desktop/Async-LinUCB-master'  # should be modified accoring to the local address

LastFM_address = datasets_address + '/Dataset/hetrec2011-lastfm-2k/processed_data'
Delicious_address = datasets_address + '/Dataset/hetrec2011-delicious-2k/processed_data'
MovieLens_address = datasets_address + '/Dataset/ml-20m/processed_data'

LastFM_FeatureVectorsFileName = os.path.join(LastFM_address, 'Arm_FeatureVectors_2.dat')
LastFM_relationFileName = os.path.join(LastFM_address, 'user_friends.dat.mapped')

Delicious_FeatureVectorsFileName = os.path.join(Delicious_address, 'Arm_FeatureVectors_2.dat')
Delicious_relationFileName = os.path.join(Delicious_address, 'user_contacts.dat.mapped')

MovieLens_FeatureVectorsFileName = os.path.join(MovieLens_address, 'Arm_FeatureVectors_2.dat')
MovieLens_relationFileName = os.path.join(MovieLens_address, 'user_contacts.dat.mapped')