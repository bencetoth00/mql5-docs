# Matematikai függvények

# Matematikai függvények

Matematikai és trigonometriai függvények gyűjteménye.

A matematikai függvényeket eredetileg skalárértékek műveleteihez tervezték. Ettől a verziótól kezdve a legtöbb függvény [mátrixokra és vektorokra](../Language-Basics/Data-Types/Matrices-and-vectors/Matrices-and-vectors.md) is alkalmazható. Ide tartozik a MathAbs, MathArccos, MathArcsin, MathArctan, MathCeil, MathCos, MathExp, MathFloor, MathLog, MathLog10, MathMod, MathPow, MathRound, MathSin, MathSqrt, MathTan, MathExpm1, MathLog1p, MathArccosh, MathArcsinh, MathArctanh, MathCosh, MathSinh és MathTanh. Ilyenkor a művelet a mátrix vagy vektor minden elemére külön végrehajtódik. Példa:

```cpp
//---
  matrix a= {{1, 4}, {9, 16}};
  Print("matrix a=\n",a);
  a=MathSqrt(a);
  Print("MatrSqrt(a)=\n",a);
  /*
   matrix a=
   [[1,4]
    [9,16]]
   MatrSqrt(a)=
   [[1,2]
    [3,4]]
  */
```

A [MathMod](MathMod/MathMod.md) és a [MathPow](MathPow/MathPow.md) esetében a második operandus skalár, illetve megfelelő méretű mátrix vagy vektor is lehet.

| Függvény | Működés |
| --- | --- |
| [MathAbs](MathAbs/MathAbs.md) | Visszaadja a megadott szám abszolút értékét. |
| [MathArccos](MathArccos/MathArccos.md) | Visszaadja x arkusz koszinuszát radiánban. |
| [MathArcsin](MathArcsin/MathArcsin.md) | Visszaadja x arcszinuszát radiánban. |
| [MathArctan](MathArctan/MathArctan.md) | Visszaadja x arkusz tangensét radiánban. |
| [MathArctan2](MathArctan2/MathArctan2.md) | Visszaadja azt a szöget radiánban, amelynek tangense a két megadott szám hányadosa. |
| [MathClassify](MathClassify/MathClassify.md) | Visszaadja a valós szám típusát. |
| [MathCeil](MathCeil/MathCeil.md) | A számnál nem kisebb legközelebbi egész számot adja vissza. |
| [MathCos](MathCos/MathCos.md) | Visszaadja a szám koszinuszát. |
| [MathExp](MathExp/MathExp.md) | Visszaadja a szám exponenciális függvényének értékét. |
| [MathFloor](MathFloor/MathFloor.md) | A számnál nem nagyobb legközelebbi egész számot adja vissza. |
| [MathLog](MathLog/MathLog.md) | Visszaadja a természetes logaritmust. |
| [MathLog10](MathLog10/MathLog10.md) | Visszaadja a szám tízes alapú logaritmusát. |
| [MathMax](MathMax/MathMax.md) | Visszaadja a két szám közül a nagyobbat. |
| [MathMin](MathMin/MathMin.md) | Visszaadja a két szám közül a kisebbet. |
| [MathMod](MathMod/MathMod.md) | Visszaadja két szám osztásának valós maradékát. |
| [MathPow](MathPow/MathPow.md) | A megadott hatványra emeli az alapot. |
| [MathRand](MathRand/MathRand.md) | Ál-véletlen értéket ad vissza 0 és 32767 között. |
| [MathRound](MathRound/MathRound.md) | A legközelebbi egész számra kerekít. |
| [MathSin](MathSin/MathSin.md) | Visszaadja a szám szinuszát. |
| [MathSqrt](MathSqrt/MathSqrt.md) | Visszaadja a négyzetgyököt. |
| [MathSrand](MathSrand/MathSrand.md) | Beállítja az ál-véletlen egész számok sorozatának kezdőértékét. |
| [MathTan](MathTan/MathTan.md) | Visszaadja a szám tangensét. |
| [MathIsValidNumber](MathIsValidNumber/MathIsValidNumber.md) | Ellenőrzi, hogy érvényes-e a valós szám. |
| [MathExpm1](MathExpm1/MathExpm1.md) | Visszaadja a `MathExp(x)-1` kifejezés értékét. |
| [MathLog1p](MathLog1p/MathLog1p.md) | Visszaadja a `MathLog(1+x)` kifejezés értékét. |
| [MathArccosh](MathArccosh/MathArccosh.md) | Visszaadja a hiperbolikus arkusz koszinuszát. |
| [MathArcsinh](MathArcsinh/MathArcsinh.md) | Visszaadja a hiperbolikus arkusz szinuszát. |
| [MathArctanh](MathArctanh/MathArctanh.md) | Visszaadja a hiperbolikus arkusz tangensét. |
| [MathCosh](MathCosh/MathCosh.md) | Visszaadja a szám hiperbolikus koszinuszát. |
| [MathSinh](MathSinh/MathSinh.md) | Visszaadja a szám hiperbolikus szinuszát. |
| [MathTanh](MathTanh/MathTanh.md) | Visszaadja a szám hiperbolikus tangensét. |
| [MathSwap](MathSwap/MathSwap.md) | Megfordítja az ushort/uint/ushort típusú érték bájtjainak sorrendjét. |
