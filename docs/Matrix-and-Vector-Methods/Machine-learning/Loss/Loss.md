# Loss

Loss

Compute the value of the loss function.

|  |
| --- |
| double vector::Loss(    const vector&       vect\_true,     // vector of true values    ENUM\_LOSS\_FUNCTION  loss,          // loss function     ...                               // additional parameter     );        double matrix::Loss(    const matrix&       matrix\_true,   // matrix of true values    ENUM\_LOSS\_FUNCTION  loss,          // loss function     );        double matrix::Loss(    const matrix&       matrix\_true,   // matrix of true values    ENUM\_LOSS\_FUNCTION  loss,          // loss function    ENUM\_MATRIX\_AXIS    axis,          // axis     ...                               // additional parameter     ); |

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

double value.

 

How the 'delta' parameter is used in the Hubert loss function (LOSS\_HUBER)

|  |
| --- |
| double delta = 1.0;     double error = fabs(y - x);     if(error<delta)        loss = 0.5 \* error^2;     else        loss = 0.5 \* delta^2 + delta \* (error - delta); |

 

Note

A neural network aims at finding the algorithms that minimize the error on the training sample, for which the loss function is used.

The value of the loss function indicates by how much the value predicted by the model deviates from the real one.

Different loss functions are used depending on the problem. For example, Mean Squared Error ([MSE](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_loss_function)) is used for regression problems, and Binary Cross-Entropy ([BCE](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_loss_function)) is used for binary classification purposes.

 

Example of calling the Hubert loss function:

|  |
| --- |
| vector y\_true = {0.0, 1.0, 0.0, 0.0};     vector y\_pred = {0.6, 0.4, 0.4, 0.6};     double loss=y\_pred.Loss(y\_true,LOSS\_HUBER);     Print(loss);     double loss2=y\_pred.Loss(y\_true,LOSS\_HUBER,0.5);     Print(loss2);     /\* Result     0.155     0.15125  \*/ |
