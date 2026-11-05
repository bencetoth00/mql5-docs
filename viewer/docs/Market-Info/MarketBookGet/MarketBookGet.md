# MarketBookGet


Returns a structure array [MqlBookInfo](../../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md) containing records of the Depth of Market of a specified symbol.

```cpp
bool  MarketBookGet(
   string        symbol,     // symbol
   MqlBookInfo&  book[]      // reference to an array
   );
```

Parameters

symbol

[in] Symbol name.

book[]

[in] Reference to an array of Depth of Market records. The array can be pre-allocated for a sufficient number of records. If a [dynamic array](../../Language-Basics/Data-Types/Dynamic-Array-Object/Dynamic-Array-Object.md) hasn't been pre-allocated in the operating memory, the client terminal will distribute the array itself.

Return Value

Returns true in case of success, otherwise false.

Note

The Depth of Market must be pre-opened by the [MarketBookAdd()](../MarketBookAdd/MarketBookAdd.md) function.

Example:

```cpp
   MqlBookInfo priceArray[];
   bool getBook=MarketBookGet(NULL,priceArray);
   if(getBook)
     {
      int size=ArraySize(priceArray);
      Print("MarketBookInfo for ",Symbol());
      for(int i=0;i<size;i++)
        {
         Print(i+":",priceArray[i].price
               +"    Volume = "+priceArray[i].volume,
               " type = ",priceArray[i].type);
        }
     }
   else
     {
      Print("Could not get contents of the symbol DOM ",Symbol());
     }
```

See also

[Structure of Depth of Market](../../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md), [Structures and Classes](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md)