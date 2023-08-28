# Exercise 3.4 notes

- General rule: internal (private) attributes for a class should have a leading underscore for legibility
- `@property` and `@<property>.setter` decorators:
    - The `@property` decorator sets a getter property for a method, allowing us to use the method as an attribute. This allows us to perform extra functions when getting/setting the property

# Exercise 3.6
- Say we want to redirect our python output to a file
- One way to do this is to wrangle our code to allow for file r/w, but we can also use *context managers*
- Context managers redirect output from `sys.stdout` to somewhere else

# Exercise 3.7
- How do we *really ensure* that an object will work correctly?
    - Python has weak type-checking, so even if an object inherits from the right base class, the derived class may be implemented improperly and break
- We can solve this by using Python's `abc` module
    - The base class should inherit from `ABC`, and each abstract method should have the `@abstractmethod` decorator
