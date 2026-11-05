# GetData

GetData

Gets the specified element of the specified buffer of the indicator. [Refresh()](../Refresh/Refresh.md) should be called for working with recent data before using the method.

|  |
| --- |
| double  GetData(     const int  buffer\_num,     // buffer number     const int  index           // index     ) const |

Parameters

buffer\_num

[in]  Indicator buffer number.

index

[in]  Indicator buffer element index.

Return Value

value - success, [EMPTY\_VALUE](../../../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) - cannot receive the data.

GetData

Gets the data from the indicator's buffer by starting position and number.

|  |
| --- |
| int  GetData(     const int      start\_pos,      // position     const int      count,          // number     const int      buffer\_num,     // buffer number     double&        buffer[]        // array     ) const |

Parameters

start\_pos

[in]  Starting position of the indicator buffer.

count

[in]  Number of indicator buffer elements.

buffer\_num

[in]  Number of the indicator buffer.

buffer

[in]  Reference to the array for storing data.

Return Value

Number of the indicator values received ​​from the specified indicator buffer - success, otherwise -1.

GetData

Gets the data from the indicator buffer by start time and number.

|  |
| --- |
| int  GetData(     const datetime  start\_time,     // starting time     const int       count,          // amount     const int       buffer\_num,     // buffer number     double&         buffer[]        // array     ) const |

Parameters

start\_time

[in]  Indicator buffer element starting time.

count

[in]  Number of indicator buffer elements.

buffer\_num

[in]  Number of the indicator buffer.

buffer

[in]  Reference to the array for storing data.

Return Value

Number of the indicator values received ​​from the specified buffer, otherwise -1.

GetData

Gets the data from the indicator buffer by start and end time.

|  |
| --- |
| int  GetData(     const datetime  start\_time,     // start time     const datetime  stop\_time,      // end time     const int       buffer\_num,     // number of buffer     double&         buffer[]        // array     ) const |

Parameters

start\_time

[in]  Indicator buffer initial element time.

stop\_time

[in]  Indicator buffer end element time.

buffer\_num

[in]  Number of the indicator buffer.

buffer

[in]  Reference to the array for storing data.

Return Value

Number of the indicator values received ​​from the specified buffer - success, otherwise -1.
