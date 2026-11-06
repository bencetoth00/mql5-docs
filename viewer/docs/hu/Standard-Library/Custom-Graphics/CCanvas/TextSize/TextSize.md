# TextSize


Lekéri a szöveg méretét.

```cpp
void  TextSize(
   const string  text,       // text
   int&          width,      // width
   int&          height      // height
   );
```

Paraméterek

text

[in]  A mérendő szöveg.

width

[out]  Hivatkozás arra a változóra, amelybe a szöveg szélessége kerül.

height

[out]  Hivatkozás arra a változóra, amelybe a szöveg magassága kerül.

Megjegyzés

A szöveg méréséhez az aktuális betűtípust használja.
