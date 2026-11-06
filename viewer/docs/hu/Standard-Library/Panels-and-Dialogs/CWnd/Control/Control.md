# Control


Index alapján lekéri a vezérlőt a konténerből.

```cpp
CWnd*  Control(
   const int  ind      // index
   )  const
```

Paraméterek

ind

[in]  A vezérlő indexe.

Visszatérési érték

A vezérlőre mutató pointer.

Megjegyzés

Az alaposztályhoz nem tartozik konténer; leszármazottai számára hozzáférést biztosít a konténerhez, és mindig NULL értéket ad vissza.
