About Tabl
============

Lightweight, intuitive and fast data-tables.

*Tabl* data-tables are tables with columns and column names, rows and row
numbers. Indexing and slicing your data is analogous to numpy array's. The
only real difference is that each column can have its own data type.


Design objectives
-----------------

I got frustrated with pandas: it's complicated slicing syntax (.loc, .x,
.iloc, .. etc), it's enforced index column and the Series objects I get when I
want a numpy array. With Tabl I created the simplified pandas I need for many
of my data-jobs. Just focussing on simple slicing of multi-datatype tables and
basic table tools.

* Intuitive simple slicing.

* Using numpy machinery, for best performance, integration with other tools
  and future support.

* Store data by column numpy arrays (column store).

* No particular index column, all columns can be used as the index, the choice
  is up to the user.

* Fundamental necessities for sorting, grouping, joining and appending tables.


Install
========

pip install tabl

Quickstart
===========

init
----

To setup a Tabl:

>>> from tabl import Tabl
>>> tabl = Tabl([ ["John", "Joe", "Jane"],
...                [1.82,1.65,2.15],
...                [False,False,True]], columns = ["Name", "Height", "Married"])
>>> tabl
 Name   |   Height |   Married
--------+----------+-----------
 John   |     1.82 |         0
 Joe    |     1.65 |         0
 Jane   |     2.15 |         1
3 rows ['<U4', '<f8', '|b1']

Alternatively, Tabls can be setup from dictionaries, numpy arrays, pandas
DataFrames, or no data at all. Database connectors usually return data as a list
of records, the module provides a convenience function to transpose this into a
list of columns.

slice
-----

Slicing can be done the numpy way, always returning Tabl objects:

>>> tabl[1:3,[0,2]]
 Name   |   Married
--------+-----------
 Joe    |         0
 Jane   |         1
2 rows ['<U4', '|b1']

Slices will always return a Tabl except in three distinct cases, when:

1. explicitly one column is requested, a numpy array is returned:

>>> tabl[1:3,'Name']       # doctest: +SKIP
array(['Joe', 'Jane'],
      dtype='<U4')

2. explicitly one row is requested, a tuple is returned:

>>> tabl[0,:]
('John', 1.82, False)

3. explicitly one element is requested:

>>> tabl[0,'Name']
'John'

In general, slicing is intuitive and does not deviate from what would expect
from numpy. With the one addition that columns can be referred to by names as
well as numbers.

set
----

Setting elements works the same as slicing:

>>> tabl = Tabl({'Name' : ["John", "Joe", "Jane"], 'Height' : [1.82,1.65,2.15], 'Married': [False,False,True]})
>>> tabl[0,"Name"] = "Jos"
>>> tabl
 Name   |   Height |   Married
--------+----------+-----------
 Jos    |     1.82 |         0
 Joe    |     1.65 |         0
 Jane   |     2.15 |         1
3 rows ['<U4', '<f8', '|b1']

The datatype that the value is expected to have, is the same as the datatype a
slice would result into.

Adding columns, works the same as setting elements, just give it a new name:

>>> tabl = Tabl({'Name' : ["John", "Joe", "Jane"], 'Height' : [1.82,1.65,2.15], 'Married': [False,False,True]})
>>> tabl['new'] = [1,2,3]
>>> tabl
 Name   |   Height |   Married |   new
--------+----------+-----------+-------
 John   |     1.82 |         0 |     1
 Joe    |     1.65 |         0 |     2
 Jane   |     2.15 |         1 |     3
3 rows ['<U4', '<f8', '|b1', '<i8']

Or set the whole column to the same value:

>>> tabl = Tabl({'Name' : ["John", "Joe", "Jane"], 'Height' : [1.82,1.65,2.15], 'Married': [False,False,True]})
>>> tabl['new'] = 13
>>> tabl
 Name   |   Height |   Married |   new
--------+----------+-----------+-------
 John   |     1.82 |         0 |    13
 Joe    |     1.65 |         0 |    13
 Jane   |     2.15 |         1 |    13
3 rows ['<U4', '<f8', '|b1', '<i8']

Just like numpy, slices are not actual copies of the data, rather they are
references.

append Tabl and row
---------------------

Tabls can be appended with other Tabls:

>>> tabl = Tabl({'Name' : ["John", "Joe", "Jane"], 'Height' : [1.82,1.65,2.15], 'Married': [False,False,True]})
>>> tabl += tabl
>>> tabl
 Name   |   Height |   Married
--------+----------+-----------
 John   |     1.82 |         0
 Joe    |     1.65 |         0
 Jane   |     2.15 |         1
 John   |     1.82 |         0
 Joe    |     1.65 |         0
 Jane   |     2.15 |         1
6 rows ['<U4', '<f8', '|b1']

Or append rows as dictionary:

>>> tabl = Tabl({'Name' : ["John", "Joe", "Jane"], 'Height' : [1.82,1.65,2.15], 'Married': [False,False,True]})
>>> tabl.row_append({'Height':1.81, 'Name':"Jack", 'Married':True})
>>> tabl
 Name   |   Height |   Married
