# Egyéni indikátorok

Ez a függvénycsoport egyéni indikátorok készítésére szolgál. Ezek a függvények Expert Advisorokban és szkriptekben nem használhatók.

| Függvény | Működés |
| --- | --- |
| [SetIndexBuffer](SetIndexBuffer/SetIndexBuffer.md) | A megadott indikátorpuffert egydimenziós dinamikus [double](../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) típusú [tömbhöz](../Language-Basics/Variables/Variables.md#array_define) rendeli. |
| [IndicatorSetDouble](IndicatorSetDouble/IndicatorSetDouble.md) | Beállítja az indikátor double típusú tulajdonságát. |
| [IndicatorSetInteger](IndicatorSetInteger/IndicatorSetInteger.md) | Beállítja az indikátor int típusú tulajdonságát. |
| [IndicatorSetString](IndicatorSetString/IndicatorSetString.md) | Beállítja az indikátor string típusú tulajdonságát. |
| [PlotIndexSetDouble](PlotIndexSetDouble/PlotIndexSetDouble.md) | Beállítja az indikátorvonal double típusú tulajdonságát. |
| [PlotIndexSetInteger](PlotIndexSetInteger/PlotIndexSetInteger.md) | Beállítja az indikátorvonal int típusú tulajdonságát. |
| [PlotIndexSetString](PlotIndexSetString/PlotIndexSetString.md) | Beállítja az indikátorvonal string típusú tulajdonságát. |
| [PlotIndexGetInteger](PlotIndexGetInteger/PlotIndexGetInteger.md) | Visszaadja az indikátorvonal egész típusú tulajdonságát. |

Az [indikátortulajdonságok](Connection-between-Indicator-Properties-and-Functions/Connection-between-Indicator-Properties-and-Functions.md) fordítói direktívákkal vagy függvényekkel állíthatók be. A működés megértéséhez tanulmányozd az [indikátorstílus-példákat](Indicator-Styles-in-Examples/Indicator-Styles-in-Examples.md).

Az egyéni indikátor minden szükséges számítását az előre meghatározott [OnCalculate()](../Event-Handling/OnCalculate/OnCalculate.md) függvényben kell elvégezni. Ha az OnCalculate() függvény rövid alakját használod, például:

```cpp
int OnCalculate (const int rates_total, const int prev_calculated, const int begin, const double& price[])
```

akkor a `rates_total` változó a `price[]` tömb elemeinek teljes számát tartalmazza. A tömb bemeneti paraméterként érkezik, és az indikátorértékek számításához használható.

A `prev_calculated` paraméter az OnCalculate() előző meghívásakor visszaadott érték. Segítségével úgy szervezhető meg a számítás, hogy a program megőrizze a korábban kiszámított értékeket. Ha például `rates_total = 1000`, `prev_calculated = 999`, akkor valószínűleg elegendő minden indikátorpufferben egyetlen új értéket kiszámítani.

Ha nem lehetne lekérdezni a `price` bemeneti tömb méretét, mind az 1000 értéket újra kellene számítani minden indikátorpufferben. Az OnCalculate() első meghívásakor a `prev_calculated` értéke 0. Ha a `price[]` tömb megváltozik, ez az érték szintén 0 lesz.

A `begin` paraméter azt mutatja meg, hány kezdeti érték nem tartalmaz számításhoz használható adatot. Ha például az Accelerator Oscillator értékei szolgálnak bemenetként, és az első 37 érték nincs kiszámítva, akkor `begin = 37`. Nézzünk egy egyszerű indikátort:

```cpp
#property indicator_chart_window
#property indicator_buffers 1
#property indicator_plots   1
//---- plot Label1
#property indicator_label1  "Label1"
#property indicator_type1   DRAW_LINE
#property indicator_color1  clrRed
#property indicator_style1  STYLE_SOLID
#property indicator_width1  1
//--- indicator buffers
double         Label1Buffer[];
//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
void OnInit()
  {
//--- indicator buffers mapping
   SetIndexBuffer(0,Label1Buffer,INDICATOR_DATA);
//---
  }
//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const int begin,
                const double &price[])
  {
//---
   Print("begin = ",begin,"  prev_calculated = ",prev_calculated,"  rates_total = ",rates_total);
//--- return value of prev_calculated for next call
   return(rates_total);
  }
```

Húzd az indikátort a Navigátor ablakból az Accelerator Oscillator ablakába, majd jelezd, hogy a számítás a korábban hozzáadott indikátor értékei alapján történjen:

![Indikátor számítása egy korábban hozzáadott indikátor értékei alapján](../assets/previousindicatorsdata.png "Indikátor számítása korábban hozzáadott indikátor értékei alapján")

Az OnCalculate() első meghívásakor a `prev_calculated` értéke 0. A további hívásokban a `rates_total` értékével egyezik meg, amíg nem nő az árdiagram gyertyáinak száma.

![A begin paraméter megadja, hány kezdeti gyertyához hiányzik érték](../assets/beginparameteronprevindabsent.png "A begin paraméter megadja, hány kezdeti gyertyához hiányzik érték")

A `begin` értéke pontosan azoknak a kezdeti gyertyáknak a száma, amelyekhez az Accelerator indikátor logikája szerint még nem készül érték. Az Accelerator.mq5 egyéni indikátor [OnInit()](../Event-Handling/OnInit/OnInit.md) függvényében a következő sort találjuk:

```cpp
//--- sets first bar from which index will be drawn
   PlotIndexSetInteger(0,PLOT_DRAW_BEGIN,37);
```

A [PlotIndexSetInteger](PlotIndexSetInteger/PlotIndexSetInteger.md) függvénnyel — a [PLOT\_DRAW\_BEGIN](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_plot_property_integer) tulajdonság beállításával — megadhatjuk, hány kezdeti érték hiányzik az egyéni indikátor nulla indexű tömbjéből, és ezért hány értéket kell kihagyni a számításból. Így lehetőség van:

1. megadni, hogy egy indikátor kezdeti értékei közül melyeket ne használja egy másik egyéni indikátor a számításhoz;
2. lekérdezni, hány kezdeti értéket kell figyelmen kívül hagyni egy másik egyéni indikátor meghívásakor, anélkül, hogy ismernénk annak számítási logikáját.
