https://docs.python.org/3/faq/programming.html

https://python-patterns.guide/gang-of-four/singleton/

Quick notes
* Note that using a module is also the basis for implementing the Singleton design pattern, for the same reason. 
* But, otherwise, the pattern is best avoided in favor of following the advice of the official Python FAQ and using the The Global Object Pattern.
* While the Gang of Four’s original Singleton Pattern is a poor fit for a language like Python that lacks the concepts of new, private, and protected, it’s not as easy to dismiss the pattern when it’s built atop __new__() — after all, singletons were part of the reason the __new__() dunder method was introduced!
* A tuple of length one is called a singleton. 
* Modules are “singletons” in Python because import only creates a single copy of each module; subsequent imports of the same name keep returning the same module object. 
  

