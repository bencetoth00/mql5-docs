# Indicator Types

Types of Technical Indicators

There are two ways to create an indicator handle for further [accessing to its values](../../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md). The first way is to directly specify a function name from the list of [technical indicators](../../../Technical-Indicators/Technical-Indicators.md). The second method using the [IndicatorCreate()](../../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md) is to uniformly create a handle of any indicator by assigning an identifier from the ENUM\_INDICATOR enumeration. Both ways of handle creation are equal, you can use the one that is most convenient in a particular case when writing a program in MQL5.

When creating an indicator of type IND\_CUSTOM, the type field of the first element of an array of [input parameters MqlParam](../../Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) must have the TYPE\_STRING value of the enumeration [ENUM\_DATATYPE](../Data-Type-Identifiers/Data-Type-Identifiers.md), while the field string\_value of the first element must contain the name of the custom indicator.

ENUM\_INDICATOR

| Identifier | Indicator |
| --- | --- |
| IND\_AC | Accelerator Oscillator |
| IND\_AD | Accumulation/Distribution |
| IND\_ADX | Average Directional Index |
| IND\_ADXW | ADX by Welles Wilder |
| IND\_ALLIGATOR | Alligator |
| IND\_AMA | Adaptive Moving Average |
| IND\_AO | Awesome Oscillator |
| IND\_ATR | Average True Range |
| IND\_BANDS | Bollinger Bands® |
| IND\_BEARS | Bears Power |
| IND\_BULLS | Bulls Power |
| IND\_BWMFI | Market Facilitation Index |
| IND\_CCI | Commodity Channel Index |
| IND\_CHAIKIN | Chaikin Oscillator |
| IND\_CUSTOM | Custom indicator |
| IND\_DEMA | Double Exponential Moving Average |
| IND\_DEMARKER | DeMarker |
| IND\_ENVELOPES | Envelopes |
| IND\_FORCE | Force Index |
| IND\_FRACTALS | Fractals |
| IND\_FRAMA | Fractal Adaptive Moving Average |
| IND\_GATOR | Gator Oscillator |
| IND\_ICHIMOKU | Ichimoku Kinko Hyo |
| IND\_MA | Moving Average |
| IND\_MACD | MACD |
| IND\_MFI | Money Flow Index |
| IND\_MOMENTUM | Momentum |
| IND\_OBV | On Balance Volume |
| IND\_OSMA | OsMA |
| IND\_RSI | Relative Strength Index |
| IND\_RVI | Relative Vigor Index |
| IND\_SAR | Parabolic SAR |
| IND\_STDDEV | Standard Deviation |
| IND\_STOCHASTIC | Stochastic Oscillator |
| IND\_TEMA | Triple Exponential Moving Average |
| IND\_TRIX | Triple Exponential Moving Averages Oscillator |
| IND\_VIDYA | Variable Index Dynamic Average |
| IND\_VOLUMES | Volumes |
| IND\_WPR | Williams' Percent Range |
