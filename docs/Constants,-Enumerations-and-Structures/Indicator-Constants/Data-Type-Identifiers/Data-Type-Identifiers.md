# Data Type Identifiers

Data Type Identifiers

When creating an indicator handle using the [IndicatorCreate()](../../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md) function, an array of [MqlParam](../../Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) type must be specified as the last parameter. Accordingly, the MqlParam structure, describing indicator, contains a special field type. This field contains information about the data type ([real](../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [integer](../../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) or [string](../../../Language-Basics/Data-Types/String-Type/String-Type.md) type) that are passed by a particular element of the array. The value of this field of the MqlParam structure may be one of ENUM\_DATATYPE values.

ENUM\_DATATYPE

| Identifier | Data type |
| --- | --- |
| TYPE\_BOOL | bool |
| TYPE\_CHAR | char |
| TYPE\_UCHAR | uchar |
| TYPE\_SHORT | short |
| TYPE\_USHORT | ushort |
| TYPE\_COLOR | color |
| TYPE\_INT | int |
| TYPE\_UINT | uint |
| TYPE\_DATETIME | datetime |
| TYPE\_LONG | long |
| TYPE\_ULONG | ulong |
| TYPE\_FLOAT | float |
| TYPE\_DOUBLE | double |
| TYPE\_STRING | string |

Each element of the array describes the corresponding input parameter of a created [technical indicator](../../../Technical-Indicators/Technical-Indicators.md), so the type and order of elements in the array must be strictly maintained in accordance with the description.
