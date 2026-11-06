# Előre definiált változók

# Az előre definiált változók

Minden végrehajtható MQL5-program használhat előre definiált változókat, amelyek a program — Expert Advisor, szkript vagy egyéni indikátor — indulásakor tükrözik az aktuális árdiagram állapotát.

A változók értékét a program indulása előtt az ügyfélterminál állítja be. Ezek konstansok, ezért az MQL5-programból nem módosíthatók. Kivétel a speciális `_LastError` változó, amelynek értékét a [ResetLastError](../Common-Functions/ResetLastError/ResetLastError.md) függvénnyel 0-ra lehet állítani.

| Változó | Érték |
| --- | --- |
| [\_AppliedTo](_AppliedTo/_AppliedTo.md) | Megadja, milyen adatok alapján történik az indikátor számítása. |
| [\_Digits](_Digits/_Digits.md) | A tizedesjegyek száma. |
| [\_Point](_Point/_Point.md) | Az aktuális szimbólum pontértéke a jegyzési devizában. |
| [\_LastError](_LastError/_LastError.md) | Az utolsó hibakód. |
| [\_Period](_Period/_Period.md) | Az aktuális diagram időkerete. |
| [\_RandomSeed](_RandomSeed/_RandomSeed.md) | Az ál-véletlenszám-generátor aktuális állapota. |
| [\_StopFlag](_StopFlag/_StopFlag.md) | A program leállítási jelzője. |
| [\_Symbol](_Symbol/_Symbol.md) | Az aktuális diagram szimbólumának neve. |
| [\_UninitReason](_UninitReason/_UninitReason.md) | Az inicializálás megszüntetésének oka. |
| [\_IsX64](_IsX64/_IsX64.md) | Megadja, hogy milyen bitverziójú terminálban fut az MQL5-alkalmazás. |

Könyvtárban nem definiálhatók előre definiált változók. A könyvtár azt a programban definiált változót használja, amelyből meghívták.
