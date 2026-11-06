# Diagramműveletek

A diagramtulajdonságokat beállító függvények ([ChartSetInteger](ChartSetInteger/ChartSetInteger.md), [ChartSetDouble](ChartSetDouble/ChartSetDouble.md), [ChartSetString](ChartSetString/ChartSetString.md)) aszinkronok: frissítési parancsot küldenek a diagramnak. Sikeres végrehajtáskor a parancs bekerül a diagram eseménysorába, a tulajdonságok módosítása pedig az eseménysor feldolgozásakor történik meg.

Ezért aszinkron függvény hívása után ne várj azonnali diagramfrissítést. A diagram megjelenésének és tulajdonságainak kényszerített frissítéséhez használd a [ChartRedraw()](ChartRedraw/ChartRedraw.md) függvényt.

| Függvény | Működés |
| --- | --- |
| [ChartApplyTemplate](ChartApplyTemplate/ChartApplyTemplate.md) | A megadott fájl sablonját alkalmazza a diagramra. |
| [ChartSaveTemplate](ChartSaveTemplate/ChartSaveTemplate.md) | Az aktuális diagrambeállításokat a megadott nevű sablonba menti. |
| [ChartWindowFind](ChartWindowFind/ChartWindowFind.md) | Visszaadja annak az alablaknak a számát, amelyben az indikátor megjelenik. |
| [ChartTimePriceToXY](ChartTimePriceToXY/ChartTimePriceToXY.md) | Az idő- és árkoordinátákat X és Y képernyőkoordinátává alakítja. |
| [ChartXYToTimePrice](ChartXYToTimePrice/ChartXYToTimePrice.md) | A diagram X és Y koordinátáit idő- és árértékké alakítja. |
| [ChartOpen](ChartOpen/ChartOpen.md) | Új diagramot nyit a megadott szimbólummal és időkerettel. |
| [ChartClose](ChartClose/ChartClose.md) | Bezárja a megadott diagramot. |
| [ChartFirst](ChartFirst/ChartFirst.md) | Visszaadja az ügyfélterminál első diagramjának azonosítóját. |
| [ChartNext](ChartNext/ChartNext.md) | Visszaadja a megadott diagram utáni diagram azonosítóját. |
| [ChartSymbol](ChartSymbol/ChartSymbol.md) | Visszaadja a megadott diagram szimbólumának nevét. |
| [ChartPeriod](ChartPeriod/ChartPeriod.md) | Visszaadja a megadott diagram időkeretét. |
| [ChartRedraw](ChartRedraw/ChartRedraw.md) | Kényszerített újrarajzolást indít a megadott diagramon. |
| [ChartSetDouble](ChartSetDouble/ChartSetDouble.md) | Beállítja a megadott diagram megfelelő tulajdonságának double értékét. |
| [ChartSetInteger](ChartSetInteger/ChartSetInteger.md) | Beállítja a megadott diagram megfelelő tulajdonságának egész típusú (datetime, int, color, bool vagy char) értékét. |
| [ChartSetString](ChartSetString/ChartSetString.md) | Beállítja a megadott diagram megfelelő tulajdonságának szöveges értékét. |
| [ChartGetDouble](ChartGetDouble/ChartGetDouble.md) | Visszaadja a megadott diagram tulajdonságának double értékét. |
| [ChartGetInteger](ChartGetInteger/ChartGetInteger.md) | Visszaadja a megadott diagram tulajdonságának egész típusú értékét. |
| [ChartGetString](ChartGetString/ChartGetString.md) | Visszaadja a megadott diagram tulajdonságának szöveges értékét. |
| [ChartNavigate](ChartNavigate/ChartNavigate.md) | A diagram megadott pozíciójához képest, a megadott számú gyertyával eltolja a diagramot. |
| [ChartID](ChartID/ChartID.md) | Visszaadja az aktuális diagram azonosítóját. |
| [ChartIndicatorAdd](ChartIndicatorAdd/ChartIndicatorAdd.md) | A megadott leírójú indikátort a diagram megadott ablakához adja. |
| [ChartIndicatorDelete](ChartIndicatorDelete/ChartIndicatorDelete.md) | A megadott nevű indikátort eltávolítja a diagram megadott ablakából. |
| [ChartIndicatorGet](ChartIndicatorGet/ChartIndicatorGet.md) | Visszaadja a diagram megadott ablakában található, rövid névvel azonosított indikátor leíróját. |
| [ChartIndicatorName](ChartIndicatorName/ChartIndicatorName.md) | Visszaadja az indikátorlistában a megadott sorszámú indikátor rövid nevét. |
| [ChartIndicatorsTotal](ChartIndicatorsTotal/ChartIndicatorsTotal.md) | Visszaadja a diagram megadott ablakára alkalmazott indikátorok számát. |
| [ChartWindowOnDropped](ChartWindowOnDropped/ChartWindowOnDropped.md) | Visszaadja annak az alablaknak az indexét, amelyre az Expert Advisort vagy szkriptet ráhúzták. |
| [ChartPriceOnDropped](ChartPriceOnDropped/ChartPriceOnDropped.md) | Visszaadja annak a diagrampontra helyezett objektumnak az árkoordinátáját, amelyre az Expert Advisort vagy szkriptet ráhúzták. |
| [ChartTimeOnDropped](ChartTimeOnDropped/ChartTimeOnDropped.md) | Visszaadja a diagrampontra helyezett objektum időkoordinátáját. |
| [ChartXOnDropped](ChartXOnDropped/ChartXOnDropped.md) | Visszaadja a diagrampontra helyezett objektum X koordinátáját. |
| [ChartYOnDropped](ChartYOnDropped/ChartYOnDropped.md) | Visszaadja a diagrampontra helyezett objektum Y koordinátáját. |
| [ChartSetSymbolPeriod](ChartSetSymbolPeriod/ChartSetSymbolPeriod.md) | Módosítja a megadott diagram szimbólumát és időkeretét. |
| [ChartScreenShot](ChartScreenShot/ChartScreenShot.md) | A diagram aktuális állapotáról GIF-, PNG- vagy BMP-képernyőképet készít a fájlkiterjesztéstől függően. |
