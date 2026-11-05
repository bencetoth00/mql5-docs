# ArrayIsDynamic

ArrayIsDynamic

The function checks whether an array is dynamic.

|  |
| --- |
| bool  ArrayIsDynamic(     const void&  array[]    // checked array     ); |

Parameters

array[]

[in]  Checked array.

Return Value

It returns true if the selected array is [dynamic](../../Language-Basics/Data-Types/Dynamic-Array-Object/Dynamic-Array-Object.md), otherwise it returns false.

Example:

|  |
| --- |
| #property description "This indicator does not calculate values. It makes a single attempt to"  #property description "apply the call of ArrayFree() function to three arrays: dynamic one, static one and"  #property description "an indicator buffer. Results are shown in Experts journal."  //--- indicator settings  #property indicator\_chart\_window  #property indicator\_buffers 1  #property indicator\_plots   1  //--- global variables  double ExtDynamic[];   // dynamic array  double ExtStatic[100]; // static array  bool   ExtFlag=true;   // flag  double ExtBuff[];      // indicator buffer  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- allocate memory for the array     ArrayResize(ExtDynamic,100);  //--- indicator buffers mapping     SetIndexBuffer(0,ExtBuff);     PlotIndexSetDouble(0,PLOT\_EMPTY\_VALUE,0);  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const int begin,                  const double &price[])    {  //--- perform a single analysis     if(ExtFlag)       {        //--- attempt to free memory for arrays        //--- 1. Dynamic array        Print("+============================+");        Print("1. Check dynamic array:");        Print("Size before memory is freed = ",ArraySize(ExtDynamic));        Print("Is this a dynamic array = ",ArrayIsDynamic(ExtDynamic) ? "Yes" : "No");        //--- attempt to free array memory        ArrayFree(ExtDynamic);        Print("Size after memory is freed = ",ArraySize(ExtDynamic));        //--- 2. Static array        Print("2. Check static array:");        Print("Size before memory is freed = ",ArraySize(ExtStatic));        Print("Is this a dynamic array = ",ArrayIsDynamic(ExtStatic) ? "Yes" : "No");        //--- attempt to free array memory        ArrayFree(ExtStatic);        Print("Size after memory is freed = ",ArraySize(ExtStatic));        //--- 3. Indicator buffer        Print("3. Check indicator buffer:");        Print("Size before memory is freed = ",ArraySize(ExtBuff));        Print("Is this a dynamic array = ",ArrayIsDynamic(ExtBuff) ? "Yes" : "No");        //--- attempt to free array memory        ArrayFree(ExtBuff);        Print("Size after memory is freed = ",ArraySize(ExtBuff));        //--- change the flag value        ExtFlag=false;       }  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Access to timeseries and indicators](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md)
