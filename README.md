# QuickFrameAssignment

A QuickFrame assignment to create data pipleline with data cleanup and normalization 

## Requirements

Python3

sqllite3 (https://www.sqlite.org/2020/sqlite-tools-win32-x86-3310100.zip)

### QuickFrameAssignment can be installed directly from the source code:

```
$ git clone https://github.com/preetiiranii/QuickFrameAssignment.git

$ cd QuickFrameAssignment
```

## Basic Usage

```
$ python runner.py
```

## Run test cases:
```
$ python UnitTest.py
```
## View database/tables:

unzip the downloaded sqlite3 and follow these commands
```
> cd QuickFrameAssignment

> <path to the exe>\sqlite3.exe

sqlite> .open pythonsqlite.db

sqlite> .databases

sqlite> .tables

sqlite> SELECT * FROM classification_totals;
```
## Problem 1: 

Pipeline.data_cleanup() #cleans the first column of every row for format "1979.486.5” and discards all other rows

Unit test case: test_data_cleanup()

## Problem 2:

Pipeline.normalize_row() #creates two separate column for date range. (1843, 1843-56, 1843-1943, ca. 1843)

There are other date formats as well in the column such as:
  19th century (?), 
  19th century, 
  after 1886
  
As these were not mentioned in the problem statement, I have skipped calculations for them and have copied these dates to both the extra columns as it is.

Unit test case: test_normalize_row

## Problem 3:

Pipeline.running_total() Calculates total count for different items

Unit test case: test_classification_total()

