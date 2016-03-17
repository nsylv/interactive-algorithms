# interactive-algorithms
Inspired by 6.006, a collection of algorithms and datatypes (that I may later develop to be interactive, but for now are just *hopefully* well-commented)

##Algorithms
The collection of algorithms I have written
* [Rabin Karp](algorithms/rabinkarp.py) ~ `O(n)` ~ Rabin-Karp substring searching algorithm
* [Rabin Karp Multi](algorithms/rabinkarpmulti.py) ~ `O(n+k)` ~ Rabin-Karp substring searching algorithm for a list of patterns, each of length *k*

##ADTs
The collection of abstract datatypes (ADTs) I have written
* [Rolling Hash](adts/rollinghash.py) ~ Rolling Hash datatype
 * get_number(item) ~ `O(1)` ~ converts the item into a number value
 * value() ~ `O(1)` ~ returns the hash of the list
 * append(item) ~ `O(1)` ~ adds item to the end of the list
 * skip(item) ~ `O(1)` ~ removes first item from list, assuming that it is item
