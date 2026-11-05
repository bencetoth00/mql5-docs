# Custom Indicators


This is the group functions used in the creation of custom indicators. These functions can't be used when writing Expert Advisors and Scripts.

| Function | Action |
| --- | --- |
| [SetIndexBuffer](SetIndexBuffer/SetIndexBuffer.md) | Binds the specified indicator buffer with one-dimensional dynamic [array](../Language-Basics/Variables/Variables.md#array_define) of the [double](../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type |
| [IndicatorSetDouble](IndicatorSetDouble/IndicatorSetDouble.md) | Sets the value of an indicator property of the [double](../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type |
| [IndicatorSetInteger](IndicatorSetInteger/IndicatorSetInteger.md) | Sets the value of an indicator property of the [int](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type |
| [IndicatorSetString](IndicatorSetString/IndicatorSetString.md) | Sets the value of an indicator property of the [string](../Language-Basics/Data-Types/String-Type/String-Type.md) type |
| [PlotIndexSetDouble](PlotIndexSetDouble/PlotIndexSetDouble.md) | Sets the value of an indicator line property of the type [double](../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) |
| [PlotIndexSetInteger](PlotIndexSetInteger/PlotIndexSetInteger.md) | Sets the value of an indicator line property of the [int](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type |
| [PlotIndexSetString](PlotIndexSetString/PlotIndexSetString.md) | Sets the value of an indicator line property of the [string](../Language-Basics/Data-Types/String-Type/String-Type.md) type |
| [PlotIndexGetInteger](PlotIndexGetInteger/PlotIndexGetInteger.md) | Returns the value of an indicator line property of the [integer](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type |

[Indicator properties](Connection-between-Indicator-Properties-and-Functions/Connection-between-Indicator-Properties-and-Functions.md) can be set using the compiler directives or using functions. To better understand this, it is recommended that you study [indicator styles in examples](Indicator-Styles-in-Examples/Indicator-Styles-in-Examples.md).

All the necessary calculations of a custom indicator must be placed in the predetermined function [OnCalculate()](../Event-Handling/OnCalculate/OnCalculate.md). If you use a short form of the OnCalculate() function call, like

```cpp
int OnCalculate (const int rates_total, const int prev_calculated, const int begin, const double& price[])
```

then the rates\_total variable contains the value of the total number of elements of the price[] array, passed as an input parameter for calculating indicator values.

Parameter prev\_calculated is the result of the execution of OnCalculate() at the previous call; it allows organizing a saving algorithm for calculating indicator values. For example, if the current value rates\_total = 1000, prev\_calculated = 999, then perhaps it's enough to make calculations only for one value of each indicator buffer.

If the information about the size of the input array price would have been unavailable, then it would lead to the necessity to make calculations for 1000 values of each indicator buffer. At the first call of OnCalculate() value prev\_calculated = 0. If the price[] array has changed somehow, then in this case prev\_calculated is also equal to 0.

The begin parameter shows the number of initial values of the price array, which don't contain data for calculation. For example, if values of Accelerator Oscillator (for which the first 37 values aren't calculated) were used as an input parameter, then begin = 37. For example, let's consider a simple indicator:

```cpp
#property indicator_chart_window
#property indicator_buffers 1
#property indicator_plots   1
//---- plot Label1
#property indicator_label1  "Label1"
#property indicator_type1   DRAW_LINE
#property indicator_color1  clrRed
#property indicator_style1  STYLE_SOLID
#property indicator_width1  1
//--- indicator buffers
double         Label1Buffer[];
//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
void OnInit()
  {
//--- indicator buffers mapping
   SetIndexBuffer(0,Label1Buffer,INDICATOR_DATA);
//---
  }
//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const int begin,
                const double &price[])
  {
//---
   Print("begin = ",begin,"  prev_calculated = ",prev_calculated,"  rates_total = ",rates_total);
//--- return value of prev_calculated for next call
   return(rates_total);
  }
```

Drag it from the "Navigator" window to the window of the Accelerator Oscillator indicator and we indicate that calculations will be made based on the values of the previous indicator:

![Calculating an indicator on values of the previously attached indicator](../assets/previousindicatorsdata.png "Calculating an indicator on values of the previously attached indicator")

As a result, the first call of OnCalculate() the value of prev\_calculated will be equal to zero, and in further calls it will be equal to the rates\_total value (until the number of bars on the price chart increases).

![The begin parameter shows the number of initial bars, on which values are omitted](../assets/beginparameteronprevindabsent.png "The begin parameter shows the number of initial bars, on which values are omitted")

The value of the begin parameter will be exactly equal to the number of initial bars, for which the values of the Accelerator indicator aren't calculated according to the logic of this indicator. If we look at the source code of the custom indicator Accelerator.mq5, we'll see the following lines in the [OnInit()](../Event-Handling/OnInit/OnInit.md) function:

```cpp
//--- sets first bar from which index will be drawn
   PlotIndexSetInteger(0,PLOT_DRAW_BEGIN,37);
```

Using the function [PlotIndexSetInteger](PlotIndexSetInteger/PlotIndexSetInteger.md)(0, [PLOT\_DRAW\_BEGIN](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_plot_property_integer), empty\_first\_values), we set the number of non-existing first values in the zero indicator array of a custom indicator, which we don't need to accept for calculation (empty\_first\_values). Thus, we have mechanisms to:

1. set the number of initial values of an indicator, which shouldn't be used for calculations in another custom indicator;
2. get information on the number of first values to be ignored when you call another custom indicator, without going into the logic of its calculations.