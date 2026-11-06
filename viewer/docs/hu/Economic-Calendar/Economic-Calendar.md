# Gazdasági naptár

# A gazdasági naptár függvényei

Ez a fejezet a MetaTrader platformon közvetlenül elérhető [gazdasági naptár](https://www.metatrader5.com/en/terminal/help/charts_analysis/fundamental) kezelésére szolgáló függvényeket ismerteti. A naptár makrogazdasági mutatókat, azok közzétételi időpontját és fontosságát leíró adatbázis. A mutatók aktuális értékei közzétételükkor megjelennek a MetaTraderben, a diagramon pedig címkék segítik a kívánt mutatók ország, deviza és fontosság szerinti követését.

A gazdasági naptár függvényei a kereskedési szerver idejét használják ([TimeTradeServer](../Date-and-Time/TimeTradeServer/TimeTradeServer.md)). Ezért az [MqlCalendarValue](../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue) struktúrában szereplő időpont és a [CalendarValueHistoryByEvent](CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md), illetve a [CalendarValueHistory](CalendarValueHistory/CalendarValueHistory.md) függvények időparaméterei a szerver időzónájában értendők, nem a felhasználó helyi ideje szerint.

A [gazdasági naptár függvényeivel](Economic-Calendar.md) automatikusan elemezhetők a beérkező események, egyéni fontossági feltételek, valamint a szükséges országok és devizák alapján.

| Függvény | Működés |
| --- | --- |
| [CalendarCountryById](CalendarCountryById/CalendarCountryById.md) | Lekéri az ország leírását azonosító alapján. |
| [CalendarEventById](CalendarEventById/CalendarEventById.md) | Lekéri az esemény leírását azonosító alapján. |
| [CalendarValueById](CalendarValueById/CalendarValueById.md) | Lekéri az eseményérték leírását azonosító alapján. |
| [CalendarCountries](CalendarCountries/CalendarCountries.md) | Visszaadja a naptárban elérhető országnevek tömbjét. |
| [CalendarEventByCountry](CalendarEventByCountry/CalendarEventByCountry.md) | Visszaadja a megadott országkódhoz tartozó összes eseményleírás tömbjét. |
| [CalendarEventByCurrency](CalendarEventByCurrency/CalendarEventByCurrency.md) | Visszaadja a megadott devizához tartozó eseményleírások tömbjét. |
| [CalendarValueHistoryByEvent](CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md) | Visszaadja egy esemény azonosítójához tartozó értékek tömbjét a megadott időszakból. |
| [CalendarValueHistory](CalendarValueHistory/CalendarValueHistory.md) | Visszaadja az adott időszak összes eseményértékét, ország és/vagy deviza szerinti rendezési lehetőséggel. |
| [CalendarValueLastByEvent](CalendarValueLastByEvent/CalendarValueLastByEvent.md) | A megadott change_id óta bekövetkezett adatbázis-változásokhoz tartozó eseményértékeket adja vissza az esemény azonosítója alapján. |
| [CalendarValueLast](CalendarValueLast/CalendarValueLast.md) | A megadott change_id óta bekövetkezett adatbázis-változások összes eseményértékét adja vissza, ország és/vagy deviza szerinti rendezési lehetőséggel. |
