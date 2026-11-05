# FrameInputs


Receives [input parameters](../../Language-Basics/Variables/Input-Variables/Input-Variables.md), on which the frame with the specified pass number is formed.

```cpp
bool  FrameInputs(
   ulong    pass,                // The number of a pass in the optimization
   string&  parameters[],        // An array of strings of form "parameterN=valueN"
   uint&    parameters_count     // The total number of parameters
   );
```

Parameters

pass

[in]  The number of a pass during optimization in the strategy tester.

parameters

[out]  A string array with the description of names and parameter values

parameters\_count

[out]  The number of elements in the array parameters[].

Return Value

Returns true if successful, otherwise false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

Having obtained the number of strings parameters\_count in the parameters[] array, you can organize a loop to go through all records. This will help you find the values of input parameters of an Expert Advisor for the specified pass number.