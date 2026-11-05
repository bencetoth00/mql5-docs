# Order Book Structure

# MqlBookInfo

It provides information about the market depth data.

```cpp
struct MqlBookInfo
  {
   ENUM_BOOK_TYPE   type;            // Order type from ENUM_BOOK_TYPE enumeration
   double           price;           // Price
   long             volume;          // Volume
   double           volume_real;     // Volume with greater accuracy
  };
```

Note

The MqlBookInfo  structure is predefined, thus it doesn't require any declaration and description. To use the structure, just declare a variable of this type.

The DOM is available only for some symbols.

Example:

```cpp
   MqlBookInfo priceArray[];
   bool getBook=MarketBookGet(NULL,priceArray);
   if(getBook)
     {
      int size=ArraySize(priceArray);
      Print("MarketBookInfo about ",Symbol());
     }
   else
     {
      Print("Failed to receive DOM for the symbol ",Symbol());
     }
```

See also

[MarketBookAdd](../../../Market-Info/MarketBookAdd/MarketBookAdd.md), [MarketBookRelease](../../../Market-Info/MarketBookRelease/MarketBookRelease.md), [MarketBookGet](../../../Market-Info/MarketBookGet/MarketBookGet.md), [Trade Orders in DOM](../../Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md), [Data Types](../../../Language-Basics/Data-Types/Data-Types.md)