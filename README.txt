BASIC WALKTHROUGH:
The router.py file in the project route is just a shell which calls the fuinctionality in classes/ in a way that's compliant with the specification. The classes in classes/ are as follows.
Router: Communicates with other routers and with its own routing table
Routing table: Manages routes and shares routes with other routing tables via its router.
Route: Conatains routers and sub-routes and can instatiate more routes and talk to routers.
Hopefully you'll forgive the circular dependancy evident in the above description. There are a lot of things in this project that a stricter language like Java would not have allowed, but that's why we use python afterall.

COMPLETION:
Part 1 and 4 are complete, these were actually done simulataneously due to the way I decided to implement it.
Part 2 is done
Part 3 is not done

EXTRAS:
Because I decided to make a wholistic implementation first and worry about the spec afterwards, there are a lot of little features that never ended up being used, mostly things to increase robustness like validity checks and self-correction. Though none especially stand out as candidates. I can't even say my object-oriented design is especially worthy of praise. One thing I am proud of is my solution to part 2: I managed to fit in three *disgusting* lines, what others used an external dependancy for. Eight list comprehensions, two joins, and a format in three lines! So I decided for my extra that I would make this a one line function (using lambdas which, I know, is cheating). Please enjoy/despair.

