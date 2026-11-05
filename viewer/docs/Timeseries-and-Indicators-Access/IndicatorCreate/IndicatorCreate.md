# IndicatorCreate


The function returns the handle of a specified technical indicator created based on the array of parameters of [MqlParam](../../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) type.

```cpp
int  IndicatorCreate(
   string           symbol,                            // symbol name
   ENUM_TIMEFRAMES  period,                            // timeframe
   ENUM_INDICATOR   indicator_type,                    // indicator type from the enumeration ENUM_INDICATOR
   int              parameters_cnt=0,                  // number of parameters
   const MqlParam&  parameters_array[]=NULL,           // array of parameters
   );
```

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

```cpp
#property tester_indicator "indicator_name.ex5"
```

If [the first form of the call](../../Event-Handling/OnCalculate/OnCalculate.md) is used in a custom indicator, you can additionally indicate as the last parameter on what data it will be calculated when passing input parameters. If the "Apply to" parameter is not specified explicitly, the default calculation is based on the [PRICE\_CLOSE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md#enum_applied_price_enum) values.

Example:

```cpp
void OnStart()
  {
   MqlParam params[];
   int      h_MA,h_MACD;
//--- create iMA("EURUSD",PERIOD_M15,8,0,MODE_EMA,PRICE_CLOSE);
   ArrayResize(params,4);
//--- set ma_period
   params[0].type         =TYPE_INT;
   params[0].integer_value=8;
//--- set ma_shift
   params[1].type         =TYPE_INT;
   params[1].integer_value=0;
//--- set ma_method
   params[2].type         =TYPE_INT;
   params[2].integer_value=MODE_EMA;
//--- set applied_price
   params[3].type         =TYPE_INT;
   params[3].integer_value=PRICE_CLOSE;
//--- create MA
   h_MA=IndicatorCreate("EURUSD",PERIOD_M15,IND_MA,4,params);
//--- create iMACD("EURUSD",PERIOD_M15,12,26,9,h_MA);
   ArrayResize(params,4);
//--- set fast ma_period
   params[0].type         =TYPE_INT;
   params[0].integer_value=12;
//--- set slow ma_period
   params[1].type         =TYPE_INT;
   params[1].integer_value=26;
//--- set smooth period for difference
   params[2].type         =TYPE_INT;
   params[2].integer_value=9;
//--- set indicator handle as applied_price
   params[3].type         =TYPE_INT;
   params[3].integer_value=h_MA;
//--- create MACD based on moving average
   h_MACD=IndicatorCreate("EURUSD",PERIOD_M15,IND_MACD,4,params);
//--- use indicators
//--- . . .
//--- release indicators (first h_MACD)
   IndicatorRelease(h_MACD);
   IndicatorRelease(h_MA);
  }
```