# Smoothing Methods

Smoothing Methods

Many technical indicators are based on various methods of the price series smoothing. Some standard technical indicators require specification of the smoothing type as an input parameter. For specifying the desired type of smoothing, identifiers listed in the ENUM\_MA\_METHOD enumeration are used.

ENUM\_MA\_METHOD

| ID | Description |
| --- | --- |
| MODE\_SMA | Simple averaging |
| MODE\_EMA | Exponential averaging |
| MODE\_SMMA | Smoothed averaging |
| MODE\_LWMA | Linear-weighted averaging |

Example:

|  |
| --- |
| double ExtJaws[];  double ExtTeeth[];  double ExtLips[];  //---- handles for moving averages  int    ExtJawsHandle;  int    ExtTeethHandle;  int    ExtLipsHandle;  //--- get MA's handles  ExtJawsHandle=iMA(NULL,0,JawsPeriod,0,MODE\_SMMA,PRICE\_MEDIAN);  ExtTeethHandle=iMA(NULL,0,TeethPeriod,0,MODE\_SMMA,PRICE\_MEDIAN);  ExtLipsHandle=iMA(NULL,0,LipsPeriod,0,MODE\_SMMA,PRICE\_MEDIAN); |
