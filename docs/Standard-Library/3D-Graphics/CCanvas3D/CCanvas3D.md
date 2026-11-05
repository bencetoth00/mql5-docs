# CCanvas3D

CCanvas3D

CCanvas3D is a class for simplified creation and visualization of 3D objects on a chart.

Description

CCanvas3D greatly simplifies creation and visualization of large amounts of data in the form of animated 3D graphics. The class contains the methods for managing camera and lighting, as well as features the resource manager for creating graphic resources: textures, shaders, vertex buffers, indexes, and shader parameters.

Besides, the library contains the classes of the scene base objects, such as a box, a three-dimensional surface on user data, or an arbitrary grid.

A video card should support DX 11 and Shader Model 5.0 for the functions to work.

Declaration

|  |
| --- |
| class CCanvas |

Title

|  |
| --- |
| #include <Canvas\Canvas.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CCanvas](../../Custom-Graphics/CCanvas/CCanvas.md)        CCanvas3D |

Class methods by groups

| Creating/deleting | Description |
| --- | --- |
| [Create](Create/Create.md) | Creates a graphic resource for rendering a 3D scene without binding to a chart object. |
| [Attach](Attach/Attach.md) | Gets a graphical resource from the OBJ\_BITMAP\_LABEL object and attaches it to an instance of the CCanvas class. |
| [ObjectAdd](ObjectAdd/ObjectAdd.md) | Adds an object to a 3D scene for subsequent rendering. |
| [Destroy](Destroy/Destroy.md) | Destroys a graphic resource and releases a graphic 3D context. |
| Light |  |
| [AmbientColorSet](AmbientColorSet/AmbientColorSet.md) | Sets the color and intensity of the ambient all-round lighting. |
| [AmbientColorGet](AmbientColorGet/AmbientColorGet.md) | Gets the color and intensity of the ambient all-round lighting. |
| [LightDirectionSet](LightDirectionSet/LightDirectionSet.md) | Sets the direction of a directed light source. |
| [LightDirectionGet](LightDirectionGet/LightDirectionGet.md) | Gets the direction of a directed light source. |
| [LightColorSet](LightColorSet/LightColorSet.md) | Sets the color and intensity of a directed light source. |
| [LightColorGet](LightColorGet/LightColorGet.md) | Gets the color and intensity of a directed light source. |
| Camera |  |
| [ProjectionMatrixSet](ProjectionMatrixSet/ProjectionMatrixSet.md) | Calculates and sets a 3D coordinate projection matrix to a 2D frame. |
| [ProjectionMatrixGet](ProjectionMatrixGet/ProjectionMatrixGet.md) | Gets a 3D scene projection matrix to a 2D frame. |
| [ViewMatrixSet](ViewMatrixSet/ViewMatrixSet.md) | Sets a 3D scene view matrix. |
| [ViewMatrixGet](ViewMatrixGet/ViewMatrixGet.md) | Returns a 3D scene view matrix. |
| [ViewPositionSet](ViewPositionSet/ViewPositionSet.md) | Sets a viewpoint on a 3D scene. |
| [ViewRotationSet](ViewRotationSet/ViewRotationSet.md) | Sets the direction of a gaze at a 3D scene. |
| [ViewTargetSet](ViewTargetSet/ViewTargetSet.md) | Sets the coordinates of the point a gaze is directed at. |
| [ViewUpDirectionSet](ViewUpDirectionSet/ViewUpDirectionSet.md) | Sets the direction of the upper frame border in 3D space. |
| Rendering |  |
| [Render](Render/Render.md) | Renders all scene objects in the frame inner buffer for subsequent display. |
| [RenderBegin](RenderBegin/RenderBegin.md) | Prepares a graphic context for rendering a new frame. |
| [RenderEnd](RenderEnd/RenderEnd.md) | Copies a rendered frame to the inner buffer and updates a chart image if necessary. |
| Getting resources |  |
| [DXContext](DXContext/DXContext.md) | Gets the graphic context handle. |
| [DXDispatcher](DXDispatcher/DXDispatcher.md) | Gets the resource dispatcher handle. |
| [InputScene](InputScene/InputScene.md) | Gets the pointer to the buffer of scene parameters. |
