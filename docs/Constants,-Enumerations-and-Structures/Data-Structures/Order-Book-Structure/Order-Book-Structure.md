# Order Book Structure

MqlBookInfo

It provides information about the market depth data.

|  |
| --- |
| struct MqlBookInfo    {     ENUM\_BOOK\_TYPE   type;            // Order type from [ENUM\_BOOK\_TYPE](../../Trade-Constants/Trade-Orders-in-DOM/Trade-Orders-in-DOM.md) enumeration     double           price;           // Price     long             volume;          // Volume     double           volume\_real;     // Volume with greater accuracy    }; |

Note

The MqlBookInfo  structure is predefined, thus it doesn't require any declaration and description. To use the structure, just declare a variable of this type.

The DOM is available only for some symbols.

Example:

|  |
| --- |
| MqlBookInfo priceArray[];     bool getBook=MarketBookGet(NULL,priceArray);     if(getBook)       {        int size=ArraySize(priceArray);        Print("MarketBookInfo about ",Symbol());       }     else       {        Print("Failed to receive DOM for the symbol ",Symbol());       } |

See also

[MarketBookAdd](../../../Market-Info/MarketBookAdd/MarketBookAdd.md), [MarketBookRelease](../../../Market-Info/MarketBookRelease/MarketBookRelease.md), [MarketBookGet](../../../Market-Info/MarketBookGet/MarketBookGet.md), [Trade Orders in DOM](../../Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md), [Data Types](../../../Language-Basics/Data-Types/Data-Types.md)
