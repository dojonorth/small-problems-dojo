##Introduction

There are three small coding problems that we'd like you to solve in two different ways, with a little 'extra-credit' at the end for the really keen.

We're open for you to use any language in solving these problems - with a view to discussing pros and cons for each at the end. And the ways in which you solve them is up to you. If you're stuck for a second way, try thinking of a constraint (such as 'now solve it without any loops') and how you would go about recoding your solution while meeting that constraint.

##The Problems:

1. **Write a palindrome tester.**

   Given a string (such as "Amore, Roma"), return a boolean stating whether this is a valid palindrome.
   
2. **Parentheses evaluator**

   Given a string, test whether it has fully balancing parentheses (of a mixed type - eg "hello, (these [are some]) {parentheses}")
   
###Extra credit:

* **Factorial calculator**
  
   * Return the factorial of a number. For example, 4! = 4 * 3 * 2 * 1 = 24
   * Benchmark your solutions. How do they perform? Is there a way you could make any of your solutions faster?

##Testsuites

We've provided a couple of sample testsuites for your solutions, one in Python,
    one in Java and one in Scala. These aren't prescriptive - you don't have to use either of
    the languages or the test suites given, but merely a starting point or some
    inspiration.

###Python

The Python suite has been tested with Python2.7, but it is simple enough that it
should run under most versions of Python2 with little to no modifications.

To run the entire suite use:

```
python -m unittest discover .
```

And to run a set of tests for a single solution, you should be able to run it directly from the test
file:

```
python test_palindrome.py
```

###Scala

You will need SBT installed. From within the scala directory enter the sbt console:

```
sbt
```

Then, to run the entire test suite use:

```
test
```

To run just one suite use:

```
test-only *PalindromeSuite
```

###
