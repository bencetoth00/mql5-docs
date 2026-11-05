# ClassificationMetric

ClassificationMetric

Compute the classification metric to evaluate the quality of the predicted data compared to the true data. The method is applied to the vector of predicted values.

|  |
| --- |
| vector vector::ClassificationMetric(     const vector&              vect\_true,     // vector of true values     ENUM\_CLASSIFICATION\_METRIC metric         // metric type     );        vector vector::ClassificationMetric(     const vector&              vect\_true,     // vector of true values     ENUM\_CLASSIFICATION\_METRIC metric         // metric type     ENUM\_AVERAGE\_MODE          mode           // averaging mode     ); |

Parameters

vect\_true

[in] Vector of true values.

metric

[in] Metric type from the [ENUM\_CLASSIFICATION\_METRIC](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_classification_metric) enumeration. Values other than CLASSIFICATION\_TOP\_K\_ACCURACY, CLASSIFICATION\_AVERAGE\_PRECISION and CLASSIFICATION\_ROC\_AUC (used in the ClassificationScore method) are applied.

mode

[in]  Averaging mode from the [ENUM\_AVERAGE\_MODE](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_average_mode) enumeration. Used for the CLASSIFICATION\_F1, CLASSIFICATION\_JACCARD, CLASSIFICATION\_PRECISION and CLASSIFICATION\_RECALL metrics.

Return Value

A vector containing the calculated metric. In the case of the AVERAGE\_NONE averaging mode, the vector contains metric values for each class without averaging. (For example, in case of the binary classification, this would be two metrics for 'false' and 'true' respectively).

 

Note about averaging modes

AVERAGE\_BINARY is only meaningful for binary classification.

AVERAGE\_MICRO — calculate metrics globally by counting the total true positives, false negatives and false positives.

AVERAGE\_MACRO — calculate metrics for each label and find their unweighted mean. This does not take label imbalance into account.

AVERAGE\_WEIGHTED — calculate metrics for each label and find their average weighted by support (the number of true instances for each label). This alters ‘macro’ to account for label imbalance; it can result in an F-score that is not between precision and recall.

Note

In case of binary classification, we can input not only an n x 2 matrix, where the first column contains probabilities for a negative label, and the second column contains probabilities for a positive label, but also a matrix consisting of one column with positive probabilities. This is because binary classification models can return either two probabilities or one probability for a positive label.

 

Example:

|  |
| --- |
| vector y\_true={7,2,1,0,4,1,4,9,5,9,0,6,9,0,1,5,9,7,3,4,8,4,2,7,6,8,4,2,3,6};     vector y\_pred={7,2,1,0,4,1,4,9,5,9,0,6,9,0,1,5,9,7,3,4,2,9,4,9,5,9,2,7,7,0};        vector accuracy=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_ACCURACY);     Print("accuracy=",accuracy);     vector balanced=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_BALANCED\_ACCURACY);     Print("balanced=",balanced);     Print("");        vector f1\_micro=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_F1,AVERAGE\_MICRO);     Print("f1\_micro=",f1\_micro);     vector f1\_macro=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_F1,AVERAGE\_MACRO);     Print("f1\_macro=",f1\_macro);     vector f1\_weighted=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_F1,AVERAGE\_WEIGHTED);     Print("f1\_weighted=",f1\_weighted);     vector f1\_none=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_F1,AVERAGE\_NONE);     Print("f1\_none=",f1\_none);     Print("");        vector jaccard\_micro=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_JACCARD,AVERAGE\_MICRO);     Print("jaccard\_micro=",jaccard\_micro);     vector jaccard\_macro=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_JACCARD,AVERAGE\_MACRO);     Print("jaccard\_macro=",jaccard\_macro);     vector jaccard\_weighted=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_JACCARD,AVERAGE\_WEIGHTED);     Print("jaccard\_weighted=",jaccard\_weighted);     vector jaccard\_none=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_JACCARD,AVERAGE\_NONE);     Print("jaccard\_none=",jaccard\_none);     Print("");        vector precision\_micro=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_PRECISION,AVERAGE\_MICRO);     Print("precision\_micro=",precision\_micro);     vector precision\_macro=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_PRECISION,AVERAGE\_MACRO);     Print("precision\_macro=",precision\_macro);     vector precision\_weighted=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_PRECISION,AVERAGE\_WEIGHTED);     Print("precision\_weighted=",precision\_weighted);     vector precision\_none=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_PRECISION,AVERAGE\_NONE);     Print("precision\_none=",precision\_none);     Print("");        vector recall\_micro=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_RECALL,AVERAGE\_MICRO);     Print("recall\_micro=",recall\_micro);     vector recall\_macro=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_RECALL,AVERAGE\_MACRO);     Print("recall\_macro=",recall\_macro);     vector recall\_weighted=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_RECALL,AVERAGE\_WEIGHTED);     Print("recall\_weighted=",recall\_weighted);     vector recall\_none=y\_pred.ClassificationMetric(y\_true,CLASSIFICATION\_RECALL,AVERAGE\_NONE);     Print("recall\_none=",recall\_none);     Print("");     //--- binary classification     vector y\_pred\_bin={0,1,0,1,1,0,0,0,1};     vector y\_true\_bin={1,0,0,0,1,0,1,1,1};        vector f1\_bin=y\_pred\_bin.ClassificationMetric(y\_true\_bin,CLASSIFICATION\_F1,AVERAGE\_BINARY);     Print("f1\_bin=",f1\_bin);     vector jaccard\_bin=y\_pred\_bin.ClassificationMetric(y\_true\_bin,CLASSIFICATION\_JACCARD,AVERAGE\_BINARY);     Print("jaccard\_bin=",jaccard\_bin);     vector precision\_bin=y\_pred\_bin.ClassificationMetric(y\_true\_bin,CLASSIFICATION\_PRECISION,AVERAGE\_BINARY);     Print("precision\_bin=",precision\_bin);     vector recall\_bin=y\_pred\_bin.ClassificationMetric(y\_true\_bin,CLASSIFICATION\_RECALL,AVERAGE\_BINARY);     Print("recall\_bin=",recall\_bin);        /\*    accuracy=[0.6666666666666666]    balanced=[0.6433333333333333]        f1\_micro=[0.6666666666666666]    f1\_macro=[0.6122510822510823]    f1\_weighted=[0.632049062049062]    f1\_none=[0.8571428571428571,1,0.3333333333333333,0.6666666666666666,0.6666666666666665,0.8,0.5,0.5714285714285715,0,0.7272727272727273]        jaccard\_micro=[0.5]    jaccard\_macro=[0.4921428571428572]    jaccard\_weighted=[0.5056349206349205]    jaccard\_none=[0.75,1,0.2,0.5,0.5,0.6666666666666666,0.3333333333333333,0.4,0,0.5714285714285714]        precision\_micro=[0.6666666666666666]    precision\_macro=[0.6571428571428571]    precision\_weighted=[0.6706349206349207]    precision\_none=[0.75,1,0.3333333333333333,1,0.75,0.6666666666666666,1,0.5,0,0.5714285714285714]        recall\_micro=[0.6666666666666666]    recall\_macro=[0.6433333333333333]    recall\_weighted=[0.6666666666666666]    recall\_none=[1,1,0.3333333333333333,0.5,0.6,1,0.3333333333333333,0.6666666666666666,0,1]        f1\_bin=[0.4444444444444445]    jaccard\_bin=[0.2857142857142857]    precision\_bin=[0.5]    recall\_bin=[0.4]  \*/ |
