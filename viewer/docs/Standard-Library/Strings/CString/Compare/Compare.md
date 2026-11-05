# Compare

# Compare

Compares to a string.

```cpp
int  Compare(
   const string  str      // string
   ) const;
```

Parameters

str

[in]  String to compare.

Return Value

0 - both strings are equal, -1 - the class string is lower than the string to compare, 1 - the class string is greater than the string to compare.

Compare

Compares to a CString class instance string.

```cpp
int  Compare(
   CString*  str      // pointer
   ) const;
```

Parameters

str

[in]  Pointer to CString class instance to compare.

Return Value

0 - strings are equal, -1 - the class string is lower than the string to compare, 1 - the class string is greater than the string to compare.