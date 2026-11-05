# Moving from MQL4

# Moving from MQL4 to MQL5

MQL5 is the evolution of its predecessor - the MQL4 programming language, in which numerous indicators, scripts, and Expert Advisors were written. Despite the fact that the new programming language is maximally compatible with the previous-generation language, there are still some differences between these languages. And when transferring programs these differences should be noted.

This section contains information intended to facilitate the adaptation of codes to the new MQL5 language for programmers who know MQL4.

First it should be noted:

- The new language does not contain functions start(), init() and deinit().
- No limit for the number of indicator buffers.
- DLLs are loaded immediately after loading an Expert Advisor (or any other mql5 program).
- Check of logical conditions is shortened.
- When limits of an array are exceeded, the current performance is terminated (critically - with the output of an errors).
- Precedence of operators like in C + +.
- The language offers the implicit type cast (even from string to a number).
- Local variables are not initialized automatically (except for strings).
- Common local arrays are automatically deleted.

## Special Functions init, start and deinit

The MQL4 language contained only three predefined functions that could be used in the indicator, script or Expert Advisor (not taking into account the include files \*.mqh and library files). In MQL5 there are no such functions, but there are their analogues. The table shows the approximate correspondence of functions.

| MQL4 | MQL5 |
| --- | --- |
| init | OnInit |
| start | OnStart |
| deinit | OnDeinit |

Functions [OnInit](../Event-Handling/OnInit/OnInit.md) and [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) perform the same role as init and deinit in MQL4 - they are designed to locate the code, which must be performed during initialization and deinitialization of mql5 programs. You can either just rename these functions accordingly, or leave them as they are, but add calls of these functions in corresponding places.

Example:

```cpp
void OnInit()
  {
//--- Call function upon initialization
   init();
  }
void OnDeinit(const int reason)
  {
//--- Call function upon deinitialization
   deinit();
//---
  }
```

The start function is replaced by [OnStart](../Event-Handling/OnStart/OnStart.md) only in scripts. In Expert Advisors and indicators it should be renamed to [OnTick](../Event-Handling/OnTick/OnTick.md) and [OnCalculate](../Event-Handling/OnCalculate/OnCalculate.md), respectively. The code that is to be executed during a mql5 program operation should be located in these three functions:

| mql5-program | main function |
| --- | --- |
| [script](../index.md#script) | OnStart |
| [indicator](../index.md#indicator) | OnCalculate |
| [Expert Advisor](../index.md#expert) | OnTick |

If the indicator or script code does not contain the main function, or the function name differs from the required one, the call of this function is not performed. It means, if the source code of a script doesn't contain OnStart, such a code will be compiled as an Expert Advisor.

If an indicator code doesn't contain the OnCalculate function, the compilation of such an indicator is impossible.

## Predefined Variables

In MQL5 there are no such predefined variables as Ask, Bid, Bars. Variables Point and Digits have a slightly different spelling:

| MQL4 | MQL5 |
| --- | --- |
| Digits | \_Digits |
| Point | \_Point |
|  | \_LastError |
|  | \_Period |
|  | \_Symbol |
|  | \_StopFlag |
|  | \_UninitReason |

## Access to Timeseries

In MQL5 there are no such predefined timeseries as Open[], High[], Low[], Close[], Volume[] and Time[]. The necessary depth of a timeseries can now be set using corresponding [functions to access timeseries](../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md).

## Expert Advisors

Expert Advisors in MQL5 do not require the obligatory presence of functions that handle the [events](../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md) of a new tick receipt - OnTick, as it was in MQL4 (the start function in MQL4 is executed when a new tick is received). In MQL5 Expert Advisors can contain pre-defined handler functions of several types of events:

- [OnTick](../Event-Handling/OnTick/OnTick.md) – receipt of a new tick;
- [OnTimer](../Event-Handling/OnTimer/OnTimer.md) – timer event;

- [OnTrade](../Event-Handling/OnTrade/OnTrade.md) - trade event;

- [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) – events of input from the keyboard and mouse, events of a graphic object moving, event of a text editing completion in the entry field of the LabelEdit object;
- [OnBookEvent](../Event-Handling/OnBookEvent/OnBookEvent.md) – event of Depth of Market status change.

## Custom Indicators

In MQL4, the number of indicator buffers is limited and can't exceed 8. In MQL5 there are no such limitations, but it should be remembered that each indicator buffer requires allocation of a certain part of memory for its location in the terminal, so the new possibility should not be abused.

MQL4 offered only 6 types of custom indicator plotting; while MQL5 now offers 18 [drawing styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_draw_type). The names of drawing types haven't changed, but the ideology of the graphical representation of indicators has changed significantly.

The direction of indexing in indicator buffers also differs. By default, in MQL5 all the indicator buffers have the behavior of common arrays, i.e. 0 indexed element is the oldest one in the history, and as the index increases, we move from the oldest data to the most recent ones.

The only function for working with [custom indicators](../Custom-Indicators/Custom-Indicators.md) that was preserved from MQL4 is [SetIndexBuffer](../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md). But its call has changed; now you should specify [type of data to be stored in an array](../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_indexbuffer_type_enum), linked to the indicator buffer.

Properties of custom indicators also have changed and expanded. New functions for [accessing timeseries](../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md) have been added, so the total calculation algorithm must be reconsidered.

## Graphical Objects

The number of graphical objects in MQL5 has been significantly increased. Besides, graphical objects can now be positioned in time with the accuracy of a second in a chart of any timeframe - now object anchor points are not rounded off to the bar opening time in the current price chart.

For the Arrow, Text and Label objects now you can specify [binding methods](../Constants,-Enumerations-and-Structures/Objects-Constants/Methods-of-Object-Binding/Methods-of-Object-Binding.md), and for the Label, Button, Chart, Bitmap Label and Edit objects you can set [chart corner to which an object is attached](../Constants,-Enumerations-and-Structures/Objects-Constants/Chart-Corner/Chart-Corner.md).