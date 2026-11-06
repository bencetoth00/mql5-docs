# ONNX-modellek

# ONNX a gépi tanulásban

Az [ONNX](https://onnx.ai/) (Open Neural Network Exchange) nyílt forráskódú formátum gépi tanulási modellekhez. Főbb előnyei:

- Az [ONNX-formátumot](ONNX-Support/ONNX-Support.md) olyan nagyvállalatok támogatják, mint a Microsoft és az Amazon, valamint több más partner.
- A nyílt formátum lehetővé teszi a különböző gépi tanulási eszközkészletek közötti [formátumkonverziót](Format-Conversion/Format-Conversion.md). A Microsoft [ONNXMLTools](https://learn.microsoft.com/ru-ru/windows/ai/windows-ml/onnxmltools) eszköze ONNX-formátumba is konvertál modelleket.
- Az MQL5 automatikusan [átalakítja az adattípusokat](Automatic-data-type-conversion/Automatic-data-type-conversion.md), ha a modell bemenetének vagy kimenetének típusa eltér az átadott paraméter típusától.
- [ONNX-modellek](Creating-a-Model/Creating-a-Model.md) különféle gépi tanulási eszközökkel készíthetők. Jelenleg a Caffe2, a Microsoft Cognitive Toolkit, az MXNet, a PyTorch és az OpenCV támogatja őket. Más népszerű keretrendszerekhez és könyvtárakhoz is elérhetők interfészek.
- Az MQL5-tel [ONNX-modell építhető be kereskedési stratégiába](Running-a-model/Running-a-model.md), és kihasználható a MetaTrader 5 platform pénzügyi piacokon nyújtott teljes eszköztára.
- Éles kereskedés előtt a modell viselkedése a Stratégiateszterben [múltbeli adatokon tesztelhető](Validation-in-the-Strategy-Tester/Validation-in-the-Strategy-Tester.md), külső eszközök nélkül.

Az MQL5 az alábbi függvényeket biztosítja az ONNX-modellek kezeléséhez:

| Függvény | Működés |
| --- | --- |
| [OnnxCreate](OnnxCreate/OnnxCreate.md) | ONNX-munkamenetet hoz létre egy `*.onnx` fájlból betöltött modellel. |
| [OnnxCreateFromBuffer](OnnxCreateFromBuffer/OnnxCreateFromBuffer.md) | ONNX-munkamenetet hoz létre adattömbből betöltött modellel. |
| [OnnxRelease](OnnxRelease/OnnxRelease.md) | Lezárja az ONNX-munkamenetet. |
| [OnnxRun](OnnxRun/OnnxRun.md) | Futtat egy ONNX-modellt. |
| [OnnxGetInputCount](OnnxGetInputCount/OnnxGetInputCount.md) | Visszaadja a modell bemeneteinek számát. |
| [OnnxGetOutputCount](OnnxGetOutputCount/OnnxGetOutputCount.md) | Visszaadja a modell kimeneteinek számát. |
| [OnnxGetInputName](OnnxGetInputName/OnnxGetInputName.md) | Index alapján visszaadja a modell egyik bemenetének nevét. |
| [OnnxGetOutputName](OnnxGetOutputName/OnnxGetOutputName.md) | Index alapján visszaadja a modell egyik kimenetének nevét. |
| [OnnxGetInputTypeInfo](OnnxGetInputTypeInfo/OnnxGetInputTypeInfo.md) | Lekéri a bemeneti típus leírását a modellből. |
| [OnnxGetOutputTypeInfo](OnnxGetOutputTypeInfo/OnnxGetOutputTypeInfo.md) | Lekéri a kimeneti típus leírását a modellből. |
| [OnnxSetInputShape](OnnxSetInputShape/OnnxSetInputShape.md) | Index alapján beállítja a modell bemeneti adatainak alakját. |
| [OnnxSetOutputShape](OnnxSetOutputShape/OnnxSetOutputShape.md) | Index alapján beállítja a modell kimeneti adatainak alakját. |
