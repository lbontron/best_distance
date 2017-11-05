# best_distance
Machine learning for calcul best distance

This program is a basic example of machine learning.

################################ How does it work #######################################
You construct a matrix distance

for example : 
# | A | B | C | D | E |...
A |000|451|264|166|675|...
B |451|000|145|333|567|...
C |264|145|000|453|099|...
D |166|333|453|000|627|...
E |675|567|099|627|000|...
..|...|...|...|...|...|...

We want go through all city. The start city is A and the end city is E
If we have 5 cities, we have choice : (nb city - 2 (start and end))!
(ABCDE, ABDCE, ACBDE, ACDBE, ADBCE, ADCBE)
if we have 100 city, we have 100! choice = 2,4E18 choice...

This program use a genetic algorithm for find a solution. The solution can be the best, but it's not sure...
The program find n random path
For example with 12 cities : A : start, L : end
We associate a path, with a distance and a probability = f(distance, distanceMin, distanceMax) 
ADGIHFKJCBEL,  4587, 0.70
AEGKCIJFBHDL,  3289, 0.85
ADGJEHKBIFCL, 19264, 0.15
ADHIEFGJKBCL,  7645, 0.55
AJKEDGFCIHBL,  6565, 0.45
A..........L, ....., 0...

The program select 2 path depending on the probability and generate a new individu (a mutate of the 2 individu selected)
 AEGKCIJFBHDL
&AEGDKIJFBCHL
-------------
 AEGKCIJFBHDL

The program calcul the distance and the probability of the new generation.

Start example.py for understand the software