--------+----------+-----------
 John   |     1.82 |         0
 Joe    |     1.65 |         0
 Jane   |     2.15 |         1
 Jack   |     1.81 |         1
4 rows ['<U4', '<f8', '|b1']


instance properties
--------------------

Your data is simply stored as a list of numpy arrays and can be accessed or
manipulated like that (just don't make a mess):

>>> tabl = Tabl({'Name' : ["John", "Joe", "Jane"], 'Height' : [1.82,1.65,2.15], 'Married': [False,False,True]})
>>> tabl.columns
['Name', 'Height', 'Married']
>>> tabl.data        # doctest: +SKIP
[array(['John', 'Joe', 'Jane'],
      dtype='<U4'), array([ 1.82,  1.65,  2.15]), array([False, False,  True], dtype=bool)]

Further the basic means to asses the size of your data:

>>> tabl.shape
(3, 3)
>>> len(tabl)
3

pandas
-------

For for interfacing with the popular datatable framework, going back and forth
is easy:

>>> import pandas as pd
>>> df = pd.DataFrame({'a':range(3),'b':range(10,13)})
>>> df
   a   b
0  0  10
1  1  11
2  2  12

To make a Tabl from a DataFrame, just supply it to the initialize:

>>> tabl = Tabl(df)
>>> tabl
   a |   b
-----+-----
   0 |  10
   1 |  11
   2 |  12
3 rows ['<i8', '<i8']

The dict property of Tabl provides a way to make a DataFrame from a Tabl:

>>> df = pd.DataFrame(tabl.dict)
>>> df
   a   b
0  0  10
1  1  11
2  2  12


Resources & getting help
==========================

* See for the full API and more examples the documentation on `RTD <https://tabl.readthedocs.io/en/stable/index.html>`_.
* The repository on `Github <https://github.com/BastiaanBergman/tabl>`_.
* Installables on `pip <https://pypi.org/project/tabl/>`_.
* Questions and answers on `StackOverflow <https://stackoverflow.com/>`_, I
  will try to monitor for it.

Stable releases
================
* tabl 1.2.3

  * Added __delitem__ feature to delete row(s) or a column.

* tabl 1.2.2

  * Added argument to save and read methods for csv and gz formats to specify
    whether or not to write/read a header with the column names. For reading
    header can be left to None for automatic sniffing of the header. Default is
    True for both read and save methods.

* tabl 1.2.1

  * Removed unicode characters from description to fix pip install
    `issue <https://github.com/BastiaanBergman/tabl/issues/6#issue-440282452>`.

* tabl 1.2.0

  * Fix for numpy 1.15.5 "warnings"
  * Fix for outerjoin to raise an error in case of unsupported datatypes

* tabl 1.1

  * Added join and group_by methods
  * September 27, 2018

* tabl 1.0

  * First release
  * September 8, 2018


Dependencies
============

* numpy
* tabulate (optional, recommended)
* pandas (optional, for converting back and forth to DataFrames)

Tested on:
----------

* Python 3.6.4;  numpy 1.15.4
* Python 3.6.4;  numpy 1.14.3
* Python 2.7.14; numpy 1.14.0


Contributing to Tabl
=====================
Tabl is perfect already, no more contributions needed. Just kidding!

See the repository for filing issues and proposing enhancements.

git:
----

* Using master as the development branch
* Every new version is branched of of master (after its finished) into its own
  "v1.2.3" named branch. Subsequent version specific fixes can be done in the
  version branches.


I'm using pytest, pylint, doctest, sphynx and setuptools.

 - git ::

    git checkout master
    git pull

 - pytest ::

    cd tabl/test
    conda activate py3_6
    pytest
    conda activate py2_7
    pytest

 - pylint ::

    cd tabl/
    ./pylint.sh

 - doctest ::

    cd tabl/docs
    make doctest

 - sphynx ::

    cd tabl/docs
    make html

 - setuptools/pypi ::

    python setup.py sdist bdist_wheel
    twine upload dist/tabl-1.1.0.*

 - git ::

    git add .
    git commit -m
    git push
    git checkout v1.2.3 -b
    git push --set-upstream origin v1.2.3



Contributors
============
Just me, Bastiaan Bergman [Bastiaan.Bergman@gmail.com].


What's in the name?
===================

*Tabl* is Dutch for table (two-dimensional enlisting), `wiktionary
<https://nl.wiktionary.org/wiki/tabl>`_. The english word table, as in "dinner
table", translates in Dutch to *tafel*. The Dutch word *tafel* is an old
fashioned word for data-table, mostly used for calculation tables which itself
is old fashioned as well.


ToDo
=====

* polish error messages and validity checking and add testing for it.
* cache buffers for faster appending: store temp in list and concatenate to
  array only once we use another method
* allow for (sparse) numpy arrays as an element
* adjust & limit __repr__ width for very wide Tabls in jupyter cell
* items() and row_items() and keys() and values() method
* pop_column method
* tox - environment testing
* set subsets of tabls with (subsets) of other tabls, seems logic as __setitem__ is
  allowed to provide the datatype that should have come from a __getitem__
* datetime column support
* add disk datalogger
