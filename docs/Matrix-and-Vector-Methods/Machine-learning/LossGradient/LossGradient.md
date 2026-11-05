# LossGradient

LossGradient

Compute a vector or matrix of loss function gradients.

|  |
| --- |
| vector vector::LossGradient(    const vector&       vect\_true,     // vector of true values    ENUM\_LOSS\_FUNCTION  loss,          // loss function type     ...                               // additional parameter     );        matrix matrix::LossGradient(    const matrix&       matrix\_true,   // matrix of true values    ENUM\_LOSS\_FUNCTION  loss,          // loss function     );        matrix matrix::LossGradient(    const matrix&       matrix\_true,   // matrix of true values    ENUM\_LOSS\_FUNCTION  loss,          // loss function    ENUM\_MATRIX\_AXIS    axis,          // axis     ...                               // additional parameter     ); |

Parameters

vect\_true/matrix\_true

 [in] Vector or matrix of true values.

loss

[in]  Loss function from the [ENUM\_LOSS\_FUNCTION](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_loss_function) enumeration.

axis

[in] [ENUM\_MATRIX\_AXIS](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_matrix_axis) enumeration value (AXIS\_HORZ — horizontal axis, AXIS\_VERT — vertical axis).

...

[in]  Additional parameter 'delta' can only be used by the Hubert loss function (LOSS\_HUBER)

Return Value

Vector or matrix of loss function gradient values. The gradient is the partial derivative with respect to dx (x is the predicted value) of the loss function at a given point.

 

Note

Gradients are used in neural networks to adjust the weight matrix weights during backpropagation, when training the model.

A neural network aims at finding the algorithms that minimize the error on the training sample, for which the loss function is used.

Different loss functions are used depending on the problem. For example, Mean Squared Error ([MSE](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_loss_function)) is used for regression problems, and Binary Cross-Entropy ([BCE](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_loss_function)) is used for binary classification purposes.

 

Example of calculating loss function gradients

|  |
| --- |
| matrixf y\_true={{ 1, 2, 3, 4 },                     { 5, 6, 7, 8 },                     { 9,10,11,12 }};     matrixf y\_pred={{ 1, 2, 3, 4 },                     {11,10, 9, 8 },                     { 5, 6, 7,12 }};     matrixf loss\_gradient =y\_pred.LossGradient(y\_true,LOSS\_MAE);     matrixf loss\_gradienth=y\_pred.LossGradient(y\_true,LOSS\_MAE,AXIS\_HORZ);     matrixf loss\_gradientv=y\_pred.LossGradient(y\_true,LOSS\_MAE,AXIS\_VERT);     Print("loss gradients\n",loss\_gradient);     Print("loss gradients on horizontal axis\n",loss\_gradienth);     Print("loss gradients on vertical axis\n",loss\_gradientv);     /\* Result     loss gradients     [[0,0,0,0]      [0.083333336,0.083333336,0.083333336,0]      [-0.083333336,-0.083333336,-0.083333336,0]]     loss gradients on horizontal axis     [[0,0,0,0]      [0.33333334,0.33333334,0.33333334,0]      [-0.33333334,-0.33333334,-0.33333334,0]]     loss gradients on vertical axis     [[0,0,0,0]      [0.25,0.25,0.25,0]      [-0.25,-0.25,-0.25,0]]  \*/ |
