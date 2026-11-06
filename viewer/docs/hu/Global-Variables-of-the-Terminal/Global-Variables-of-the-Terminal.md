# A terminál globális változói

# Az ügyfélterminál globális változói

Ez a függvénycsoport az ügyfélterminál globális változóinak kezelésére szolgál.

Ezeket nem szabad összekeverni az MQL5-program [globális hatókörében](../Language-Basics/Variables/Global-Variables/Global-Variables.md) deklarált változókkal.

Az ügyfélterminál globális változóit a terminál az utolsó hozzáféréstől számított négy hétig tárolja, majd automatikusan törli. Hozzáférésnek nemcsak az új érték beállítása, hanem a változó értékének beolvasása is számít.

Az ügyfélterminálban futó összes MQL5-program egyszerre hozzáférhet ezekhez a globális változókhoz.

| Függvény | Működés |
| --- | --- |
| [GlobalVariableCheck](GlobalVariableCheck/GlobalVariableCheck.md) | Ellenőrzi, hogy létezik-e a megadott nevű globális változó. |
| [GlobalVariableTime](GlobalVariableTime/GlobalVariableTime.md) | Visszaadja a globális változó utolsó elérésének időpontját. |
| [GlobalVariableDel](GlobalVariableDel/GlobalVariableDel.md) | Töröl egy globális változót. |
| [GlobalVariableGet](GlobalVariableGet/GlobalVariableGet.md) | Visszaadja egy globális változó értékét. |
| [GlobalVariableName](GlobalVariableName/GlobalVariableName.md) | A globális változók listájában elfoglalt sorszáma alapján visszaadja a változó nevét. |
| [GlobalVariableSet](GlobalVariableSet/GlobalVariableSet.md) | Beállítja egy globális változó új értékét. |
| [GlobalVariablesFlush](GlobalVariablesFlush/GlobalVariablesFlush.md) | Kényszerítetten lemezre menti az összes globális változó tartalmát. |
| [GlobalVariableTemp](GlobalVariableTemp/GlobalVariableTemp.md) | Új értéket állít be a globális változónak, amely csak az aktuális terminálmunkamenetben létezik. |
| [GlobalVariableSetOnCondition](GlobalVariableSetOnCondition/GlobalVariableSetOnCondition.md) | Feltételtől függően beállítja egy meglévő globális változó új értékét. |
| [GlobalVariablesDeleteAll](GlobalVariablesDeleteAll/GlobalVariablesDeleteAll.md) | Törli azokat a globális változókat, amelyek neve a megadott előtaggal kezdődik. |
| [GlobalVariablesTotal](GlobalVariablesTotal/GlobalVariablesTotal.md) | Visszaadja a globális változók teljes számát. |
