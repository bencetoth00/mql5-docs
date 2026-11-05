# Price Constants

Price Constants

Calculations of technical indicators require price values and/or values of volumes, on which calculations will be performed. There are 7 predefined identifiers from the ENUM\_APPLIED\_PRICE enumeration, used to specify the desired price base for calculations.

ENUM\_APPLIED\_PRICE

| ID | Description |
| --- | --- |
| PRICE\_CLOSE | Close price |
| PRICE\_OPEN | Open price |
| PRICE\_HIGH | The maximum price for the period |
| PRICE\_LOW | The minimum price for the period |
| PRICE\_MEDIAN | Median price, (high + low)/2 |
| PRICE\_TYPICAL | Typical price, (high + low + close)/3 |
| PRICE\_WEIGHTED | Average price, (high + low + close + close)/4 |

If the volume is used in calculations, it's necessary to specify one of the two values from the ENUM\_APPLIED\_VOLUME enumeration.

ENUM\_APPLIED\_VOLUME

| ID | Description |
| --- | --- |
| VOLUME\_TICK | Tick volume |
| VOLUME\_REAL | Trade volume |

The [iStochastic()](../../../Technical-Indicators/iStochastic/iStochastic.md) technical Indicator can be calculated in two ways using:

- either only Close prices;
- or High and Low prices.

To select a necessary variant for calculation, specify one of the values of the ENUM\_STO\_PRICE enumeration.

ENUM\_STO\_PRICE

| ID | Description |
| --- | --- |
| STO\_LOWHIGH | Calculation is based on Low/High prices |
| STO\_CLOSECLOSE | Calculation is based on Close/Close prices |

If a technical indicator uses for calculations price data, type of which is set by ENUM\_APPLIED\_PRICE, then handle of any indicator (built in the terminal or written by a user) can be used as the input price series. In this case, values of the zero buffer of the indicator will be used for calculations. This makes it easy to build values of one indicator using values of another indicator. The handle of a custom indicator is created by calling the [iCustom()](../../../Technical-Indicators/iCustom/iCustom.md) function.

Example:

|  |
| --- |
| #property indicator\_separate\_window  #property indicator\_buffers 2  #property indicator\_plots   2  //--- input parameters  input int      RSIperiod=14;         // Period for calculating the RSI  input int      Smooth=8;             // Smoothing period RSI  input ENUM\_MA\_METHOD meth=MODE\_SMMA; // Method of smoothing  //---- plot RSI  #property indicator\_label1  "RSI"  #property indicator\_type1   DRAW\_LINE  #property indicator\_color1  clrRed  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  1  //---- plot RSI\_Smoothed  #property indicator\_label2  "RSI\_Smoothed"  #property indicator\_type2   DRAW\_LINE  #property indicator\_color2  clrNavy  #property indicator\_style2  STYLE\_SOLID  #property indicator\_width2  1  //--- indicator buffers  double         RSIBuffer[];          // Here we store the values of RSI  double         RSI\_SmoothedBuffer[]; // Here will be smoothed values of RSI  int            RSIhandle;            // Handle to the RSI indicator  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  void OnInit()    {  //--- indicator buffers mapping     SetIndexBuffer(0,RSIBuffer,INDICATOR\_DATA);     SetIndexBuffer(1,RSI\_SmoothedBuffer,INDICATOR\_DATA);     IndicatorSetString(INDICATOR\_SHORTNAME,"iRSI");     IndicatorSetInteger(INDICATOR\_DIGITS,2);  //---      RSIhandle=iRSI(NULL,0,RSIperiod,PRICE\_CLOSE);  //---    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                   const int prev\_calculated,                   const int begin,                   const double &price[]                   )       {  //---  Reset the value of the last error     ResetLastError();  //--- Get RSI indicator data in an array RSIBuffer []     int copied=CopyBuffer(RSIhandle,0,0,rates\_total,RSIBuffer);     if(copied<=0)       {        Print("Unable to copy the values of the indicator RSI. Error = ",              GetLastError(),",  copied =",copied);        return(0);       }  //--- Create the indicator of average values using values of RSI     int RSI\_MA\_handle=iMA(NULL,0,Smooth,0,meth,RSIhandle);     copied=CopyBuffer(RSI\_MA\_handle,0,0,rates\_total,RSI\_SmoothedBuffer);     if(copied<=0)       {        Print("Unable to copy the smoothed indicator of RSI. Error = ",              GetLastError(),",  copied =",copied);        return(0);       }  //--- return value of prev\_calculated for next call     return(rates\_total);    } |
