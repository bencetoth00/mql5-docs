# SignalBaseSelect

SignalBaseSelect

Selects a signal from signals, available in terminal for further working with it.

|  |
| --- |
| bool  SignalBaseSelect(     int     index     // signal index     ); |

Parameters

index

[in]  Signal index in base of trading signals.

Return Value

Returns true if successful, otherwise returns false. To read more about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Example:

|  |
| --- |
| void OnStart()    {  //--- get total amount of signals in the terminal     int total=SignalBaseTotal();  //--- process all signals     for(int i=0;i<total;i++)       {        //--- select the signal by index        if(SignalBaseSelect(i))          {           //--- get signal properties           long   id    =SignalBaseGetInteger(SIGNAL\_BASE\_ID);          // signal id           long   pips  =SignalBaseGetInteger(SIGNAL\_BASE\_PIPS);        // profit in pips           long   subscr=SignalBaseGetInteger(SIGNAL\_BASE\_SUBSCRIBERS); // number of subscribers           string name  =SignalBaseGetString(SIGNAL\_BASE\_NAME);         // signal name           double price =SignalBaseGetDouble(SIGNAL\_BASE\_PRICE);        // signal price           string curr  =SignalBaseGetString(SIGNAL\_BASE\_CURRENCY);     // signal currency           //--- print all profitable free signals with subscribers           if(price==0.0 && pips>0 && subscr>0)              PrintFormat("id=%d, name=\"%s\", currency=%s, pips=%d, subscribers=%d",id,name,curr,pips,subscr);          }        else PrintFormat("Error in call of SignalBaseSelect. Error code=%d",GetLastError());       }    } |
