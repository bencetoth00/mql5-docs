# Connection between Indicator Properties and Functions

Connection between Indicator Properties and Corresponding Functions

Every custom indicator has numerous [properties](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md), some of which are obligatory and are always positioned at the beginning of description. They are the following properties:

- indication of a window to plot the indicator – indicator\_separate\_window or indicator\_chart\_window;
- number of indicator buffers – indicator\_buffers;
- number of plots of the indicator – indicator\_plots.

Also there are other properties that can be set both through [preprocessor](../../Language-Basics/Preprocessor/Preprocessor.md) directives and through functions intended for custom indicator creation. These properties and corresponding functions are described in the following table.

| Directives for properties of indicator subwindow | Functions of IndicatorSet...() type | Description of the adjusted property of the subwindow |
| --- | --- | --- |
| indicator\_height | [IndicatorSetInteger](../PlotIndexSetInteger/PlotIndexSetInteger.md)([INDICATOR\_INDICATOR\_HEIGHT](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_integer), nHeight) | The fixed value of the subwindow height |
| indicator\_minimum | [IndicatorSetDouble](../IndicatorSetDouble/IndicatorSetDouble.md)([INDICATOR\_MINIMUM](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_double), dMaxValue) | Minimal value of the vertical axis |
| indicator\_maximum | [IndicatorSetDouble](../IndicatorSetDouble/IndicatorSetDouble.md)([INDICATOR\_MAXIMUM](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_double), dMinValue) | Maximal value of the vertical axis |
| indicator\_levelN | [IndicatorSetDouble](../IndicatorSetDouble/IndicatorSetDouble.md)([INDICATOR\_LEVELVALUE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_double), N-1, nLevelValue) | Vertical axis value for N level |
| no preprocessor directive | [IndicatorSetString](../IndicatorSetString/IndicatorSetString.md)([INDICATOR\_LEVELTEXT](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string), N-1, sLevelName) | Name of a displayed level |
| indicator\_levelcolor | [IndicatorSetInteger](../PlotIndexSetInteger/PlotIndexSetInteger.md)([INDICATOR\_LEVELCOLOR](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_integer), N-1, nLevelColor) | Color of N level |
| indicator\_levelwidth | [IndicatorSetInteger](../PlotIndexSetInteger/PlotIndexSetInteger.md)([INDICATOR\_LEVELWIDTH](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_integer), N-1, nLevelWidth) | Line width for N level |
| indicator\_levelstyle | [IndicatorSetInteger](../PlotIndexSetString/PlotIndexSetString.md)([INDICATOR\_LEVELSTYLE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_integer), N-1, nLevelStyle) | Line style for N level |
| Directives for plotting properties | Functions of PlotIndexSet...() type | Description of the adjusted property of a plot |
| indicator\_labelN | [PlotIndexSetString](../PlotIndexSetString/PlotIndexSetString.md)(N-1,[PLOT\_LABEL](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_plot_property_string),sLabel) | Short name of the number N plot. It is displayed in DataWindow and in the pop-up tooltip when pointing the mouse cursor over it |
| indicator\_colorN | [PlotIndexSetInteger](../PlotIndexSetInteger/PlotIndexSetInteger.md)(N-1, [PLOT\_LINE\_COLOR](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_plot_property_string), nColor) | Line color for N plot |
| indicator\_styleN | [PlotIndexSetInteger](../PlotIndexSetInteger/PlotIndexSetInteger.md)(N-1, [PLOT\_LINE\_STYLE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_integer), nType) | Line style for N plot |
| indicator\_typeN | [PlotIndexSetInteger](../PlotIndexSetInteger/PlotIndexSetInteger.md)(N-1, [PLOT\_DRAW\_TYPE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md), nType) | Line type for N plot |
| indicator\_widthN | [PlotIndexSetInteger](../PlotIndexSetInteger/PlotIndexSetInteger.md)(N-1, [PLOT\_LINE\_WIDTH](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_plot_property_integer), nWidth) | Line width for N plot |
| Common indicator properties | Functions of IndicatorSet...() type | Description |
| no preprocessor directive | [IndicatorSetString](../IndicatorSetString/IndicatorSetString.md)([INDICATOR\_SHORTNAME](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string), sShortName) | Sets the convenient short name of the indicator that will be displayed in the list of indicators (opened in the terminal by pressing Ctrl+I). |
| no preprocessor directive | [IndicatorSetInteger](../IndicatorSetInteger/IndicatorSetInteger.md)([INDICATOR\_DIGITS](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_integer), nDigits) | Sets required accuracy of display of indicator values - number of decimal places |
| no preprocessor directive | [IndicatorSetInteger](../IndicatorSetInteger/IndicatorSetInteger.md)([INDICATOR\_LEVELS](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_integer), nLevels) | Sets number of levels in the indicator window |
| indicator\_applied\_price | No function, the property can be set only by the preprocessor directive. | Default price type used for the indicator calculation. It is specified when necessary, only if OnCalculate() of the first type is used.  The property value can also be set from the dialog of indicator properties in the "Parameters" tab - ["Apply to"](../../Technical-Indicators/iCustom/iCustom.md#applyto). |

It should be noted that numeration of levels and plots in preprocessor terms starts with one, while numeration of the same properties at using functions starts with zero, i.e. the indicated value must be by 1 less than that indicated for #property.

There are several directives, for which there are no corresponding functions:

| Directive | Description |
| --- | --- |
| indicator\_chart\_window | Indicator is displayed in the main window |
| indicator\_separate\_window | Indicator is displayed in a separate subwindow |
| indicator\_buffers | Number of required indicator buffers |
| indicator\_plots | Number of [plots](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) in the indicator |
