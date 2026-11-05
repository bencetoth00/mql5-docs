# ScreenShot

ScreenShot

Creates a screenshot of the specified chart in its current state in .gif format.

|  |
| --- |
| bool  ScreenShot(     string           filename,                   // file name     int              width,                      // width     int              height,                     // height     ENUM\_ALIGN\_MODE  align\_mode=ALIGN\_RIGHT      // align type     ) const |

Parameters

filename

[in]  File name for screenshot.

width

[in]  Screenshot width in pixels.

height

[in]  Screenshot height in pixels.

align\_mode=ALIGN\_RIGHT

[in]  Align mode, if screenshot is narrow.

Return Value

true - successful, false - error.
