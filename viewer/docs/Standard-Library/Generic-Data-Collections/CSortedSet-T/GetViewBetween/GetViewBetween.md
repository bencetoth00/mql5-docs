# GetViewBetween


Gets from the current sorted set a subset specified by the minimum and maximum values.

```cpp
bool GetViewBetween(
   T&  array[],         // an array for writing
   T   lower_value,     // the minimum value
   T   upper_value      // the maximum value
   );
```

Parameters

&array[]

[out] An array for writing the subset.

lower\_value

[in] The minimum value of the range.

upper\_value

[in] The maximum value of the range.

Return Value

Returns true on successful, or false otherwise.