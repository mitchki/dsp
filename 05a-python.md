# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>Both are a list of numbers,that can be referred to via an index value starting at zero.  

>>Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Tuples can be accessed either by index or by named keys (in which case they're named tuples.) Since lists can only be accessed via numbered indexes, they are not good as keys for dictionaries.

>>Lists are mutable (changeable), and their elements are usually homogeneous and are accessed by iterating over the list.  
>>Lists are represented in square brackets, tuples in parentheses.

>>Named tuples will work as keys in dictionaries as their elements are associated by name with each entry.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets contain only unique elements and their elements are immutable.  Lists are changeable (not immutable) and may contain duplicates.

Example list: ` cities = ["London", "New York", "Raleigh", "London", "Miami" ]`

Example set:  ` cities = {"London", "New York", "Raleigh"}`

Membership testing in a set is vastly faster, especially for large sets. That is because the set uses a hash function to map to a bucket. Since Python implementations automatically resize that hash table, the speed can be constant (O(1)) no matter the size of the set (assuming the hash function is sufficiently good).

In contrast, to evaluate whether an object is a member of a list, Python has to compare every single member for equality, i.e. the test is O(n).




---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is a construct in python that creates an anonymous function.  It can be used anywhere you need a simple function that will not be reused (and therefore doesn't need a name.)

```
>>> words = "This is my list of words for the sorted and lambda exercise".split()
>>> words
['This', 'is', 'my', 'list', 'of', 'words', 'for', 'the', 'sorted', 'and', 'lambda', 'exercise']
>>> sorted(words, key = lambda l: len(l))
['is', 'my', 'of', 'for', 'the', 'and', 'This', 'list', 'words', 'sorted', 'lambda', 'exercise']
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions use 'for' and/or  'if' statements to build a list. 
```
>>> words = "This is my list of words for the list comprehension exercise".split()
>>> words
['This', 'is', 'my', 'list', 'of', 'words', 'for', 'the', 'list', 'comprehension', 'exercise']
>>> stuff = [[w.upper(), w.lower(), len(w)] for w in words]
>>> stuff
[['THIS', 'this', 4], ['IS', 'is', 2], ['MY', 'my', 2], ['LIST', 'list', 4], ['OF', 'of', 2], ['WORDS', 'words', 5], ['FOR', 'for', 3], ['THE', 'the', 3], ['LIST', 'list', 4], ['COMPREHENSION', 'comprehension', 13], ['EXERCISE', 'exercise', 8]]

>>> stuff2 = [[w.upper(), w.lower(), len(w)] for w in words if len(w) > 2]
>>> stuff2
[['THIS', 'this', 4], ['LIST', 'list', 4], ['WORDS', 'words', 5], ['FOR', 'for', 3], ['THE', 'the', 3], ['LIST', 'list', 4], ['COMPREHENSION', 'comprehension', 13], ['EXERCISE', 'exercise', 8]]


``` 
The above examples use list comprehension to build lists of lists, each sublist with 2 string elements and an integer.



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





