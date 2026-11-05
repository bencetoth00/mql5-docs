# Enumerations

Enumeration for matrix and vector operations

This section describes the enumerations that are used in various matrix and vector methods.

 

ENUM\_AVERAGE\_MODE

Smoothing type enumeration.

| ID | Description |
| --- | --- |
| AVERAGE\_NONE | No averaging. Results are provided for each label separately |
| AVERAGE\_BINARY | Label 1 result for binary classification |
| AVERAGE\_MICRO | Average error matrix result (confusion matrix) |
| AVERAGE\_MACRO | Average result from the results of the error matrices of each label |
| AVERAGE\_WEIGHTED | Weighted average result |

 

ENUM\_VECTOR\_NORM

Enumeration of vector norms for vector::[Norm](../../Features/Norm/Norm.md).

| ID | Description |
| --- | --- |
| VECTOR\_NORM\_INF | Inf norm |
| VECTOR\_NORM\_MINUS\_INF | Minus Inf norm |
| VECTOR\_NORM\_P | Norm P |

 

ENUM\_MATRIX\_NORM

Enumeration of matrix norms for matrix::[Norm](../../Features/Norm/Norm.md) and for obtaining the matrix::[Cond](../../Features/Cond/Cond.md) matrix condition number.

| ID | Description |
| --- | --- |
| MATRIX\_NORM\_FROBENIUS | Frobenius norm |
| MATRIX\_NORM\_SPECTRAL | Spectral norm |
| MATRIX\_NORM\_NUCLEAR | Nuclear norm |
| MATRIX\_NORM\_INF | Inf norm |
| MATRIX\_NORM\_P1 | P1 norm |
| MATRIX\_NORM\_P2 | P2 norm |
| MATRIX\_NORM\_MINUS\_INF | Minus Inf norm |
| MATRIX\_NORM\_MINUS\_P1 | Minus P1 norm |
| MATRIX\_NORM\_MINUS\_P2 | Minus P2 norm |

 

ENUM\_VECTOR\_CONVOLVE

Enumeration for convolution vector::[Convolve](../../Products/Convolve/Convolve.md) and cross-correlation vector::[Correlate](../../Products/Correlate/Correlate.md).

| ID | Description |
| --- | --- |
| VECTOR\_CONVOLVE\_FULL | Convolve full |
| VECTOR\_CONVOLVE\_SAME | Convolve same |
| VECTOR\_CONVOLVE\_VALID | Convolve valid |

 

ENUM\_REGRESSION\_METRIC

Enumeration of regression metrics for vector::[RegressionMetric](../../Machine-learning/RegressionMetric/RegressionMetric.md).

| ID | Description |
| --- | --- |
| REGRESSION\_MAE | Mean Absolute Error |
| REGRESSION\_MSE | Mean Squared Error |
| REGRESSION\_RMSE | Root Mean Squared Error |
| REGRESSION\_R2 | R-Squared |
| REGRESSION\_MAPE | Mean Absolute Percentage Error |
| REGRESSION\_MSPE | Mean Squared Percentage Error |
| REGRESSION\_RMSLE | Root Mean Squared Logarithmic Error |
| REGRESSION\_SMAPE | Symmetric Mean Absolute Percentage Error |
| REGRESSION\_MAXE | Maximal Absolute Error |
| REGRESSION\_MEDE | Median Absolute Error |
| REGRESSION\_MPD | Mean Poisson Deviance |
| REGRESSION\_MGD | Mean Gamma Deviance |
| REGRESSION\_EXPV | Explained Variance |

 

ENUM\_CLASSIFICATION\_METRIC

Enumeration of metrics for classification problems.

| ID | Description |
| --- | --- |
| CLASSIFICATION\_ACCURACY | Model quality in terms of prediction accuracy for all classes |
| CLASSIFICATION\_AVERAGE\_PRECISION | Average model accuracy |
| CLASSIFICATION\_BALANCED\_ACCURACY | Balanced prediction accuracy |
| CLASSIFICATION\_F1 | F1 score. Harmonic mean between the model precision and recall |
| CLASSIFICATION\_JACCARD | Jaccard score |
| CLASSIFICATION\_PRECISION | Model accuracy in predicting true positives for the target class |
| CLASSIFICATION\_RECALL | Model completeness |
| CLASSIFICATION\_ROC\_AUC | Area under the error curve |
| CLASSIFICATION\_TOP\_K\_ACCURACY | Frequency of the correct label appearing at the top of k predicted labels |

 

ENUM\_LOSS\_FUNCTION

Enumeration for loss function calculations vector::[Loss](../../Machine-learning/Loss/Loss.md).

| ID | Description |
| --- | --- |
| LOSS\_MSE | Root mean square error |
| LOSS\_MAE | Mean Absolute Error |
| LOSS\_CCE | Categorical Crossentropy |
| LOSS\_BCE | Binary Crossentropy |
| LOSS\_MAPE | Mean Absolute Percentage Error |
| LOSS\_MSLE | Mean Squared Logarithmic Error |
| LOSS\_KLD | Kullback-Leibler Divergence |
| LOSS\_COSINE | Cosine similarity/proximity |
| LOSS\_POISSON | Poisson |
| LOSS\_HINGE | Hinge |
| LOSS\_SQ\_HINGE | Squared Hinge |
| LOSS\_CAT\_HINGE | Categorical Hinge |
| LOSS\_LOG\_COSH | Logarithm of the Hyperbolic Cosine |
| LOSS\_HUBER | Huber |

 

ENUM\_ACTIVATION\_FUNCTION

Enumeration for the activation function vector::[Activation](../../Machine-learning/Activation/Activation.md) and for the activation function derivative vector::[Derivative](../../Machine-learning/Derivative/Derivative.md).

| ID | Description |
| --- | --- |
| AF\_ELU | Exponential Linear Unit |
| AF\_EXP | Exponential |
| AF\_GELU | Gaussian Error Linear Unit |
| AF\_HARD\_SIGMOID | Hard Sigmoid |
| AF\_LINEAR | Linear |
| AF\_LRELU | Leaky Rectified Linear Unit |
| AF\_RELU | REctified Linear Unit |
| AF\_SELU | Scaled Exponential Linear Unit |
| AF\_SIGMOID | Sigmoid |
| AF\_SOFTMAX | Softmax |
| AF\_SOFTPLUS | Softplus |
| AF\_SOFTSIGN | Softsign |
| AF\_SWISH | Swish |
| AF\_TANH | The hyperbolic tangent function |
| AF\_TRELU | Thresholded Rectified Linear Unit |

 

ENUM\_SORT\_MODE

Enumeration of sort types for the [Sort](../../Manipulations/Sort/Sort.md) function.

| ID | Description |
| --- | --- |
| SORT\_ASCENDING | Sort ascending |
| SORT\_DESCENDING | Sort descending |

 

ENUM\_MATRIX\_AXIS

Enumeration for specifying the axis in all [statistical functions](../../Statistics/Statistics.md) for matrices.

| ID | Description |
| --- | --- |
| AXIS\_NONE | The axis is not specified. Calculation is performed over all matrix elements, as if it were a vector (see the [Flat](../../Manipulations/Flat/Flat.md) method). |
| AXIS\_HORZ | Horizontal axis |
| AXIS\_VERT | Vertical axis |
