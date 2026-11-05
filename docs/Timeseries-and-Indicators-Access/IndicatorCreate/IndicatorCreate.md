# IndicatorCreate

IndicatorCreate

The function returns the handle of a specified technical indicator created based on the array of parameters of [MqlParam](../../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) type.

|  |
| --- |
| int  IndicatorCreate(     string           symbol,                            // symbol name     ENUM\_TIMEFRAMES  period,                            // timeframe     ENUM\_INDICATOR   indicator\_type,                    // indicator type from the enumeration ENUM\_INDICATOR     int              parameters\_cnt=0,                  // number of parameters     const MqlParam&  parameters\_array[]=NULL,           // array of parameters     ); |

Parameters

symbol

[in] Name of a symbol, on data of which the indicator is calculated. [NULL](../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) means the current symbol.

period

[in]  The value of the timeframe can be one of values of the [ENUM\_TIMEFRAMES](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration, 0 means the current timeframe.

indicator\_type

[in]  Indicator type, can be one of values of the [ENUM\_INDICATOR](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicator-Types/Indicator-Types.md) enumeration.

parameters\_cnt

[in] The number of parameters passed in the parameters\_array[] array. The array elements have a special structure type [MqlParam](../../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md). By default, zero - parameters are not passed. If you specify a non-zero number of parameters, the parameter parameters\_array is obligatory. You can pass no more than 64 parameters.

parameters\_array[]=NULL

[in]  An array of MqlParam type, whose elements contain the type and value of each input parameter of a [technical indicator](../../Technical-Indicators/Technical-Indicators.md).

Return Value

Returns the handle of a specified technical indicator,  in case of failure returns [INVALID\_HANDLE](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

Note

If the indicator handle of IND\_CUSTOM type is created, the type field of the first element of the array of input parameters parameters\_array must have the TYPE\_STRING value of the [ENUM\_DATATYPE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Data-Type-Identifiers/Data-Type-Identifiers.md) enumeration, and the string\_value field of the first element must contain the name of the custom indicator. The custom indicator must be compiled (file with EX5 extension) and located in the directory MQL5/Indicators of the client terminal or in a subdirectory.

Indicators that require testing are defined automatically from the call of the iCustom() function, if the corresponding parameter is set through a [constant string](../../Language-Basics/Data-Types/String-Type/String-Type.md). For all other cases (use of the [IndicatorCreate()](IndicatorCreate.md) function or use of a non-constant string in the parameter that sets the indicator name) the property [#property tester\_indicator](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md) is required:

|  |
| --- |
| #property tester\_indicator "indicator\_name.ex5" |

If [the first form of the call](../../Event-Handling/OnCalculate/OnCalculate.md) is used in a custom indicator, you can additionally indicate as the last parameter on what data it will be calculated when passing input parameters. If the "Apply to" parameter is not specified explicitly, the default calculation is based on the [PRICE\_CLOSE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md#enum_applied_price_enum) values.

Example:

|  |
| --- |
| void OnStart()    {     MqlParam params[];     int      h\_MA,h\_MACD;  //--- create iMA("EURUSD",PERIOD\_M15,8,0,MODE\_EMA,PRICE\_CLOSE);     ArrayResize(params,4);  //--- set ma\_period     params[0].type         =TYPE\_INT;     params[0].integer\_value=8;  //--- set ma\_shift     params[1].type         =TYPE\_INT;     params[1].integer\_value=0;  //--- set ma\_method     params[2].type         =TYPE\_INT;     params[2].integer\_value=MODE\_EMA;  //--- set applied\_price     params[3].type         =TYPE\_INT;     params[3].integer\_value=PRICE\_CLOSE;  //--- create MA     h\_MA=IndicatorCreate("EURUSD",PERIOD\_M15,IND\_MA,4,params);  //--- create iMACD("EURUSD",PERIOD\_M15,12,26,9,h\_MA);     ArrayResize(params,4);  //--- set fast ma\_period     params[0].type         =TYPE\_INT;     params[0].integer\_value=12;  //--- set slow ma\_period     params[1].type         =TYPE\_INT;     params[1].integer\_value=26;  //--- set smooth period for difference     params[2].type         =TYPE\_INT;     params[2].integer\_value=9;  //--- set indicator handle as applied\_price     params[3].type         =TYPE\_INT;     params[3].integer\_value=h\_MA;  //--- create MACD based on moving average     h\_MACD=IndicatorCreate("EURUSD",PERIOD\_M15,IND\_MACD,4,params);  //--- use indicators  //--- . . .  //--- release indicators (first h\_MACD)     IndicatorRelease(h\_MACD);     IndicatorRelease(h\_MA);    } |
