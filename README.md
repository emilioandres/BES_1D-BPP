# BES_1D-BPP
BES Algorithm to solve Bin Packing Problem
The unidimensional bin packing is a combinatorial optimization problem that involves packing objects of different sizes into containers (also known as "bins") with limited capacity. The goal is to use the fewest number of containers possible to pack all the objects.

The problem can be stated as follows: you have a list of objects, each with a specific size, and containers with fixed capacity. The objective is to determine how to distribute the objects into the containers in a way that minimizes the number of containers used.

There are different approaches to solving this problem, but one of the most common is the "First-Fit" algorithm. In this approach, the objects are processed in order and placed into the first available container that can accommodate them. If there is no available container that can fit the object, a new container is used. This process continues until all the objects have been placed into containers.

The First-Fit algorithm has a time complexity of O(n log n), where n is the number of objects. However, there are variants and more sophisticated algorithms that can improve efficiency in certain cases.

It's important to note that the unidimensional bin packing problem is known as "NP-hard," which means that there is no known polynomial-time optimal solution for all cases. Therefore, the algorithms used generally provide approximate or heuristic solutions that approach the optimal solution but do not guarantee it.
