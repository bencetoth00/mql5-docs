# Class templates

Template advantages

[Function templates](../Function-templates/Function-templates.md) are used when you need to perform similar operations on various data types, for example, searching for a maximum element in the array.  The main advantage of applying the templates is that you do not have to code a separate [overload](../Overload/Overload.md) for each type.  Instead of declaring multiple overloads of each type

|  |
| --- |
| double ArrayMax(double array[])    {     ...    }  int ArrayMax(int array[])    {     ...    }  uint ArrayMax(uint array[])    {     ...    }  long ArrayMax(long array[])    {     ...    }  datetime ArrayMax(datetime array[])    {     ...    } |

we need to write only one template function

|  |
| --- |
| template<typename T>   T ArrayMax(T array[])    {     if(ArraySize()==0)         return(0);     uint max\_index=ArrayMaximum(array);       return(array[max\_index]);    } |

to use it in your code:

|  |
| --- |
| double high[];  datetime time[];  ....  double max\_high=ArrayMax(high);  datetime lasttime=ArrayMax(time); |

Here, the T formal parameter specifying a type of used data is replaced with an actually applied type during compilation, i.e. the compiler automatically generates a separate function for each type – [double](../../Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [datetime](../../Data-Types/Integer-Types/Datetime-Type/Datetime-Type.md), etc. MQL5 also allows you to develop class templates using all the advantages of the approach.

Class templates

A class template is declared using the template keyword followed by angle brackets<> enumerating the list of formal parameters with the typename keyword. This entry informs the compiler that it deals with a generic class with the T formal parameter defining a real variable type when implementing a class. For example, let's create a vector class for storing an array with T type elements:

|  |
| --- |
| #define TOSTR(x) #x+" "   // macro for displaying an object name  //+------------------------------------------------------------------+  //| Vector class for storing T-type elements                       |  //+------------------------------------------------------------------+  template <typename T>  class TArray    {  protected:     T                 m\_array[];  public:     //--- constructor creates an array for 10 elements by default     void TArray(void){ArrayResize(m\_array,10);}     //--- constructor for creating a vector with a specified array size     void TArray(int size){ArrayResize(m\_array,size);}     //--- return a type and amount of data stored in the TArray type object     string Type(void){return(typename(m\_array[0])+":"+(string)ArraySize(m\_array));};    }; |

Next, let's apply different methods to create three TArray objects in the program for working with various types

|  |
| --- |
| void OnStart()    {     TArray<double> double\_array;   // vector has a default size of 10      TArray<int> int\_array(15);     // vector has a size of 15     TArray<string> \*string\_array;  // pointer to TArray<string> vector   //--- create a dynamic object     string\_array=new TArray<string>(20);  //--- display an object name, data type and vector size in the Journal     PrintFormat("%s (%s)",TOSTR(double\_array),double\_array.Type());     PrintFormat("%s (%s)",TOSTR(int\_array),int\_array.Type());     PrintFormat("%s (%s)",TOSTR(string\_array),string\_array.Type());  //--- remove a dynamic object before completing the program     delete(string\_array);       } |

Script execution results:

|  |
| --- |
| double\_array  (double:10)    int\_array  (int:15)    string\_array  (string:20) |

Now, we have 3 vectors with different data types: double, int and string.

Class templates are well suited for developing containers – objects designed for encapsulating other objects of any type. Container objects are collections already containing objects of one certain type. Usually, working with stored data is instantly built into the container.

For example, you can create a class template that does not allow accessing an element outside the array, thus avoiding the "out of range" [critical error](../../../MQL5-programs/Runtime-Errors/Runtime-Errors.md).

|  |
| --- |
| //+------------------------------------------------------------------+  //| Class for a free access to an array element               |  //+------------------------------------------------------------------+  template<typename T>  class TSafeArray    {  protected:     T                 m\_array[];  public:     //--- default constructor     void              TSafeArray(void){}     //--- constructor for creating the array of a specified size     void              TSafeArray(int size){ArrayResize(m\_array,size);}     //--- array size      int               Size(void){return(ArraySize(m\_array));}     //--- change the array size      int               Resize(int size,int reserve){return(ArrayResize(m\_array,size,reserve));}     //--- release the array      void              Erase(void){ZeroMemory(m\_array);}     //--- operator for accessing the array element by index     T                 operator[](int index);     //--- assignment operator for receiving all elements from the array at once     void              operator=(const T  &array[]); // T type array     };  //+------------------------------------------------------------------+  //| Receiving an element by index                           |  //+------------------------------------------------------------------+  template<typename T>  T TSafeArray::operator[](int index)    {     static T invalid\_value;  //---     int max=ArraySize(m\_array)-1;     if(index<0 || index>=ArraySize(m\_array))       {        PrintFormat("%s index %d is not in range (0-%d)!",\_\_FUNCTION\_\_,index,max);        return(invalid\_value);       }  //---     return(m\_array[index]);    }  //+------------------------------------------------------------------+  //| Assigning for the array                                 |  //+------------------------------------------------------------------+  template<typename T>  void TSafeArray::operator=(const T  &array[])    {     int size=ArraySize(array);     ArrayResize(m\_array,size);  //--- T type should support the copying operator     for(int i=0;i<size;i++)        m\_array[i]=array[i];  //---    }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     int copied,size=15;       MqlRates rates[];  //--- copy the array of quotes     if((copied=CopyRates(\_Symbol,\_Period,0,size,rates))!=size)       {        PrintFormat("CopyRates(%s,%s,0,%d) returned %d error code",        \_Symbol,EnumToString(\_Period),size,GetLastError());        return;       }  //--- create a container and insert the MqlRates value array to it     TSafeArray<MqlRates> safe\_rates;     safe\_rates=rates;     //--- index within the array     int index=3;     PrintFormat("Close[%d]=%G",index,safe\_rates[index].close);     //--- index outside the array     index=size;     PrintFormat("Close[%d]=%G",index,safe\_rates[index].close);    } |

Please note that template declaration should also be used when describing methods outside the class declaration:

|  |
| --- |
| template<typename T>  T TSafeArray::operator[](int index)    {     ...    }  template<typename T>  void TSafeArray::operator=(const T  &array[])    {     ...    } |

Class and function templates allow you to define multiple comma-separated formal parameters, for example, Map collection for storing "key – value" pairs:

|  |
| --- |
| template<typename Key, template Value>  class TMap    {     ...    } |

 

See also

[Function templates](../Function-templates/Function-templates.md), [Overload](../Overload/Overload.md)
