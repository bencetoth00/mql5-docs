# Bars

Bars

Returns the number of bars count in the history for a specified symbol and period. There are 2 variants of functions calls.

Request all of the history bars

|  |
| --- |
| int  Bars(     string           symbol\_name,     // symbol name     ENUM\_TIMEFRAMES  timeframe        // period     ); |

Request the history bars for the selected time interval

|  |
| --- |
| int  Bars(     string           symbol\_name,     // symbol name     ENUM\_TIMEFRAMES  timeframe,       // period     datetime         start\_time,      // start date and time     datetime         stop\_time        // end date and time     ); |

Parameters

symbol\_name

[in]  Symbol name.

timeframe

[in]  Period.

start\_time

[in]  Bar time corresponding to the first element.

stop\_time

[in]  Bar time corresponding to the last element.

Return Value

If the start\_time and stop\_time parameters are defined, the function returns the number of bars in the specified time interval, otherwise it returns the total number of bars.

Note

If data for the timeseries with specified parameters are not formed in the terminal by the time of the Bars() function call, or data of the timeseries are not [synchronized](../Organizing-Data-Access/Organizing-Data-Access.md#synchronized) with a trade server by the moment of the function call, the function returns a zero value.

When requesting the number of bars in a specified time interval, only bars with an open time falling within the interval are considered. For example, if the current day of the week is Saturday and the request is made for the number of W1 bars with start\_time=last\_tuesday and stop\_time=last\_friday, the function will return 0 since the open time of a W1 timeframe is always Sunday and not a single W1 bar falls within the specified interval.

Sample request for the number of all history bars:

|  |
| --- |
| int bars=Bars(\_Symbol,\_Period);     if(bars>0)       {        Print("Number of bars in the terminal history for the symbol-period at the moment = ",bars);       }     else  //no available bars       {        //--- data on the symbol might be not synchronized with data on the server        bool synchronized=false;        //--- loop counter        int attempts=0;        // make 5 attempts to wait for synchronization        while(attempts<5)          {           if(SeriesInfoInteger(Symbol(),0,SERIES\_SYNCHRONIZED))             {              //--- synchronization done, exit              synchronized=true;              break;             }           //--- increase the counter           attempts++;           //--- wait 10 milliseconds till the next iteration           Sleep(10);          }        //--- exit the loop after synchronization        if(synchronized)          {           Print("Number of bars in the terminal history for the symbol-period at the moment = ",bars);           Print("The first date in the terminal history for the symbol-period at the moment = ",                 (datetime)SeriesInfoInteger(Symbol(),0,SERIES\_FIRSTDATE));           Print("The first date in the history for the symbol on the server = ",                 (datetime)SeriesInfoInteger(Symbol(),0,SERIES\_SERVER\_FIRSTDATE));          }        //--- synchronization of data didn't happen        else          {           Print("Failed to get number of bars for ",\_Symbol);          }       } |

Sample request for the number of bars in the specified interval:

|  |
| --- |
| int n;     datetime date1 = D'2016.09.02 23:55'; // Friday     datetime date2 = D'2016.09.05 00:00'; // Monday     datetime date3 = D'2016.09.08 00:00'; // Thursday     //---     n=Bars(\_Symbol,PERIOD\_H1,D'2016.09.02 02:05',D'2016.09.02 10:55');     Print("Number of bars: ",n); // Output: "Number of bars: 8", H2 bar is considered in the calculation, while H11 one is not     n=Bars(\_Symbol,PERIOD\_D1,date1,date2);     Print("Number of bars: ",n); // Output: "Number of bars: 1", since an open time of a single D1 (Monday) bar falls within the interval     n=Bars(\_Symbol,PERIOD\_W1,date2,date3);     Print("Number of bars: ",n); // Output: "Number of bars: 0", since not a single W1 bar open time falls within the specified interval |

See also

[Event Handling Functions](../../Event-Handling/OnCalculate/OnCalculate.md)
