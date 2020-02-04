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
> <path to the exe>\sqlite3.exe

sqlite> .open pythonsqlite.db

sqlite> .databases

sqlite> .tables

sqlite> SELECT * FROM classification_totals;
```
