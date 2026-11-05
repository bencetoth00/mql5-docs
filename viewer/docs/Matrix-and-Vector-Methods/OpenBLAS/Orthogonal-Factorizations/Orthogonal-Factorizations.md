# Orthogonal Factorizations


 

OpenBLAS предоставляет ряд процедур для разложения общей прямоугольной матрицы A размера m на n в произведение ортогональной (в комплексном случае — унитарной) и треугольной (или, возможно, трапециевидной) матриц.  

Реальная матрица Q называется ортогональной, если QT Q = I ; комплексная матрица Q называется унитарной, если QH Q = I . Ортогональные и унитарные матрицы обладают важным свойством — они сохраняют евклидову норму вектора:

||x||2 = ||Qx||2, если Q ортогональна или унитарна

Благодаря этому такие матрицы способствуют численной устойчивости, поскольку не усиливают ошибки округления.

Ортогональные разложения широко применяются при решении задач наименьших квадратов. Их также можно использовать для выполнения предварительных шагов при решении задач на собственные значения или сингулярные значения.

| Функция | Выполняемое действие |
| --- | --- |
| [FactorizationQR](FactorizationQR/FactorizationQR.md) | Вычисляет QR-разложение общей матрицы размера m на n: A = Q \* R. LAPACK-функция [GEQRF](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/geqrf.html). |
| [FactorizationQRNonNeg](FactorizationQRNonNeg/FactorizationQRNonNeg.md) | Вычисляет QR-разложение общей матрицы размера m на n: A = Q \* R, где R — верхнетреугольная матрица с неотрицательными элементами на диагонали. LATPACK-функция [GEQRFP](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/geqrfp.html). |
| [FactorizationQRPivot](FactorizationQRPivot/FactorizationQRPivot.md) | Вычисляет QR-разложение общей матрицы размера m на n с перестановкой столбцов: A \* P = Q \* R. LAPACK-функция [GEQP3](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/geqp3.html). |
| [FactorizationLQ](FactorizationLQ/FactorizationLQ.md) | Computes the LQ factorization of a general m-by-n matrix: A = L \* Q. LAPACK function [GELQF](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gelqf.html). |
| [FactorizationQL](FactorizationQL/FactorizationQL.md) | Computes the QL factorization of a general m-by-n matrix: A = Q \* L. LAPACK function [GEQLF](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/geqlf.html). |
| [FactorizationRQ](FactorizationRQ/FactorizationRQ.md) | Computes the RQ factorization of a general m-by-n matrix: A = R \* Q. LAPACK function [GERQF](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gerqf.html). |
