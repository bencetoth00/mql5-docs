# Negative binomial distribution

Negative binomial distribution

This section contains functions for working with negative binomial distribution. They allow to calculate density, probability, quantiles and to generate pseudo-random numbers distributed according to the negative binomial law. The negative binomial distribution is defined by the following formula:

![pdf_negative_binomial_distribution](../../../../assets/pdf_negative_binomial_distribution.png)

where:

- x — value of the random variable

- r — number of successful tests

- p — probability of success

![DemoNegativeBinomial](../../../../assets/demonegativebinomial.png)

In addition to the calculation of the individual random variables, the library also implements the ability to work with arrays of random variables.  

| Function | Description |
| --- | --- |
| [MathProbabilityDensityNegativeBinomial](MathProbabilityDensityNegativeBinomial/MathProbabilityDensityNegativeBinomial.md) | Calculates the probability density function of the negative binomial distribution |
| [MathCumulativeDistributionNegativeBinomial](MathCumulativeDistributionNegativeBinomial/MathCumulativeDistributionNegativeBinomial.md) | Calculates the value of the negative binomial probability distribution function |
| [MathQuantileNegativeBinomial](MathQuantileNegativeBinomial/MathQuantileNegativeBinomial.md) | Calculates the value of the inverse negative binomial distribution function for the specified probability |
| [MathRandomNegativeBinomial](MathRandomNegativeBinomial/MathRandomNegativeBinomial.md) | Generates a pseudorandom variable/array of pseudorandom variables distributed according to the negative binomial law |
| [MathMomentsNegativeBinomial](MathMomentsNegativeBinomial/MathMomentsNegativeBinomial.md) | Calculates the theoretical numerical values of the first 4 moments of the negative binomial distribution |

Example:

|  |
| --- |
| #include <Graphics\Graphic.mqh>  #include <Math\Stat\NegativeBinomial.mqh>  #include <Math\Stat\Math.mqh>  #property script\_show\_inputs  //--- input parameters  input double n\_par=40;        // the number of tests  input double p\_par=0.75;      // probability of success for each test  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- hide the price chart     ChartSetInteger(0,CHART\_SHOW,false);  //--- initialize the random number generator       MathSrand(GetTickCount());  //--- generate a sample of the random variable     long chart=0;     string name="GraphicNormal";     int n=1000000;       // the number of values in the sample     int ncells=19;       // the number of intervals in the histogram     double x[];          // centers of the histogram intervals     double y[];          // the number of values from the sample falling within the interval     double data[];       // sample of random values     double max,min;      // the maximum and minimum values in the sample  //--- obtain a sample from the negative binomial distribution     MathRandomNegativeBinomial(n\_par,p\_par,n,data);  //--- calculate the data to plot the histogram     CalculateHistogramArray(data,x,y,max,min,ncells);  //--- obtain the theoretically calculated data at the interval of [min,max]     double x2[];     double y2[];     MathSequence(0,n\_par,1,x2);     MathProbabilityDensityNegativeBinomial(x2,n\_par,p\_par,false,y2);  //--- set the scale     double theor\_max=y2[ArrayMaximum(y2)];     double sample\_max=y[ArrayMaximum(y)];     double k=sample\_max/theor\_max;     for(int i=0; i<ncells; i++)        y[i]/=k;  //--- output charts     CGraphic graphic;     if(ObjectFind(chart,name)<0)        graphic.Create(chart,name,0,0,0,780,380);     else        graphic.Attach(chart,name);     graphic.BackgroundMain(StringFormat("Negative Binomial distributionn n=%G p=%G",n\_par,p\_par));     graphic.BackgroundMainSize(16);  //--- plot all curves     graphic.CurveAdd(x,y,CURVE\_HISTOGRAM,"Sample").HistogramWidth(6);  //--- and now plot the theoretical curve of the distribution density     graphic.CurveAdd(x2,y2,CURVE\_LINES,"Theory").LinesSmooth(true);     graphic.CurvePlotAll();  //--- plot all curves     graphic.Update();    }  //+------------------------------------------------------------------+  //|  Calculate frequencies for data set                              |  //+------------------------------------------------------------------+  bool CalculateHistogramArray(const double &data[],double &intervals[],double &frequency[],                               double &maxv,double &minv,const int cells=10)    {     if(cells<=1) return (false);     int size=ArraySize(data);     if(size<cells\*10) return (false);     minv=data[ArrayMinimum(data)];     maxv=data[ArrayMaximum(data)];     double range=maxv-minv;     double width=range/cells;     if(width==0) return false;     ArrayResize(intervals,cells);     ArrayResize(frequency,cells);  //--- define the interval centers     for(int i=0; i<cells; i++)       {        intervals[i]=minv+(i+0.5)\*width;        frequency[i]=0;       }  //--- fill the frequencies of falling within the interval     for(int i=0; i<size; i++)       {        int ind=int((data[i]-minv)/width);        if(ind>=cells) ind=cells-1;        frequency[ind]++;       }     return (true);    } |
