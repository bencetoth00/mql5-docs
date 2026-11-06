# OnChangeItem


A vezérlő „ChangeItem” (elemváltozás) belső eseményének virtuális kezelője.

```cpp
virtual bool  OnChangeItem(
   const int  index      // index
   )
```

Paraméterek

index

[in]  A megváltozott elem indexe.

Visszatérési érték

true – az esemény feldolgozva, egyébként false.
