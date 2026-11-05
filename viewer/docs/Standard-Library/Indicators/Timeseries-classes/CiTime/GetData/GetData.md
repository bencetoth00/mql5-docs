# GetData

# GetData

Gets the specified element of a timeseries buffer.

```cpp
datetime  GetData(
   int  index      // index
   ) const
```

Parameters

index

[in]  Index of the buffer element.

Return Value

The timeseries buffer element, or 0.

# GetData

Gets the data from a timeseries buffer by starting position and number.

```cpp
int  GetData(
   int   start_pos,     // position
   int   count,         // number
   long& buffer         // array
   ) const
```

Parameters

start\_pos

[in]  Starting position of timeseries.

count

[in]  Number of timeseries buffer elements.

buffer

[in]  Reference to the array for storing data.

Return Value

>=0 - successful, -1 - cannot receive data.

# GetData

Gets the data from timeseries buffer by starting time and number.

```cpp
int  GetData(
   datetime  start_time,     // starting time
   int       count,          // number
   long&     buffer          // array
   ) const
```

Parameters

start\_time

[in]  Time of a timeseries buffer initial element.

count

[in]  Number of timeseries buffer elements.

buffer

[in]  Reference to the array for storing data.

Return Value

>=0 - successful, -1 - cannot receive data.

GetData

Gets the data from a timeseries buffer by starting and stop times.

```cpp
int  GetData(
   datetime  start_time,     // starting time
   datetime  stop_time,      // stop time
   long&     buffer          // array
   ) const
```

Parameters

start\_time

[in]  Time of a timeseries buffer initial element.

stop\_time

[in]  Time of a timeseries buffer end element.

buffer

[in]  Reference to the array for storing data

Return Value

>=0 - successful, -1 - cannot receive data.