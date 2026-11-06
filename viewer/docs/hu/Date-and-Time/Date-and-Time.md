# Dátum és idő

Ez a függvénycsoport a [datetime](../Language-Basics/Data-Types/Integer-Types/Datetime-Type/Datetime-Type.md) típusú adatok kezelésére szolgál. Ez egy egész szám, amely az 1970. január 1-jei 0 óra óta eltelt másodperceket jelöli.

Nagy felbontású számlálókhoz és időzítőkhöz használd a [GetTickCount()](../Common-Functions/GetTickCount/GetTickCount.md) függvényt, amely ezredmásodpercben adja meg az értékeket.

| Függvény | Működés |
| --- | --- |
| [TimeCurrent](TimeCurrent/TimeCurrent.md) | Az utolsó ismert szerveridőt, vagyis az utolsó jegyzés érkezési idejét adja vissza datetime formátumban. |
| [TimeTradeServer](TimeTradeServer/TimeTradeServer.md) | A kereskedési szerver aktuális számított idejét adja vissza. |
| [TimeLocal](TimeLocal/TimeLocal.md) | A számítógép helyi idejét adja vissza datetime formátumban. |
| [TimeGMT](TimeGMT/TimeGMT.md) | A GMT-időt adja vissza datetime formátumban, a terminált futtató számítógép helyi nyári időszámítását figyelembe véve. |
| [TimeDaylightSavings](TimeDaylightSavings/TimeDaylightSavings.md) | A nyári időszámítás váltásának előjelét adja vissza. |
| [TimeGMTOffset](TimeGMTOffset/TimeGMTOffset.md) | A GMT és a helyi számítógépidő közötti, másodpercben kifejezett aktuális eltérést adja vissza, a nyári időszámítást is figyelembe véve. |
| [TimeToStruct](TimeToStruct/TimeToStruct.md) | A datetime értéket MqlDateTime típusú struktúrát használó változóvá alakítja. |
| [StructToTime](StructToTime/StructToTime.md) | Az MqlDateTime típusú struktúrát használó változót datetime értékké alakítja. |
