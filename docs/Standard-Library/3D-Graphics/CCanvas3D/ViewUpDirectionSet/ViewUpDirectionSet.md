# ViewUpDirectionSet

ViewUpDirectionSet

Sets the direction of the upper frame border in 3D space.

|  |
| --- |
| void  ViewUpDirectionSet(     const DXVector3  &up\_direction      // top direction     ); |

Parameters

&up\_direction

[in]  Direction of the upper part of the frame in 3D space.

Return Value

None.

Note

Setting a new direction using ViewUpDirectionSet() changes the view matrix obtained in [ViewMatrixGet()](../ViewMatrixGet/ViewMatrixGet.md).

ViewUpDirectionSet() is used together with [ViewTargetSet()](../ViewTargetSet/ViewTargetSet.md) to define the gaze direction.
