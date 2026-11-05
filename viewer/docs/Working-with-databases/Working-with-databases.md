# Working with databases


The functions for working with databases apply the popular and easy-to-use [SQLite](https://www.sqlite.org/index.html) engine. The convenient feature of this engine is that the entire database is located in a single file on a user PC's hard disk.

The functions allow for convenient creation of tables, adding data to them, performing modifications and sampling using simple SQL requests:

- receiving trading history and quotes from any formats,
- saving optimization and test results,
- preparing and exchanging data with other analysis packages,
- storing MQL5 application settings and status.

Queries allow using [statistical](Working-with-databases.md#math) and [mathematical](Working-with-databases.md#stats) functions.

The functions for working with databases allow you to replace the most repetitive large data array handling operations with SQL requests, so that it is often possible to use the [DatabaseExecute](DatabaseExecute/DatabaseExecute.md)/[DatabasePrepare](DatabasePrepare/DatabasePrepare.md) calls instead of programming complex loops and comparisons. Use the [DatabaseReadBind](DatabaseReadBind/DatabaseReadBind.md) function to conveniently obtain query results in a ready-made structure. The function allows reading all record fields at once within a single call.

To accelerate reading, writing and modification, a database can be opened/created in RAM with the DATABASE\_OPEN\_MEMORY flag, although such a database is available only to a specific application and is not shared. When working with databases located on the hard disk, bulk data inserts/changes should be wrapped in transactions using [DatabaseTransactionBegin](DatabaseTransactionBegin/DatabaseTransactionBegin.md)/DatabaseTransactionCommit/DatabaseTransactionRollback. This accelerates the process hundreds of times.

To start working with the functions, read the article [SQLite: Native handling of SQL databases in MQL5](https://www.mql5.com/en/articles/7463).

| Function | Action |
| --- | --- |
| [DatabaseOpen](DatabaseOpen/DatabaseOpen.md) | Opens or creates a database in a specified file |
| [DatabaseClose](DatabaseClose/DatabaseClose.md) | Closes a database |
| [DatabaseImport](DatabaseImport/DatabaseImport.md) | Imports data from a file into a table |
| [DatabaseExport](DatabaseExport/DatabaseExport.md) | Exports a table or an SQL request execution result to a CSV file |
| [DatabasePrint](DatabasePrint/DatabasePrint.md) | Prints a table or an SQL request execution result in the Experts journal |
| [DatabaseTableExists](DatabaseTableExists/DatabaseTableExists.md) | Checks the presence of the table in a database |
| [DatabaseExecute](DatabaseExecute/DatabaseExecute.md) | Executes a request to a specified database |
| [DatabasePrepare](DatabasePrepare/DatabasePrepare.md) | Creates a handle of a request, which can then be executed using DatabaseRead() |
| [DatabaseReset](DatabaseReset/DatabaseReset.md) | Resets a request, like after calling [DatabasePrepare()](DatabasePrepare/DatabasePrepare.md) |
| [DatabaseBind](DatabaseBind/DatabaseBind.md) | Sets a parameter value in a request |
| [DatabaseBindArray](DatabaseBindArray/DatabaseBindArray.md) | Sets an array as a parameter value |
| [DatabaseRead](DatabaseRead/DatabaseRead.md) | Moves to the next entry as a result of a request |
| [DatabaseReadBind](DatabaseReadBind/DatabaseReadBind.md) | Moves to the next record and reads data into the structure from it |
| [DatabaseFinalize](DatabaseFinalize/DatabaseFinalize.md) | Removes a request created in DatabasePrepare() |
| [DatabaseTransactionBegin](DatabaseTransactionBegin/DatabaseTransactionBegin.md) | Starts transaction execution |
| [DatabaseTransactionCommit](DatabaseTransactionCommit/DatabaseTransactionCommit.md) | Completes transaction execution |
| [DatabaseTransactionRollback](DatabaseTransactionRollback/DatabaseTransactionRollback.md) | Rolls back transactions |
| [DatabaseColumnsCount](DatabaseColumnsCount/DatabaseColumnsCount.md) | Gets the number of fields in a request |
| [DatabaseColumnName](DatabaseColumnName/DatabaseColumnName.md) | Gets a field name by index |
| [DatabaseColumnType](DatabaseColumnType/DatabaseColumnType.md) | Gets a field type by index |
| [DatabaseColumnSize](DatabaseColumnSize/DatabaseColumnSize.md) | Gets a field size in bytes |
| [DatabaseColumnText](DatabaseColumnText/DatabaseColumnText.md) | Gets a field value as a string from the current record |
| [DatabaseColumnInteger](DatabaseColumnInteger/DatabaseColumnInteger.md) | Gets the int type value from the current record |
| [DatabaseColumnLong](DatabaseColumnLong/DatabaseColumnLong.md) | Gets the long type value from the current record |
| [DatabaseColumnDouble](DatabaseColumnDouble/DatabaseColumnDouble.md) | Gets the double type value from the current record |
| [DatabaseColumnBlob](DatabaseColumnBlob/DatabaseColumnBlob.md) | Gets a field value as an array from the current record |

Statistical functions:

- mode – [mode](https://en.wikipedia.org/wiki/Mode_(statistics))
- median – [median](https://en.wikipedia.org/wiki/Median) (50th percentile)
- percentile\_25 – 25th [percentile](https://en.wikipedia.org/wiki/Quantile)
- percentile\_75
- percentile\_90
- percentile\_95
- percentile\_99
- stddev or stddev\_samp — sample standard deviation
- stddev\_pop — population standard deviation
- variance or var\_samp — sample variance
- var\_pop — population variance

Mathematical functions

- [acos(X)](https://sqlite.org/lang_mathfunc.html#acos) – arccosine in radians
- [acosh(X)](https://sqlite.org/lang_mathfunc.html#acosh) – hyperbolic arccosine
- [asin(X)](https://sqlite.org/lang_mathfunc.html#asin) – arcsine in radians
- [asinh(X)](https://sqlite.org/lang_mathfunc.html#asinh) – hyperbolic arcsine
- [atan(X)](https://sqlite.org/lang_mathfunc.html#atan) – arctangent in radians
- [atan2(X,Y)](https://sqlite.org/lang_mathfunc.html#atan2) – arctangent in radians of the X/Y ratio
- [atanh(X)](https://sqlite.org/lang_mathfunc.html#atanh) – hyperbolic arctangent
- [ceil(X)](https://sqlite.org/lang_mathfunc.html#ceil) – rounding up to an integer
- [ceiling(X)](https://sqlite.org/lang_mathfunc.html#ceil) – rounding up to an integer
- [cos(X)](https://sqlite.org/lang_mathfunc.html#cos) – angle cosine in radians
- [cosh(X)](https://sqlite.org/lang_mathfunc.html#cosh) – hyperbolic cosine
- [degrees(X)](https://sqlite.org/lang_mathfunc.html#degrees) – convert radians into the angle
- [exp(X)](https://sqlite.org/lang_mathfunc.html#exp) – exponent
- [floor(X)](https://sqlite.org/lang_mathfunc.html#floor) – rounding down to an integer
- [ln(X)](https://sqlite.org/lang_mathfunc.html#ln) – natural logarithm
- [log(B,X)](https://sqlite.org/lang_mathfunc.html#log) – logarithm to the indicated base
- [log(X)](https://sqlite.org/lang_mathfunc.html#log) – decimal logarithm
- [log10(X)](https://sqlite.org/lang_mathfunc.html#log) – decimal logarithm
- [log2(X)](https://sqlite.org/lang_mathfunc.html#log2) – logarithm to base 2
- [mod(X,Y)](https://sqlite.org/lang_mathfunc.html#mod) – remainder of division
- [pi()](https://sqlite.org/lang_mathfunc.html#pi) – approximate Pi
- [pow(X,Y)](https://sqlite.org/lang_mathfunc.html#pow) – power by the indicated base
- [power(X,Y)](https://sqlite.org/lang_mathfunc.html#pow) – power by the indicated base
- [radians(X)](https://sqlite.org/lang_mathfunc.html#radians) – convert the angle into radians
- [sin(X)](https://sqlite.org/lang_mathfunc.html#sin) – angle sine in radians
- [sinh(X)](https://sqlite.org/lang_mathfunc.html#sinh) – hyperbolic sine
- [sqrt(X)](https://sqlite.org/lang_mathfunc.html#sqrt) – square root
- [tan(X)](https://sqlite.org/lang_mathfunc.html#tan) – angle tangent in radians
- [tanh(X)](https://sqlite.org/lang_mathfunc.html#tanh) – hyperbolic tangent
- [trunc(X)](https://sqlite.org/lang_mathfunc.html#trunc) – truncate to an integer closest to 0

Example:

```cpp
select
  count(*) as book_count,
  cast(avg(parent) as integer) as mean,
  cast(median(parent) as integer) as median,
  mode(parent) as mode,
  percentile_90(parent) as p90,
  percentile_95(parent) as p95,
  percentile_99(parent) as p99
from moz_bookmarks;
```