# Fájlkezelő függvények

Ez a függvénycsoport fájlok kezelésére szolgál.

Biztonsági okokból az MQL5 szigorúan szabályozza a fájlműveleteket. Az MQL5 eszközeivel kezelt fájlok csak a fájlsandboxon belül lehetnek.

A munkafájlok két könyvtárban és azok alkönyvtáraiban helyezhetők el:

- `terminal_data_folder\MQL5\FILES\` — a terminálban válaszd a Fájl → Adatmappa megnyitása menüpontot;
- a számítógépre telepített összes terminál közös mappája, amely általában a `C:\Documents and Settings\All Users\Application Data\MetaQuotes\Terminal\Common\Files` könyvtárban található.

A könyvtárak elérési útja programból is lekérhető a [TerminalInfoString()](../Checkup/TerminalInfoString/TerminalInfoString.md) függvénnyel és az [ENUM\_TERMINAL\_INFO\_STRING](../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_string) felsorolással:

```cpp
//--- Folder that stores the terminal data
   string terminal_data_path=TerminalInfoString(TERMINAL_DATA_PATH);
//--- Common folder for all client terminals
   string common_data_path=TerminalInfoString(TERMINAL_COMMONDATA_PATH);
```

Más könyvtárakban lévő fájlok kezelése nem engedélyezett.

Ha a fájlt írásra nyitod meg a [FileOpen()](FileOpen/FileOpen.md) függvénnyel, az útvonalban megadott, még nem létező alkönyvtárak automatikusan létrejönnek.

A fájlkezelő függvények úgynevezett névvel ellátott csövekkel is tudnak dolgozni. Ehhez a [FileOpen()](FileOpen/FileOpen.md) függvényt kell meghívni a megfelelő paraméterekkel.

| Függvény | Működés |
| --- | --- |
| [FileSelectDialog](FileSelectDialog/FileSelectDialog.md) | Fájl- vagy mappamegnyitó/-létrehozó párbeszédablakot jelenít meg. |
| [FileFindFirst](FileFindFirst/FileFindFirst.md) | A megadott szűrő alapján elkezdi a fájlok keresését egy könyvtárban. |
| [FileFindNext](FileFindNext/FileFindNext.md) | Folytatja a FileFindFirst() függvénnyel indított keresést. |
| [FileFindClose](FileFindClose/FileFindClose.md) | Lezárja a keresési leírót. |
| [FileOpen](FileOpen/FileOpen.md) | Megnyitja a megadott nevű fájlt a megadott jelzőkkel. |
| [FileDelete](FileDelete/FileDelete.md) | Törli a megadott fájlt. |
| [FileFlush](FileFlush/FileFlush.md) | Lemezre írja a bemeneti/kimeneti fájl pufferében maradt adatokat. |
| [FileGetInteger](FileGetInteger/FileGetInteger.md) | Lekéri egy fájl egész típusú tulajdonságát. |
| [FileIsEnding](FileIsEnding/FileIsEnding.md) | Olvasás közben megállapítja, hogy a fájl végére értünk-e. |
| [FileIsLineEnding](FileIsLineEnding/FileIsLineEnding.md) | Szövegfájl olvasásakor megállapítja, hogy a sor végére értünk-e. |
| [FileClose](FileClose/FileClose.md) | Bezár egy korábban megnyitott fájlt. |
| [FileIsExist](FileIsExist/FileIsExist.md) | Ellenőrzi, hogy létezik-e a fájl. |
| [FileCopy](FileCopy/FileCopy.md) | Helyi vagy közös mappából egy másik fájlba másolja a forrásfájlt. |
| [FileMove](FileMove/FileMove.md) | Áthelyez vagy átnevez egy fájlt. |
| [FileReadArray](FileReadArray/FileReadArray.md) | String kivételével bármilyen típusú tömböt olvas BIN fájlból. |
| [FileReadBool](FileReadBool/FileReadBool.md) | CSV-fájlból az aktuális pozíciótól az elválasztóig vagy a sor végéig olvas egy szöveget, majd bool értékké alakítja. |
| [FileReadDatetime](FileReadDatetime/FileReadDatetime.md) | CSV-fájlból `YYYY.MM.DD HH:MM:SS`, `YYYY.MM.DD` vagy `HH:MM:SS` formátumú értéket olvas, majd datetime értékké alakítja. |
| [FileReadDouble](FileReadDouble/FileReadDouble.md) | double értéket olvas a fájlmutató aktuális pozíciójáról. |
| [FileReadFloat](FileReadFloat/FileReadFloat.md) | float értéket olvas a fájlmutató aktuális pozíciójáról. |
| [FileReadInteger](FileReadInteger/FileReadInteger.md) | int, short vagy char értéket olvas a fájlmutató aktuális pozíciójáról. |
| [FileReadLong](FileReadLong/FileReadLong.md) | long értéket olvas a fájlmutató aktuális pozíciójáról. |
| [FileReadNumber](FileReadNumber/FileReadNumber.md) | CSV-fájlból az aktuális pozíciótól az elválasztóig vagy a sor végéig olvas egy szöveget, majd double értékké alakítja. |
| [FileReadString](FileReadString/FileReadString.md) | Karakterláncot olvas a fájlmutató aktuális pozíciójától. |
| [FileReadStruct](FileReadStruct/FileReadStruct.md) | Bináris fájlból a fájlmutató aktuális pozíciójától struktúrába olvassa az adatokat. |
| [FileSeek](FileSeek/FileSeek.md) | A fájlmutatót a megadott pozícióhoz képest, bájtban megadott mértékkel mozgatja. |
| [FileSize](FileSize/FileSize.md) | Visszaadja a megnyitott fájl méretét. |
| [FileTell](FileTell/FileTell.md) | Visszaadja a megnyitott fájlmutató aktuális pozícióját. |
| [FileWrite](FileWrite/FileWrite.md) | CSV- vagy TXT-fájlba ír adatokat. |
| [FileWriteArray](FileWriteArray/FileWriteArray.md) | String kivételével bármilyen típusú tömböt BIN fájlba ír. |
| [FileWriteDouble](FileWriteDouble/FileWriteDouble.md) | double értéket ír bináris fájlba a fájlmutató aktuális pozíciójától. |
| [FileWriteFloat](FileWriteFloat/FileWriteFloat.md) | float értéket ír bináris fájlba a fájlmutató aktuális pozíciójától. |
| [FileWriteInteger](FileWriteInteger/FileWriteInteger.md) | int értéket ír bináris fájlba a fájlmutató aktuális pozíciójától. |
| [FileWriteLong](FileWriteLong/FileWriteLong.md) | long értéket ír bináris fájlba a fájlmutató aktuális pozíciójától. |
| [FileWriteString](FileWriteString/FileWriteString.md) | A paraméterként kapott karakterláncot BIN- vagy TXT-fájlba írja a fájlmutató aktuális pozíciójától. |
| [FileWriteStruct](FileWriteStruct/FileWriteStruct.md) | A paraméterként kapott struktúra tartalmát bináris fájlba írja a fájlmutató aktuális pozíciójától. |
| [FileLoad](FileLoad/FileLoad.md) | A megadott bináris fájl minden adatát numerikus típusú vagy egyszerű struktúrákat tartalmazó tömbbe olvassa. |
| [FileSave](FileSave/FileSave.md) | A paraméterként átadott tömb minden elemét bináris fájlba írja. |
| [FolderCreate](FolderCreate/FolderCreate.md) | Mappát hoz létre a Files könyvtárban. |
| [FolderDelete](FolderDelete/FolderDelete.md) | Törli a kiválasztott könyvtárat. Nem üres mappa nem törölhető. |
| [FolderClean](FolderClean/FolderClean.md) | Törli a megadott mappában található összes fájlt. |
