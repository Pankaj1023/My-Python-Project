Python is an object-oriented programming language, which means it deals with objects. Everything in Python is an object, including numbers, strings, lists, and even functions. Objects have attributes and methods associated with them.

Numbers:

Python supports various types of numbers, including integers, floating-point numbers, and complex numbers.

Integer:
Represents integers (whole numbers).


[ ]
num_int = 42
print(num_int)
print(type(num_int))
42
<class 'int'>
Float

[ ]
num_int_error = 3.14
print(num_int_error)
print(type(num_int_error))
3.14
<class 'float'>
Complex

[ ]
num_complex = 2 + 3j
print(num_complex)  #
print(type(num_complex))
(2+3j)
<class 'complex'>
Bool: Booleans represent truth values, either True or False.


[ ]
bool_true = True
print(bool_true)
print(type(bool_true))

True
<class 'bool'>

[ ]
bool_false = False
print(bool_false)
print(type(bool_false))
False
<class 'bool'>
Set:

A set is an unordered collection of unique elements. Sets are mutable, meaning they can be modified after creation, but they cannot contain duplicate elements.


[ ]
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))
{1, 2, 3, 4, 5}
<class 'set'>

[ ]
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)
print(type(my_dict))

{'name': 'John', 'age': 25, 'city': 'New York'}
<class 'dict'>
Sequence:

Strings in Python are sequences of characters enclosed in single, double, or triple quotes. They support various operations such as concatenation, slicing, and formatting.


[ ]
my_str = "Hello, World!"
print(my_str)
print(type(my_str))

Hello, World!
<class 'str'>
List:

A list is a versatile data structure used to store collections of items. Lists are mutable, meaning they can be modified after creation. Each item in a list is indexed, and you can access elements by their index. Lists can contain items of different data types, and they can also contain other lists (nested lists).


[ ]
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

[1, 2, 3, 4, 5]
<class 'list'>
Tuple:

A tuple in Python is a collection of ordered and immutable elements. It is similar to a list, but unlike lists, tuples are immutable, meaning their elements cannot be changed after creation. Tuples are defined using parentheses () and can contain elements of different data types.


[ ]
my_tuple = (1, 'two', 3.0)
print(my_tuple)
print(type(my_tuple))

(1, 'two', 3.0)
<class 'tuple'>
None:

None is a special constant representing the absence of a value or a null value. It is often used to indicate that a variable or an object does not have a meaningful value or has not been assigned yet.


[ ]
my_none = None
print(my_none)
print(type(my_none))

None
<class 'NoneType'>