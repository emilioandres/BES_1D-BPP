# BES_1D-BPP
BES Algorithm to solve Bin Packing Problem
The unidimensional bin packing is a combinatorial optimization problem that involves packing objects of different sizes into containers (also known as "bins") with limited capacity. The goal is to use the fewest number of containers possible to pack all the objects.

The problem can be stated as follows: you have a list of objects, each with a specific size, and containers with fixed capacity. The objective is to determine how to distribute the objects into the containers in a way that minimizes the number of containers used.

There are different approaches to solving this problem, but one of the most common is the "First-Fit" algorithm. In this approach, the objects are processed in order and placed into the first available container that can accommodate them. If there is no available container that can fit the object, a new container is used. This process continues until all the objects have been placed into containers.

The First-Fit algorithm has a time complexity of O(n log n), where n is the number of objects. However, there are variants and more sophisticated algorithms that can improve efficiency in certain cases.

It's important to note that the unidimensional bin packing problem is known as "NP-hard," which means that there is no known polynomial-time optimal solution for all cases. Therefore, the algorithms used generally provide approximate or heuristic solutions that approach the optimal solution but do not guarantee it.



$\alpha$: Referred to as "alpha" in the implementation, ranging from 1.5 to 2, this parameter belongs to the space selection stage. The value set in the algorithm is 1.5. This parameter is associated with the magnitude of change that controls the eagle's movement. In this case, the minimum value is used to obtain low variation in the new values.

$a$: Referred to as "a_factor" in the implementation, this parameter belongs to the space search stage and ranges from 5 to 10. The chosen value is 8, as the parameter is associated with the bald eagle's movement towards the best median value within the search space. A very small value shortens the search within the space.

$R$: Referred to as "R_factor" in the implementation, ranging from 0.5 to 2, these parameters are present in the search stage. In this case, a value of 1 is considered, as a very small value performs a highly constrained search and does not converge to optimal values. Likewise, very large values oscillate between optimal and worse solutions.

$c1 c2$: The values c1 and c2 range from 1 to 2. These values are present in the swoop stage. A value of 2 is chosen for both parameters because equal weight is assigned to the best value ($P_{best}$) and the current mean value ($P_{mean}$). These parameters allow the solution to oscillate between the best value and the current mean value, without assigning extra weight to the solutions. This way, other solutions can be explored that may lie between these positions.

$popSize$: The popSize is a parameter ranging from 1 to 40, allowing the algorithm to converge faster but also increasing computational complexity. This parameter is associated with the swarm, and in this implementation, it relates to the number of variations applied to the points obtained during the flight of the bald eagle, specifically the number of points within the search spiral and the swoop. The chosen value for this parameter is 15, as tests were conducted with sizes ranging from [5, 25], and it was concluded that a size above 20 involves execution times exceeding 9 seconds.

$maxIter$: It is a parameter related to the number of algorithm iterations. This parameter is set to 50, considering the execution times and the convergence speed of the algorithm.

The results:

![imagen](https://github.com/emilioandres/BES_1D-BPP/assets/20390219/4b67c4cb-237a-46ee-91d5-2418b334dd33)


![imagen](https://github.com/emilioandres/BES_1D-BPP/assets/20390219/64fe9536-f6bd-4905-a084-7885876c7028)


