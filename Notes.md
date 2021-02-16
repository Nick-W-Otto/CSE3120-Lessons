#CSE 3120 Object-Oriented Programming 1 Notes

## Definitions 

__Object-Oriented Analysis (OOA)__ is the process of looking at a problem, system or task and identifying the objects and interactions between those objects. It answers the question of _what needs to be done_?

__Object-Oriented Design (OOD)__ is the processing of converting the identified objects and interactions from OOA into objects behaviours. It answers the question _how things need to be done_?
* How things interact with eachother.

__Object-Oriented Programming (OOP)__ is the processing of implementing the outcome of OOD into a functioning program. 

A __Class__ is a model of an object. Classes contain _attributes_ and _behaviours_ which are inherited objects instantiated from the class. Another way of thinking of a class is a blueprint or template of data storage and manipulation

* Classes often use PascalCase in naming 
  
An _attribute_ is a property or characteristic an object possess. Each object can have a different value for the attribute, but all objects instantiated from the class inherits attributes. other names for attributes are _member's_ and _properties_
* Attributes often use lowercase in naming In addition snake_case is often used too

A _behaviours_ is a action that can be performed on a object. Behaviours are formally called methods and are written the same as a function. Therefore, methods can also accept arguments into their parameters and return values.

* One major advantage to methods is that they automatically have access to all attributes within the object, Therefore, object attributes neither need to be passed as an argument. Nor Goballed into the method
* Methods always have at least one argument. ```self```, which indicates that the function references the current object
    *__Constructors__ are methods that provide the object with default set of attributes. In python, it is ```self.init(self)```. Constructors create the object from the class template with values within the attributes. The constructor can have arguments that are passed to the object's attributes. Other attributes can be defaulted of the class
     *In general, all attributes of the object should be present in the constructor even if their default value is None.
```python   
class Die:
    """Creating the class for the die"""
    def __init__(self, MAX_VALUE):
        """Constructor method to create the Die """
        self.MAX_VALUE = MAXVALUE # Attribute of the die object 
        self.VALUE = NONE

```
An __Object__ is a unique set of data and functions instantiated from a class An object assesses attribute and methods using _Dot notation_. which identifies the object, then the attribute or value

```python
<object>.<attribute> ==> VALUE
<object>.<method>(parameters) ==> runs the method
```

### Overloading Methods(IB)
Methods can be overloaded where they have the same name but different parameters. this is typically a advanced process 

### God/System objects

As with many methodologies, there is a right way and wrong way to follow the methodology. For example, using only global variables in functional programming making it more similar to structural programming. Similarly, writing a program with only class/object. results in a program similar to functional programming.

## Why OOP?
1.) __Encapsulation__ is the process of protecting or hiding data throughout the use of an _interface_ The interface is often a collection of methods, such as setter(Modifier) and Getter(Accessors) Methods, that other objects can interact with. 
* A television encapsulates all the hardware and software into a small box in which the user interacts with using with a interface called a remote control
* The Setter and Getter methods are the buttons on the interface 

2.) __Abstraction__ is the process of setting the level of detail and complexity for wat is appropriate for the given task
    * A Driver only needs to interact with the steering, accelerator, and brakes of the car to drive, But a mechanic has a much more complex understanding of the car in order to repair and maintain it. Therefore, the mechanic's abstraction of the car is more complex. 

3.) __Aggregation__ This the process of grouping objects together. Objects exist independently of each-other, but changing one does not change the other of the group 

4.) __Composition__ Is the process of creating a complex object by creating several objects together 
    * A car is composed of an engine, transmission, starter, headlights, windshield, etc. Each of the car's objects have attributes and behaviours such as the engine's pistons, values and crack shaft/ If the car is missing an object from its composition the car no longer functions 
    * All Compositions are Aggregations but not all Aggregations are Compositions. Compositions have interdependence between aggregate objects. 
 
