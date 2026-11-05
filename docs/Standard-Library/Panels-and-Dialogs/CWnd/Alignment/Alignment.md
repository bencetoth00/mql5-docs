# Alignment

Alignment

Sets alignment parameters of the control.

|  |
| --- |
| void  Alignment(     const int  flags,      // flags     const int  left,       // offset     const int  top,        // offset     const int  right,      // offset     const int  bottom      // offset     ) |

Parameters

flags

[in]  Alignment flags.

left

[in]  Fixed offset from the left border.

top

[in]  Fixed offset from the top border.

right

[in]  Fixed offset from the right border.

bottom

[in]  Fixed offset from the bottom border.

Return Value

None.

Note

Alignement flags:

|  |
| --- |
| enum WND\_ALIGN\_FLAGS  {     WND\_ALIGN\_NONE=0,                                  // no align     WND\_ALIGN\_LEFT=1,                                  // align left     WND\_ALIGN\_TOP=2,                                   // align top     WND\_ALIGN\_RIGHT=4,                                 // align right     WND\_ALIGN\_BOTTOM=8,                                // align bottom     WND\_ALIGN\_WIDTH = WND\_ALIGN\_LEFT|WND\_ALIGN\_RIGHT,  // align width     WND\_ALIGN\_HEIGHT=WND\_ALIGN\_TOP|WND\_ALIGN\_BOTTOM,   // align height     WND\_ALIGN\_CLIENT=WND\_ALIGN\_WIDTH|WND\_ALIGN\_HEIGHT, // align height and width     } |
