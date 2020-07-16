# travelling-salesman
All the code I write while doing [a Coursera course on the TSP](https://www.coursera.org/learn/delivery-problem)

[pathlength.py](pathlength.py): Calcluates the total weight of a specified path through a specified graph  
[random_bruteforce.py](random_bruteforce.py): Bruteforce search for best path but generates random paths instead of working through them logically due to the fact that brute force is O(n!) which makes a full search impractical for most graphs, runs indefinetly until killed  
[random_bruteforce.py](random_bruteforce.py): Picks a random starting node then picks the nearest node, then picks the nearest node to the one it just went to and so on, goes through all possible starting nodes unless killed prior to halting
## Copyright
Copyright © 2020  Rory Sharp All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with this program.  If you have not received this, see <http://www.gnu.org/licenses/gpl-3.0.html>.

For a (non-legally binding) summary of the license go to https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)
