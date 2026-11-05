# ViewTargetSet

ViewTargetSet

Sets the coordinates of the point a gaze is directed at.

|  |
| --- |
| void  ViewTargetSet(     const DXVector3  &target      // target coordinates     ); |

Parameters

&target

[in]  Coordinates of the point a gaze is directed at.

Return Value

None.

Note

Used to fix the gaze at one scene point when moving the viewpoint.

Setting a new target coordinate using ViewRotationSet() changes the view matrix obtained in [ViewMatrixGet()](../ViewMatrixGet/ViewMatrixGet.md).

ViewTargetSet() is used together with [ViewUpDirectionSet()](../ViewUpDirectionSet/ViewUpDirectionSet.md) to define the gaze direction.
