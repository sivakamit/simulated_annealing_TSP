# Simulated annealing TSP

Traveling salesman problem can be solved by using simulated annealing technique which can be optimized. Annealing is the process where the temperature is increased to the high temperature and then gradually reducing the temperature, this eliminates local minimum. In simulated annealing the temperature is decreased from the high temperature to get the optimized cost of the path (distance). When the temperature is high, huge random changes are made which avoids the risk of getting trapped in the local maxima. The temperature falls in the series of exponential decay. 

The process of annealing in solving the problem starts from listing all the cities in the order and then selecting random positions from the order. In each step, the transforms of the route is made randomly. The segment of the path is selected, where start and end cities are randomly selected. 

The first iteration starts with the random tour. Select a random city from the neighbors of the existing tour. This is done by selecting two random cities and reverse the order in the middle. This tour would be better or worse than the existing tour. If the tour is better, then it is considered as the new tour. If the tour is worst than the actual tour, this is also considered with the certain probability. The higher temperature is likely to accept the worse tour. Lowering the temperature in every iteration till the end temperature. this is done till the minimum.


  
## Comparisons
Case 1:

initial_temp = 1000

end_temp = 0.00000001

desc_factor = 0.9995

iteration = 10000000

<img width="379" alt="image" src="https://user-images.githubusercontent.com/38185827/187320656-ddeb7af9-7517-469b-a723-de4315a8737f.png">

 
Case 2:

initial_temp = 500

end_temp = 0.00000001

desc_factor = 0.9995

iteration = 5000000

<img width="370" alt="image" src="https://user-images.githubusercontent.com/38185827/187320720-e78c555b-6c2f-4bde-9802-9356930ab58d.png">

 
Case 3:

initial_temp = 1200

end_temp = 0.00000001

desc_factor = 0.9995

iteration = 10000000

<img width="366" alt="image" src="https://user-images.githubusercontent.com/38185827/187320773-d3bf16df-1c96-44ac-926b-0025ad299435.png">

 

Case 4:

initial_temp = 1500

end_temp = 0.00000001

desc_factor = 0.9995

iteration = 100000

<img width="368" alt="image" src="https://user-images.githubusercontent.com/38185827/187320855-e1ac36f7-8500-42b4-862a-61d71141e415.png">

 

Case 5:

initial_temp = 696

end_temp = 0.00000001

desc_factor = 0.9995

iteration = 100000

<img width="366" alt="image" src="https://user-images.githubusercontent.com/38185827/187320893-3b448257-09bf-42d0-a47c-8212e86ff7c2.png">
