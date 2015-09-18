# Assignment2
ai3202 hw3

command line: python hw3.py <World1/2>.txt <manhattan/custom>

The second heuristic is exe using 'custom' instead of 'manhattan' for the third arguement. The Equation uses the euclidean distance and also has an if statement to avoid paths that end lead to a corner. The euclidean distance is just the pythagorean theorem with the remaining rows and columns as the x and y values. I thought this would be a good heuristic because by keeping the diagonal distance miimized it provides the algoritm incentive to take to shortest path. The performance for both worlds was initially worse than the manhattan. Manhattan, world1:156. Manhattan, world2: 150. Custom world1:166. Custom, world2:144. The only reason the custom heuristic is more efficient on world2 is the if statement that avoids the corner in the bottom left corner of the map.

