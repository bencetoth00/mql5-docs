# CAxis


CAxis is an auxiliary graphics library class for working with the coordinate axes.

### Description

The CAxis class receives and stores various parameters of the coordinate axes. The class implements the ability to auto scale the coordinate axes dynamically.

### Declaration

```cpp
   class CAxis
```

### Title

```cpp
   #include <Graphics\Axis.mqh>
```

### Class methods

| Method | Description |
| --- | --- |
| [AutoScale](AutoScale/AutoScale.md) | Get/set the auto-scaling flag |
| [Min](Min/Min.md) | Get/set the minimum axis value |
| [Max](Max/Max.md) | Get/set the maximum axis value |
| [Step](Step/Step.md) | Get the step value by axis |
| [Name](Name/Name.md) | Get/set the axis name |
| [Color](Color/Color.md) | Get/set the axis color |
| [ValuesSize](ValuesSize/ValuesSize.md) | Get/set the size of the axis numbers |
| [ValuesWidth](ValuesWidth/ValuesWidth.md) | Get/set the maximum displayed length of the axis numbers |
| [ValuesFormat](ValuesFormat/ValuesFormat.md) | Get/set the format of the axis numbers |
| [ValuesDateTimeMode](ValuesDateTimeMode/ValuesDateTimeMode.md) | Get the format of converting a date into a string. |
| [ValuesFunctionFormat](ValuesFunctionFormat/ValuesFunctionFormat.md) | Get the pointer to the function defining the format of displaying values on the axis. |
| [ValuesFunctionFormatCBData](ValuesFunctionFormatCBData/ValuesFunctionFormatCBData.md) | Get the pointer to the object that may contain additional data on converting axis values. |
| [NameSize](NameSize/NameSize.md) | Get/set the font size of the axis name |
| [ZeroLever](ZeroLever/ZeroLever.md) | Get/set the "zero lever" value |
| [DefaultStep](DefaultStep/DefaultStep.md) | Get/set the initial step value by axis |
| [MaxLabels](MaxLabels/MaxLabels.md) | Get/set the maximum amount of numbers on the axis |
| [MinGrace](MinGrace/MinGrace.md) | Get/set the "tolerance" value for the axis minimum |
| [MaxGrace](MaxGrace/MaxGrace.md) | Get/set the "tolerance" value for the axis maximum |
| [SelectAxisScale](SelectAxisScale/SelectAxisScale.md) | Auto scale the axis. |