**Decorator Pattern**
- Structural Pattern that allow you adding new behaviours to objects dynamically by them inside special wrapper objects.
- Wrapper is alternative name for Decorator Pattern
- It takes Composition approach instead of Inheritance. 

- Structure
  - Interface
  - Concrete class
  - Base Decorator for Interface
  - Concrete Decorator
  - Client Code

**What problem it is solving?**

  - creating two many subclass as per the new requirements
  - altering behaviour of the object in runtime. Through inheritance, it can't be achivable
  - multiple inheritance doesnt not supported by most languages.

**Examples where it can be used:**
  - Notifier Service ( email, sms, slack , etc)
  - Product customization ( Wok to walk , pizza toppings, etc)
  - File Input stream ( unzip, buffer , deserialise )
  
**Related with other patterns**
Few patterns apply similar composition principle but intents are different

- Adapter pattern
- Chain of Responsibility
- Strategy
- Proxy 
  
**Reference Links**
- https://refactoring.guru/design-patterns/decorator