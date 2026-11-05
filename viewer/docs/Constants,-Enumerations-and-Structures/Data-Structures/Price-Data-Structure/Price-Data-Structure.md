# Price Data Structure

# The Structure for Returning Current Prices (MqlTick)

This is a structure for storing the latest prices of the symbol. It is designed for fast retrieval of the most requested information about current prices.

```cpp
struct MqlTick
  {
   datetime     time;          // Time of the last prices update
   double       bid;           // Current Bid price
   double       ask;           // Current Ask price
   double       last;          // Price of the last deal (Last)
   ulong        volume;        // Volume for the current Last price
   long         time_msc;      // Time of a price last update in milliseconds
   uint         flags;         // Tick flags
   double       volume_real;   // Volume for the current Last price with greater accuracy
  };
```

The variable of the MqlTick type allows obtaining values of Ask, Bid, Last and Volume within a  single call of the [SymbolInfoTick()](../../../Market-Info/SymbolInfoTick/SymbolInfoTick.md) function.

The parameters of each tick are filled in regardless of whether there are changes compared to the previous tick. Thus, it is possible to find out a correct price for any moment in the past without the need to search for previous values at the tick history. For example, even if only a Bid price changes during a tick arrival, the structure still contains other parameters as well, including the previous Ask price, volume, etc.

You can analyze the tick flags to find out what data have been changed exactly:

- TICK\_FLAG\_BID –  tick has changed a Bid price
- TICK\_FLAG\_ASK  – a tick has changed an Ask price
- TICK\_FLAG\_LAST – a tick has changed the last deal price
- TICK\_FLAG\_VOLUME – a tick has changed a volume
- TICK\_FLAG\_BUY – a tick is a result of a buy deal
- TICK\_FLAG\_SELL – a tick is a result of a sell deal

Example:

```cpp
void OnTick()
  {
   MqlTick last_tick;
//---
   if(SymbolInfoTick(Symbol(),last_tick))
     {
      Print(last_tick.time,": Bid = ",last_tick.bid,
            " Ask = ",last_tick.ask,"  Volume = ",last_tick.volume);
     }
   else Print("SymbolInfoTick() failed, error = ",GetLastError());
//---
  }
```

See also

[Structures and Classes](../../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md), [CopyTicks()](../../../Timeseries-and-Indicators-Access/CopyTicks/CopyTicks.md), [SymbolInfoTick()](../../../Market-Info/SymbolInfoTick/SymbolInfoTick.md)