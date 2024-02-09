# Pure Exploration for Asynchronous Federated Bandits

**Introduction**

This project investigates the federated pure exploration problem within multi-armed and linear bandits settings, where multiple agents collaborate to identify the best arm under communication with a central server. Addressing common issues like latency and unavailability of clients in practical scenarios, we introduce the first federated asynchronous algorithms for multi-armed bandit (MAB) and linear bandit models aimed at pure exploration with fixed confidence. Our approach balances the exploration-exploitation trade-off efficiently, even in fully asynchronous environments, enhancing robustness against delays and agent unavailability while minimizing communication costs.


**Main Code**

This repository contains implementation of the proposed algorithms UGapE, LinGapE, and FALinPE for comparison. 

For experiments on the synthetic dataset, run: 
SimLinear.py 
SimTabular.py

Experiment results can be found in "./SimTabular/" and "./SimLinear/ folder, which contains: 

"SamConAndCommCost_[startTime].png/pdf": plot of accumulated regret / communication cost over time for each algorithm 

"SampleComplex_dataset[number][startTime].csv": sample complexty at each iteration for each algorithm_ 

"AccCommCost_dataset[number][startTime].csv": communication cost at each iteration for each algorithm_


For experiments on realworld dataset (MovieLens): 
Available dataset and file scripts for data processing and feature vector generationare given in "./Dataset" folder.
Experiment results can be found in "./MovieLinear/" folder。

run plot_v.py
