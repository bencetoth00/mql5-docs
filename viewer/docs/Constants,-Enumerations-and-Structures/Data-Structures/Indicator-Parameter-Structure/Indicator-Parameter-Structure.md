# Indicator Parameter Structure

# The Structure of Input Parameters of Indicators (MqlParam)

The MqlParam structure has been specially designed to provide [input parameters](../../../Language-Basics/Variables/Input-Variables/Input-Variables.md) when creating the handle of [a technical indicator](../../../Technical-Indicators/Technical-Indicators.md) using the [IndicatorCreate()](../../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md) function.

```cpp
struct MqlParam
  {
   ENUM_DATATYPE     type;                    // type of the input parameter, value of ENUM_DATATYPE
   long              integer_value;           // field to store an integer type
   double            double_value;            // field to store a double type
   string            string_value;            // field to store a string type
  };
```

All input parameters of an indicator are transmitted in the form of an array of the MqlParam type, the type field of each element of this array specifies the type of data transmitted by the element. The indicator values must be first placed in the appropriate fields for each element (in integer\_value, in double\_value or string\_value) depending on what value of [ENUM\_DATATYPE](../../Indicator-Constants/Data-Type-Identifiers/Data-Type-Identifiers.md) enumeration is specified in the type field.

If the IND\_CUSTOM value is passed third as the indicator type to the [IndicatorCreate()](../../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md) function, the first element of the array of input parameters must have the type field with the value of TYPE\_STRING from the [ENUM\_DATATYPE](../../Indicator-Constants/Data-Type-Identifiers/Data-Type-Identifiers.md) enumeration, and the string\_value field must contain the name of the [custom indicator](../../../Technical-Indicators/iCustom/iCustom.md).