# FileFindNext

FileFindNext

Continues file search started by the FileFindFirst() method.

|  |
| --- |
| bool  FileFindNext(     int      search\_handle,     // search handle     string&  file\_name          // reference     ) |

Parameters

search\_handle

[in]  Search handle returned by FileFindFirst() method.

file\_name

[in]  The reference to the string the name of the found file is placed into if successful.

Return Value

true - successful, false - there are no files corresponding to the filter.
