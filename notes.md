# Basics 

* Abstraction
* Encapsulation
* Polymorphism
* Inheritance



# OO Principles

* Encapsulate what varies.
* Favor composition over inheritance.
* Program to interfaces, not implementations.
* Strive for loosely coupled designs between objects that interact.
* Classes should be open for extension but closed for modification.
* Depend on abstractions. Do not depend on concrete classes.
* Only talk to your friends.
* Don’t call us, we’ll call you.
* A class should have only one reason to change.
* Return and pass around objects (of a generic type), not raw data
* Use a push model rather than a pull model -- push info to delegate so it can do its work



# Patterns

## Creational
* Abstract Factory
* Factory Method
* Singleton
* (Prototype)
* (Builder)


## Behavioral
* Template Method
* Strategy
* Iterator
* Command
* State
* Observer (Pub/Sub)
* (Interpreter)
* (Chain of responsibility)
* (Memento)
* (Visitor)
* (Mediator)


## Structural
* Adapter
* Façade
* Decorator
* Composite
* (Flyweight)
* (Bridge)
* (Proxy)



# Holub on Patterns Lessons

* OO design is the CIA, need-to-know school of program design.
* An object is defined by what it can do, not by how it does it -- it's a bundle of capabilities
* An OO system is one where intelligent objects (computational animals) are inside the machine sending message to one another.
* Getters and setters are evil (when it violates encapsulation).  Don't use get/set just to provide access to a field.
* Extends is evil (because you lose flexibility)
* Losing flexibility, coupling, and fragile base class are challenges in OO design.
* Fragile base class (FBC) means a change to the base class causes derived classes to malfunction.
* FBC changes may cause problems in the entire hierarchy and in code that depends on those objects.
* Coupling can be avoided by hiding implementation details. Fields that aren't constant should always be private.
* Explicit use of concrete class names locks you into specific implementation making down the line changes difficult.
* Agile development is coding without a strict, monolithic design. Rather, prioritized features are built now while also accomodating future needs.
* Polymorphism is the ability to have multiple implementations of the same type. A system that doesn't use Polymorphism isn't object oriented.
* Complexity of an OO sytem is proportional to the amount of data that flows between objects.
* Extends is appropriate when code would otherwise be copied. "Normalizing" code.
* Composition versus inheritance. "Is-a" isn't always the best way to determine inheritance.
* Inheritance should be determined by the operations that are shared
* Adding a malicious method -- the only solution is encapsulation
* 80% of code base should be written in terms of interfaces
* Patterns are discovered not invented
* A pattern is a general technique -- not a specific solutionA piece of code demonstrating the pattern is not the pattern itself.
* Classes and objects can participate in multiple patterns simultaneously
* Patterns can look the same but differ in dynamic behavior
* Reify -- to make real. A pattern is reified by a design, not an instance
* As a rough estimate, a class takes two to three weeks to implement
* Factory method adds no new functionality/operations



# UML Diagrams

To-do
* Sequence diagrams
* Static-model diagram



# CRC Cards

To-do
* Class
* Reponsibility
* Collaborates With