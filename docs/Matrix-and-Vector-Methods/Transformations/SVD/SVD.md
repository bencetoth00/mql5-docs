# SVD

SVD

Singular Value Decomposition.

|  |
| --- |
| bool matrix::SVD(    matrix&  U,                   // unitary matrix     matrix&  V,                   // unitary matrix     vector&  singular\_values      // singular values vector     ); |

Parameters

U

 [out] Unitary matrix of order m, consisting of left singular vectors.

V

[out] Unitary matrix of order n, consisting of right singular vectors.

singular\_values

[out] Singular values

Return Value

Returns true on success, false otherwise.

 

Example

|  |
| --- |
| matrix a= {{0, 1, 2, 3, 4, 5, 6, 7, 8}};    a=a-4;    Print("matrix a \n", a);    a.Reshape(3, 3);    matrix b=a;    Print("matrix b \n", b);  //--- execute SVD decomposition    matrix U, V;    vector singular\_values;    b.SVD(U, V, singular\_values);    Print("U \n", U);    Print("V \n", V);    Print("singular\_values = ", singular\_values);     // check block  //--- U \* singular diagonal \* V = A    matrix matrix\_s;    matrix\_s.Diag(singular\_values);    Print("matrix\_s \n", matrix\_s);    matrix matrix\_vt=V.Transpose();    Print("matrix\_vt \n", matrix\_vt);    matrix matrix\_usvt=(U.MatMul(matrix\_s)).MatMul(matrix\_vt);    Print("matrix\_usvt \n", matrix\_usvt);       ulong errors=(int)b.Compare(matrix\_usvt, 1e-9);    double res=(errors==0);    Print("errors=", errors);     //---- another check    matrix U\_Ut=U.MatMul(U.Transpose());    Print("U\_Ut \n", U\_Ut);    Print("Ut\_U \n", (U.Transpose()).MatMul(U));       matrix vt\_V=matrix\_vt.MatMul(V);    Print("vt\_V \n", vt\_V);    Print("V\_vt \n", V.MatMul(matrix\_vt));       /\*    matrix a    [[-4,-3,-2,-1,0,1,2,3,4]]    matrix b    [[-4,-3,-2]     [-1,0,1]     [2,3,4]]    U    [[-0.7071067811865474,0.5773502691896254,0.408248290463863]     [-6.827109697437648e-17,0.5773502691896253,-0.8164965809277256]     [0.7071067811865472,0.5773502691896255,0.4082482904638627]]    V    [[0.5773502691896258,-0.7071067811865474,-0.408248290463863]     [0.5773502691896258,1.779939029415334e-16,0.8164965809277258]     [0.5773502691896256,0.7071067811865474,-0.408248290463863]]    singular\_values = [7.348469228349533,2.449489742783175,3.277709923350408e-17]       matrix\_s    [[7.348469228349533,0,0]     [0,2.449489742783175,0]     [0,0,3.277709923350408e-17]]    matrix\_vt    [[0.5773502691896258,0.5773502691896258,0.5773502691896256]     [-0.7071067811865474,1.779939029415334e-16,0.7071067811865474]     [-0.408248290463863,0.8164965809277258,-0.408248290463863]]    matrix\_usvt    [[-3.999999999999997,-2.999999999999999,-2]     [-0.9999999999999981,-5.977974170712231e-17,0.9999999999999974]     [2,2.999999999999999,3.999999999999996]]    errors=0       U\_Ut    [[0.9999999999999993,-1.665334536937735e-16,-1.665334536937735e-16]     [-1.665334536937735e-16,0.9999999999999987,-5.551115123125783e-17]     [-1.665334536937735e-16,-5.551115123125783e-17,0.999999999999999]]    Ut\_U    [[0.9999999999999993,-5.551115123125783e-17,-1.110223024625157e-16]     [-5.551115123125783e-17,0.9999999999999987,2.498001805406602e-16]     [-1.110223024625157e-16,2.498001805406602e-16,0.999999999999999]]    vt\_V    [[1,-5.551115123125783e-17,0]     [-5.551115123125783e-17,0.9999999999999996,1.110223024625157e-16]     [0,1.110223024625157e-16,0.9999999999999996]]    V\_vt    [[0.9999999999999999,1.110223024625157e-16,1.942890293094024e-16]     [1.110223024625157e-16,0.9999999999999998,1.665334536937735e-16]     [1.942890293094024e-16,1.665334536937735e-16,0.9999999999999996]    \*/   } |
