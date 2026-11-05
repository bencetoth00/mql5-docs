# History Data Structure

# MqlRates

This structure stores information about the prices, volumes and spread.

```cpp
struct MqlRates
  {
   datetime time;         // Period start time
   double   open;         // Open price
   double   high;         // The highest price of the period
   double   low;          // The lowest price of the period
   double   close;        // Close price
   long     tick_volume;  // Tick volume
   int      spread;       // Spread
   long     real_volume;  // Trade volume
  };
```

 

Example:

```cpp
void OnStart()
  {
   MqlRates rates[];
   int copied=CopyRates(NULL,0,0,100,rates);
   if(copied<=0)
      Print("Error copying price data ",GetLastError());
   else Print("Copied ",ArraySize(rates)," bars");
  }
```

See also

[CopyRates](../../../Timeseries-and-Indicators-Access/CopyRates/CopyRates.md), [Access to timeseries](../../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md)