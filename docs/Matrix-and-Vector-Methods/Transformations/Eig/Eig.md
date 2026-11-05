# Eig

Eig

Compute the eigenvalues and right eigenvectors of a square matrix.

|  |
| --- |
| bool matrix::Eig(    matrix&  eigen\_vectors,         // matrix of eigenvectors     vector&  eigen\_values           // vector of eigenvalues      ); |

Complex solution of eigenvalues and eigenvectors

|  |
| --- |
| bool matrix::Eig(    matrix<complex>& eigen\_vectors, // matrix of eigenvectors    vector<complex>& eigen\_values   // vector of eigenvalues     ); |

Parameters

eigen\_vectors

[out]  Matrix of vertical eigenvectors.

eigen\_values

[out]  Vector of eigenvalues.

Return Value

Returns true on success, false otherwise.

Note

If a complex solution is encountered when calculating eigenvalues, the calculation is stopped and the error code is set to [4019 (ERR\_MATH\_OVERFLOW)](../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md). Use the complex overload of the Eig method to obtain a complete solution in complex space

If a complex eigenvalue has an imaginary part equal to zero, then it is a real eigenvalue. This can be seen in the example below.

Example

|  |
| --- |
| void OnStart()    {     matrix matrix\_a =       {          {-3.474589, 1.106384, -9.091977,-3.925227 },          {-5.522139, 2.366887,-15.162351,-6.357512 },          { 8.394926,-2.960067, 22.292115, 9.524129 },          { 7.803242,-2.080287, 19.217706, 8.186645 }       };        matrix eigen\_vectors;     vector eigen\_values;        bool res=matrix\_a.Eig(eigen\_vectors, eigen\_values);     Print("res=",res,"  error=",GetLastError());     Print("Eigen vectors:\n",eigen\_vectors, "\nEigen Values:\n",eigen\_values);     //--- check correctness A \* v = lambda \* v     int vectors=0;     for(ulong n=0; n<eigen\_values.Size(); n++)       {        vector eigen\_vector=eigen\_vectors.Col(n);        vector vector\_d1   =eigen\_vector\*eigen\_values[n];        vector vector\_d2   =matrix\_a.MatMul(eigen\_vector);           ulong errors=vector\_d1.Compare(vector\_d2,1e-13);        if(errors==0)           vectors++;       }     Print("vectors=",vectors);     //--- complex solution     matrix<complex> eigen\_vectors\_c;     vector<complex> eigen\_values\_c;     ResetLastError();     res=matrix\_a.Eig(eigen\_vectors\_c,eigen\_values\_c);     Print("res=",res,"  error=",GetLastError());     Print("Eigen vectors:\n",eigen\_vectors\_c, "\nEigen Values:\n",eigen\_values\_c);     //--- check correctness A \* v = lambda \* v     matrixc matrix\_c;     matrix\_c.Assign(matrix\_a);     vectors=0;     for(ulong n=0; n<eigen\_values\_c.Size(); n++)       {        vectorc eigen\_vector\_c=eigen\_vectors\_c.Col(n);        vectorc vector\_c1     =eigen\_vector\_c\*eigen\_values\_c[n];        vectorc vector\_c2     =matrix\_c.MatMul(eigen\_vector\_c);           ulong errors=vector\_c1.Compare(vector\_c2,1e-13);        if(errors==0)           vectors++;       }     Print("vectors=",vectors);    }  /\* Result     res=true  error=4019     Eigen vectors:     [[0.2649667608713664]      [0.4488818803991876]      [-0.6527335897527492]      [-0.5497604331807768]]     Eigen Values:     [28.94158645962942]     vectors=1     res=true  error=0     Eigen vectors:     [[(0.2649667608713664,0),(0.2227392219204762,0.3745470492013296),(0.403285439089771,-0.1345146135716524),(-0.2050778513598178,0)]      [(0.4488818803991876,0),(-0.2613452530342438,-0.3685707727819327),(-0.3968506126372395,0.5257002255533059),(0.8014703373356256,0)]      [(-0.6527335897527492,0),(-0.3418479634708521,-0.3299830378162041),(-0.3553021031180292,-0.03685418759727989),(-0.05618703726964112,0)]      [(-0.5497604331807768,0),(0.523227993452828,0.3262508584080381),(0.3512835596143666,0.3666300350184092),(0.558955624442244,0)]]     Eigen Values:     [(28.94158645962942,0),(0.01022501104810897,0.02954980822331488),(0.01022501104810897,-0.02954980822331488),(0.4090215182743634,0)]     vectors=3  \*/ |
