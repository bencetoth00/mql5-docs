# ProjectionMatrixSet

ProjectionMatrixSet

Calculates and sets a 3D coordinate projection matrix to a 2D frame.

|  |
| --- |
| void  ProjectionMatrixSet(     float  fov,              // field of view     float  aspect\_ratio,     // frame aspect ratio     float  z\_near,           //      float  z\_far             //      ); |

Parameters

fov

[in]  Field of view width in radians to create a scene projection.

aspect\_ratio

[in]  2D frame aspect ratio.

z\_near

[in]  Distance to the near clipping plane.

z\_far

[in]  Distance to the far clipping plane.

Return Value

None.

Note

2D frame displays only projections of 3D objects falling into the specified field of view and located between the near and far clipping planes.
