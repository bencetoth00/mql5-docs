# GetData

GetData

Gets the element of timeseries by starting position and number of elements.

|  |
| --- |
| int  GetData(     int   start\_pos,     // position     int   count,         // number     double& buffer       // array     ) const |

Parameters

start\_pos

[in]  Starting position of a timeseries buffer.

count

[in]  Number of timeseries buffer elements.

buffer

[in]  Reference to the data storage array.

Return Value

>=0 - successful, -1 - cannot receive data.

GetData

Gets the data from a timeseries buffer by starting time and number.

|  |
| --- |
| int  GetData(     datetime  start\_time,     // starting time     int       count,          // number     double&     buffer        // array     ) const |

Parameters

start\_time

[in]  Time of a timeseries buffer initial element.

count

[in]  Number of timeseries buffer elements.

buffer

[in]  Reference to the data storage array.

Return Value

>=0 - successful, -1 - cannot receive data.

GetData

Gets data from the timeseries buffer by starting and stop times.

|  |
| --- |
| int  GetData(     datetime  start\_time,     // starting time     datetime  stop\_time,      // stop time     double&   buffer          // array     ) const |

Parameters

start\_time

[in]  Time of a timeseries buffer initial element.

stop\_time

[in]  Time of a timeseries buffer last element.

buffer

[in]  Reference to the data storage array

Return Value

>=0 - successful, -1 - cannot receive data.
