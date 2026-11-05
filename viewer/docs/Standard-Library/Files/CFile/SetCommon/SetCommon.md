# SetCommon


Sets/clears the FILE\_COMMON flag.

```cpp
void  SetCommon(
   bool  common      // flag value
   )
```

Parameters

common

[in]  New value for FILE\_COMMON flag.

Note

The FILE\_COMMON flag determines the current working folder. If it is false, the  local terminal folder is used as the current working folder. If it is true, the common data folder is used as the current working folder. If the file is already opened, the flag cannot be changed.