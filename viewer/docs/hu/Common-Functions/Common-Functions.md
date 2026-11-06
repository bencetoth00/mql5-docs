# Általános függvények

Az itt felsorolt általános célú függvények nem tartoznak egyik speciális függvénycsoportba sem.

| Függvény | Működés |
| --- | --- |
| [Alert](Alert/Alert.md) | Üzenetet jelenít meg külön ablakban. |
| [CheckPointer](CheckPointer/CheckPointer.md) | Visszaadja az objektummutató típusát. |
| [Comment](Comment/Comment.md) | Megjegyzést jelenít meg a diagram bal felső sarkában. |
| [CryptEncode](CryptEncode/CryptEncode.md) | A megadott módszerrel átalakítja a tömb adatait. |
| [CryptDecode](CryptDecode/CryptDecode.md) | Visszaállítja a tömb adatainak eredeti formáját. |
| [DebugBreak](DebugBreak/DebugBreak.md) | Töréspontot helyez el a programban hibakereséshez. |
| [ExpertRemove](ExpertRemove/ExpertRemove.md) | Leállítja az Expert Advisort, és eltávolítja a diagramról. |
| [GetPointer](GetPointer/GetPointer.md) | Visszaadja az objektum [mutatóját](../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md). |
| [GetTickCount](GetTickCount/GetTickCount.md) | Visszaadja a rendszerindítás óta eltelt ezredmásodpercek számát. |
| [GetTickCount64](GetTickCount64/GetTickCount64.md) | Visszaadja a rendszerindítás óta eltelt ezredmásodpercek számát 64 bites értékként. |
| [GetMicrosecondCount](GetMicrosecondCount/GetMicrosecondCount.md) | Visszaadja az MQL5-program indulása óta eltelt mikroszekundumok számát. |
| [MessageBox](MessageBox/MessageBox.md) | Üzenetablakot hoz létre, jelenít meg és kezel. |
| [PeriodSeconds](PeriodSeconds/PeriodSeconds.md) | Visszaadja az időszak hosszát másodpercben. |
| [PlaySound](PlaySound/PlaySound.md) | Lejátszik egy hangfájlt. |
| [Print](Print/Print.md) | Üzenetet ír a naplóba. |
| [PrintFormat](PrintFormat/PrintFormat.md) | A megadott formátum szerint formázza és naplófájlba írja a szövegeket és értékeket. |
| [ResetLastError](ResetLastError/ResetLastError.md) | A [\_LastError](../Predefined-Variables/_LastError/_LastError.md) előre definiált változót 0-ra állítja. |
| [ResourceCreate](ResourceCreate/ResourceCreate.md) | Képerőforrást hoz létre adatkészletből. |
| [ResourceFree](ResourceFree/ResourceFree.md) | Törli a [dinamikusan létrehozott erőforrást](ResourceCreate/ResourceCreate.md#dynamic_resourcecreate), és felszabadítja a memóriáját. |
| [ResourceReadImage](ResourceReadImage/ResourceReadImage.md) | Beolvassa a [ResourceCreate() függvénnyel létrehozott](ResourceCreate/ResourceCreate.md#dynamic_resourcecreate), vagy fordításkor az EX5 fájlba [mentett](../MQL5-programs/Resources/Resources.md#resource_include) grafikus erőforrás adatait. |
| [ResourceSave](ResourceSave/ResourceSave.md) | Erőforrást ment a megadott fájlba. |
| [SetUserError](SetUserError/SetUserError.md) | Az `_LastError` értékét az `ERR_USER_ERROR_FIRST + user_error` kifejezés eredményére állítja. |
| [SetReturnError](SetReturnError/SetReturnError.md) | Beállítja azt a kódot, amelyet a terminálfolyamat a művelet befejezésekor visszaad. |
| [Sleep](Sleep/Sleep.md) | A megadott időre felfüggeszti az aktuális Expert Advisor vagy szkript végrehajtását. |
| [TerminalClose](TerminalClose/TerminalClose.md) | Leállítási utasítást küld a terminálnak. |
| [TesterHideIndicators](TesterHideIndicators/TesterHideIndicators.md) | Beállítja, hogy a tesztelő elrejtse vagy megjelenítse az EA által használt indikátorokat. |
| [TesterStatistics](TesterStatistics/TesterStatistics.md) | Visszaadja a teszteredményekből számított megadott statisztikai értéket. |
| [TesterStop](TesterStop/TesterStop.md) | A tesztelés során leállítási utasítást ad a programnak. |
| [TesterDeposit](TesterDeposit/TesterDeposit.md) | Befizetést szimulál a teszt során; egyes pénzkezelő rendszereknél használható. |
| [TesterWithdrawal](TesterWithdrawal/TesterWithdrawal.md) | Pénzfelvételt szimulál a teszt során. |
| [TranslateKey](TranslateKey/TranslateKey.md) | Virtuális billentyűkód alapján Unicode-karaktert ad vissza. |
| [ZeroMemory](ZeroMemory/ZeroMemory.md) | Nullázza a referenciaként átadott változót. Bármilyen típusú lehet, kivéve a konstruktorral rendelkező osztályokat és struktúrákat. |
