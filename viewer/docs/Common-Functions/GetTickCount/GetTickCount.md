# GetTickCount


The GetTickCount() function returns the number of milliseconds that elapsed since the system start.

```cpp
uint  GetTickCount();
```

Return Value

Value of uint type.

Note

Counter is limited by the restrictions of the system timer. Time is stored as an unsigned integer, so it's overfilled every 49.7 days if a computer works uninterruptedly.

Example:

```cpp
#define MAX_SIZE 40
//+------------------------------------------------------------------+
//| Script for measuring computation time of 40 Fibonacci numbers    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- Remember the initial value
   uint start=GetTickCount();
//--- A variable for getting the next number in the Fibonacci series
   long fib=0;
//--- In loop calculate the specified amount of numbers from Fibonacci series
   for(int i=0;i<MAX_SIZE;i++) fib=TestFibo(i);
//--- Get the spent time in milliseconds
   uint time=GetTickCount()-start;
//--- Output a message to the Experts journal
   PrintFormat("Calculating %d first Fibonacci numbers took %d ms",MAX_SIZE,time);
//--- Script completed
   return;
  }
//+------------------------------------------------------------------+
//| Function for getting Fibonacci number by its serial number       |
//+------------------------------------------------------------------+
long TestFibo(long n)
  {
//--- The first member of the Fibonacci series
   if(n<2) return(1);
//--- All other members are calculated by the following formula
   return(TestFibo(n-2)+TestFibo(n-1));
  }
```

See also

[Date and Time](../../Date-and-Time/Date-and-Time.md), [EventSetMillisecondTimer](../../Working-with-Events/EventSetMillisecondTimer/EventSetMillisecondTimer.md), [GetTickCount64](../GetTickCount64/GetTickCount64.md), [GetMicrosecondCount](../GetMicrosecondCount/GetMicrosecondCount.md)