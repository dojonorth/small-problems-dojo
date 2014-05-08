##Introduction

This dojo is going to be more fragmented than the first 'minesweeper' one. There are three small coding problems that we'd like you to solve in two different ways, with a little 'extra-credit' at the end for the really keen.

We're open for you to use any language in solving these problems - with a view to discussing pros and cons for each at the end. And the ways in which you solve them is up to you. If you're stuck for a second way, try thinking of a constraint (such as 'now solve it without any loops') and how you would go about recoding your solution while meeting that constraint.

##The Problems:

1. **Write a palindrome tester.**

   Given a string (such as "Amore, Roma"), return a boolean stating whether this is a valid palindrome.
   
2. **Parentheses evaluator**

   Given a string, test whether it has fully balancing parentheses (of a mixed type - eg "hello, (these [are some]) {parentheses}")
   
3. **Factorial calculator**
  
   Return the factorial of a number. For example, 4! = 4 * 3 * 2 * 1 = 24

###Extra credit:
Benchmark your solutions. How do they perform? Is there a way you could make any of your solutions faster?

##Testsuites

We've provided a couple of sample testsuites for your solutions, one in Python,
    and one in Java. These aren't prescriptive - you don't have to use either of
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

### Immediate todo list

- [x] Draft readme
- [ ] Write test suites for dynamically typed language
- [ ] Write test suites for statically typed language
- [ ] Test the test suites
- [ ] ??? do we provide benchmarking tools, or should that be left as a task for the participant?
