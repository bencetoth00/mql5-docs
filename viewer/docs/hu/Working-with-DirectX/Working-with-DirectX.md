# DirectX használata

A DirectX 11 függvényei és árnyalói 3D-s megjelenítést tesznek lehetővé közvetlenül az árdiagramon.

3D-grafikához létre kell hozni egy [grafikus környezetet](DXContextCreate/DXContextCreate.md) a szükséges képmérettel. Elő kell készíteni a vertex- és indexpuffereket ([DXBufferCreate](DXBufferCreate/DXBufferCreate.md)), valamint létre kell hozni a vertex- és pixelárnyalókat ([DXShaderCreate](DXShaderCreate/DXShaderCreate.md)). Színes grafika megjelenítéséhez ennyi elegendő.

Összetettebb grafikához az árnyalók további megjelenítési paramétereit átadó bemeneteket kell beállítani ([DXInputSet](DXInputSet/DXInputSet.md)). Így meghatározható a kamera és a 3D-objektumok pozíciója, megadhatók a fényforrások, és egérrel vagy billentyűzettel vezérelhető a megjelenítés.

A beépített MQL5-függvényekkel harmadik féltől származó eszköz nélkül készíthetők animált 3D-diagramok a MetaTrader 5-ben. A függvények használatához DX 11-et és Shader Model 5.0-t támogató videokártya szükséges.

A könyvtár használatának megkezdéséhez olvasd el a [3D-grafika készítése DirectX-szel a MetaTrader 5-ben](https://www.mql5.com/en/articles/7708) című cikket.

| Függvény | Működés |
| --- | --- |
| [DXContextCreate](DXContextCreate/DXContextCreate.md) | Grafikus környezetet hoz létre a megadott méretű képkockák megjelenítéséhez. |
| [DXContextSetSize](DXContextSetSize/DXContextSetSize.md) | Módosítja a DXContextCreate() függvénnyel létrehozott grafikus környezet képkockaméretét. |
| [DXContextSetSize](DXContextSetSize/DXContextSetSize.md) | Lekéri a DXContextCreate() függvénnyel létrehozott grafikus környezet képkockaméretét. |
| [DXContextClearColors](DXContextClearColors/DXContextClearColors.md) | A megadott színre állítja a renderpuffer összes képpontját. |
| [DXContextClearDepth](DXContextClearDepth/DXContextClearDepth.md) | Törli a mélységi puffert. |
| [DXContextGetColors](DXContextGetColors/DXContextGetColors.md) | Lekéri a grafikus környezet képének megadott méretű és eltolású részét. |
| [DXContextGetDepth](DXContextGetDepth/DXContextGetDepth.md) | Lekéri a renderelt képkocka mélységi pufferét. |
| [DXBufferCreate](DXBufferCreate/DXBufferCreate.md) | A megadott típusú puffert hoz létre adattömb alapján. |
| [DXTextureCreate](DXTextureCreate/DXTextureCreate.md) | 2D-textúrát hoz létre az átadott kép megadott méretű téglalapjából. |
| [DXInputCreate](DXInputCreate/DXInputCreate.md) | Létrehozza az árnyalóbemeneteket. |
| [DXInputSet](DXInputSet/DXInputSet.md) | Beállítja az árnyalóbemeneteket. |
| [DXShaderCreate](DXShaderCreate/DXShaderCreate.md) | A megadott típusú árnyalót hoz létre. |
| [DXShaderSetLayout](DXShaderSetLayout/DXShaderSetLayout.md) | Beállítja a vertexárnyaló vertexelrendezését. |
| [DXShaderInputsSet](DXShaderInputsSet/DXShaderInputsSet.md) | Beállítja az árnyalóbemeneteket. |
| [DXShaderTexturesSet](DXShaderTexturesSet/DXShaderTexturesSet.md) | Beállítja az árnyaló textúráit. |
| [DXDraw](DXDraw/DXDraw.md) | Rendereli a DXBufferSet() függvénnyel beállított vertexpuffer csúcsait. |
| [DXDrawIndexed](DXDrawIndexed/DXDrawIndexed.md) | A DXBufferSet() függvénnyel beállított indexpufferben leírt grafikus primitíveket rendereli. |
| [DXPrimiveTopologySet](DXPrimiveTopologySet/DXPrimiveTopologySet.md) | Beállítja a DXDrawIndexed() által renderelt primitívek típusát. |
| [DXBufferSet](DXBufferSet/DXBufferSet.md) | Beállítja az aktuális rendereléshez használt puffert. |
| [DXShaderSet](DXShaderSet/DXShaderSet.md) | Beállítja a rendereléshez használt árnyalót. |
| [DXHandleType](DXHandleType/DXHandleType.md) | Visszaadja a leíró típusát. |
| [DXRelease](DXRelease/DXRelease.md) | Felszabadít egy leírót. |
