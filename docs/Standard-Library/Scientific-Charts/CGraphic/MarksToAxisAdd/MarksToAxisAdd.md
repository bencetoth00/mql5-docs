# MarksToAxisAdd

MarksToAxisAdd

Add a scale mark (ticks) to the specified chart axis.

|  |
| --- |
| bool  MarksToAxisAdd(     const double        &marks[],        // tick coordinates     const int           mark\_size,       // tick size     ENUM\_MARK\_POSITION  position,        // tick location     const int           dimension=0      // dimension     ) |

Parameters

&marks[]

[in]  Tick coordinates

mark\_size

[in]  Tick size

position

[in]  Tick location

dimension=0

[in]  0 — adding to X axis,

       1 — adding to Y axis

Return Value

true - successful, otherwise - false.
