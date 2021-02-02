**In Absense of Builder Pattern**
- Option 1 : Creating too many subclasses 
- Option 2 : Fat Constructor with all possible multiple parameters which may be optional or unwanted.
- Option 3 : Overload constructors with many combination of parameters
- Multiple Constructors with different parameters

__**Builder Pattern**__
- Use Single Responsibility Principle
- Focus on building complex object step by step
- Relation with other patterns : *Prototype*, *Abstract Factory*


**Builder Interface**
- Define all possible construction steps
- if you want to give all the list of steps to be followed in order a product, define the steps here.

**Concrete Builders**
- Implement the consturction steps to build a particular product as result 
- If you want to build different type of product varitions , develop different concrete builders and respective implementation

**Director**
- Director class guide the order of construction and client can pass the inputs
- If you want to change the order of constuction. Modify only this class 

Examples in real use cases :

1. Spark API
2. Pandas Dataframe libraries
