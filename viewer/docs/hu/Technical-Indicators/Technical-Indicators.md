# Technikai indikátorok

# Technikai indikátorok függvényei

Az olyan függvények, mint az `iMA`, `iAC` és `iMACD`, létrehozzák a megfelelő technikai indikátor példányát a terminál globális gyorsítótárában. Ha azonos paraméterekkel már létezik példány, a rendszer azt használja új példány létrehozása helyett.

A függvények az indikátorpéldány leíróját adják vissza. Ezzel a leíróval kérhetők le a kiszámított értékek. Az indikátor 1–5 belső puffert is tartalmazhat; ezek adatai a [CopyBuffer()](../Timeseries-and-Indicators-Access/CopyBuffer/CopyBuffer.md) függvénnyel másolhatók át az MQL5-programba.

Az indikátorértékek közvetlenül a létrehozás után még nem feltétlenül állnak rendelkezésre, mert kiszámításuk időt igényel. Ezért célszerű a leírókat az `OnInit()` függvényben létrehozni. Az [iCustom()](iCustom/iCustom.md) függvény egyéni indikátort hoz létre. Az egyéni indikátorok legfeljebb 512 puffert tartalmazhatnak; tartalmuk szintén a `CopyBuffer()` függvénnyel olvasható ki.

Bármely technikai indikátor létrehozható az [IndicatorCreate()](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md) általános függvénnyel. Paraméterként a szimbólum nevét, az időkeretet, az indikátor típusát, a bemeneti paraméterek számát és az értékeket tartalmazó [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) tömböt kell megadni.

A már nem használt indikátor memóriafoglalása az [IndicatorRelease()](../Timeseries-and-Indicators-Access/IndicatorRelease/IndicatorRelease.md) függvénnyel szabadítható fel. Az indikátorfüggvények legalább két paramétere a szimbólum és az időkeret. A `NULL` szimbólum az aktuális instrumentumot, a `0` időkeret pedig az aktuális [időkeretet](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) jelenti.

| Függvény | A visszaadott indikátor |
| --- | --- |
| [iAC](iAC/iAC.md) | Gyorsulás/deceleráció indikátor |
| [iAD](iAD/iAD.md) | Felhalmozás/elosztás indikátor |
| [iADX](iADX/iADX.md) | Átlagos irányindex |
| [iAlligator](iAlligator/iAlligator.md) | Alligator indikátor |
| [iAMA](iAMA/iAMA.md) | Adaptív mozgóátlag |
| [iAO](iAO/iAO.md) | Awesome Oscillator |
| [iATR](iATR/iATR.md) | Valós tartomány átlaga |
| [iBands](iBands/iBands.md) | Bollinger-szalagok |
| [iCCI](iCCI/iCCI.md) | Áru-csatorna index |
| [iCustom](iCustom/iCustom.md) | Egyéni indikátor |
| [iIchimoku](iIchimoku/iIchimoku.md) | Ichimoku Kinko Hyo |
| [iMA](iMA/iMA.md) | Mozgóátlag |
| [iMACD](iMACD/iMACD.md) | Mozgóátlag-konvergencia/divergencia |
| [iMomentum](iMomentum/iMomentum.md) | Momentum |
| [iRSI](iRSI/iRSI.md) | Relatív erősség index |
| [iStochastic](iStochastic/iStochastic.md) | Sztochasztikus oszcillátor |
| [iVolumes](iVolumes/iVolumes.md) | Forgalom |
| [iWPR](iWPR/iWPR.md) | Williams százalékos tartomány |
