# Konverziós függvények

Ez a függvénycsoport különböző formátumú adatok átalakítására szolgál.

Kiemelendő a [NormalizeDouble()](NormalizeDouble/NormalizeDouble.md) függvény, amely biztosítja az árak megfelelő pontosságú megjelenítését. Kereskedési műveleteknél csak a kereskedési szerver által megkövetelt pontosságra normalizált ár használható.

| Függvény | Működés |
| --- | --- |
| [CharToString](CharToString/CharToString.md) | Egy karakter kódját egykarakteres karakterlánccá alakítja. |
| [DoubleToString](DoubleToString/DoubleToString.md) | Numerikus értéket a megadott pontosságú szöveggé alakít. |
| [EnumToString](EnumToString/EnumToString.md) | Bármilyen típusú felsorolás értékét karakterlánccá alakítja. |
| [NormalizeDouble](NormalizeDouble/NormalizeDouble.md) | Lebegőpontos számot a megadott pontosságra kerekít. |
| [StringToDouble](StringToDouble/StringToDouble.md) | Számot ábrázoló karakterláncot double típusú számmá alakít. |
| [StringToInteger](StringToInteger/StringToInteger.md) | Számot ábrázoló karakterláncot long típusú számmá alakít. |
| [StringToTime](StringToTime/StringToTime.md) | A `yyyy.mm.dd [hh:mi]` formátumú dátumot vagy időt tartalmazó karakterláncot datetime típusúvá alakítja. |
| [TimeToString](TimeToString/TimeToString.md) | Az 1970.01.01. óta eltelt másodperceket tartalmazó értéket `yyyy.mm.dd hh:mi` formátumú karakterlánccá alakítja. |
| [IntegerToString](IntegerToString/IntegerToString.md) | int értéket a megadott hosszúságú karakterlánccá alakít. |
| [ShortToString](ShortToString/ShortToString.md) | Unicode karakterkódot egykarakteres karakterlánccá alakít. |
| [ShortArrayToString](ShortArrayToString/ShortArrayToString.md) | A tömb egy részét karakterláncba másolja. |
| [StringToShortArray](StringToShortArray/StringToShortArray.md) | Karakterenként átmásolja a karakterláncot egy ushort típusú tömb megadott részébe. |
| [CharArrayToString](CharArrayToString/CharArrayToString.md) | ANSI karakterkódokat karakterlánccá alakít. |
| [StringToCharArray](StringToCharArray/StringToCharArray.md) | A Unicode-ról ANSI-ra alakított karakterláncot karakterenként egy uchar tömb megadott részébe másolja. |
| [CharArrayToStruct](CharArrayToStruct/CharArrayToStruct.md) | uchar tömböt [POD-struktúrába](../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#simple_structure) másol. |
| [StructToCharArray](StructToCharArray/StructToCharArray.md) | [POD-struktúrát](../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#simple_structure) uchar tömbbe másol. |
| [ColorToARGB](ColorToARGB/ColorToARGB.md) | color típust uint típussá alakít az ARGB-ábrázolás lekéréséhez. |
| [ColorToPRGB](ColorToPRGB/ColorToPRGB.md) | A [color](../Language-Basics/Data-Types/Integer-Types/Color-Type/Color-Type.md) típust [uint](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#uint) típussá alakítja a premultiplikált ARGB, azaz PRGB-ábrázolás előállításához. |
| [ColorToString](ColorToString/ColorToString.md) | A színértéket `R,G,B` formátumú karakterlánccá alakítja. |
| [StringToColor](StringToColor/StringToColor.md) | Az `R,G,B` formátumú vagy színnevet tartalmazó karakterláncot color értékké alakítja. |
| [StringFormat](StringFormat/StringFormat.md) | Számot a megadott formátum szerinti karakterlánccá alakít. |

Lásd még: [Kódlap használata](../Constants,-Enumerations-and-Structures/Input-Output-Constants/Use-of-a-Codepage/Use-of-a-Codepage.md).
