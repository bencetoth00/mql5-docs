# Static Members of a Class

# Static members of a Class/Structure

## Static Members

The members of a class can be declared using the storage class modifier [static](../../Variables/Static-Variables/Static-Variables.md). These data members are shared by all instances of this class and are stored in one place. Non-static data members are created for each class object variable.

The inability to declare static members of a class would have led to the need to declare these data on the [the global level](../../Variables/Global-Variables/Global-Variables.md) of the program. It would break the relationship between the data and their class, and is not consistent with the basic paradigm of the OOP - joining data and methods for handling them in a class. The static member allows class data that are not specific to a particular instance to exist in the class scope.

Since a static class member does not depend on the particular instance, the reference to it is as follows:

```cpp
class_name::variable
```

where class\_name is the name of the class, and variable is the name of the class member.

As you see, to access the static member of a class, [context resolution operator ::](../../Operations-and-Expressions/Other-Operations/Other-Operations.md#context_allow) is used. When you access a static member within class methods, the context operator is optional.

Static member of a class has to be explicitly initialized with desired value. For this it must be declared and initialized in global scope. The sequence of static members initialization will correspond to the sequence of their declaration in global scope.

For example, we have a class CParser used for parsing the text, and we need to count the total number of processed words and characters. We only need to declare the necessary class members as static and initialize them at the global level. Then all instances of the class will use common counters of words and characters.

```cpp
//+------------------------------------------------------------------+
//| Class "Text analyzer"                                            |
//+------------------------------------------------------------------+
class CParser
  {
public:
   static int        s_words;
   static int        s_symbols;
   //--- Constructor and destructor
                     CParser(void);
                    ~CParser(void){};
  };
...
//--- Initialization of static members of the Parser class at the global level
int CParser::s_words=0;
int CParser::s_symbols=0;
```

A static class member can be declared with the const keyword. Such static constants must be initialized at the global level with the const keyword:

```cpp
//+------------------------------------------------------------------+
//| Class "Stack" for storing processed data                         |
//+------------------------------------------------------------------+
class CStack
  {
public:
                     CStack(void);
                    ~CStack(void){};
...
private:
   static const int  s_max_length; // Maximum stack capacity
  };
//--- Initialization of the static constant of the CStack class
const int CStack::s_max_length=1000;
```

## Pointer this

The keyword [this](../../Data-Types/References-Modifier-&-and-Keyword-this/References-Modifier-&-and-Keyword-this.md) denotes an implicitly declared [pointer](../../Data-Types/Object-Pointers/Object-Pointers.md) to itself – to a specific instance of the class, in the context of which the method is executed. It can be used only in non-static methods of the class. Pointer this is an implicit non-static member of any class.

In static functions you can access only static members/methods of a class.

## Static Methods

In MQL5 member functions of type [static](../../Variables/Static-Variables/Static-Variables.md) can be used. The static modifier must precede the return type of a function in the declaration inside a class.

```cpp
class CStack
  {
public:
   //--- Constructor and destructor
                     CStack(void){};
                    ~CStack(void){};
   //--- Maximum stack capacity
   static int        Capacity();
private:
   int               m_length;     // The number of elements in the stack
   static const int  s_max_length; // Maximum stack capacity
  };
//+------------------------------------------------------------------+
//| Returns the maximum number of elements to store in the stack     |
//+------------------------------------------------------------------+
int CStack::Capacity(void)
  {
   return(s_max_length);
  }
//--- Initialization of the static constant of the CStack class
const int CStack::s_max_length=1000;
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- declare CStack type variable
   CStack stack;
//--- call the object's static method
   Print("CStack.s_max_length=",stack.Capacity());
//--- it can also be called the following way, as the method is static and does not require the presence of the object
   Print("CStack.s_max_length=",CStack::Capacity());
  }
```

A method with the const modifier is called constant and cannot modify implicit members of its class. Declaration of constant functions of a class and constant parameters is called const-correctness control. Through this control you can be sure that the compiler will ensure the consistency of values of objects and will return an error during compilation if there is something wrong.

The const modifier is placed after the list of arguments inside a class declaration. Definition outside a class should also include the const modifier:

```cpp
//+------------------------------------------------------------------+
//| Class "Rectangle"                                                |
//+------------------------------------------------------------------+
class CRectangle
  {
private:
   double            m_width;      // Width
   double            m_height;     // Height
public:
   //--- Constructors and destructor
                     CRectangle(void):m_width(0),m_height(0){};
                     CRectangle(const double w,const double h):m_width(w),m_height(h){};
                    ~CRectangle(void){};
   //--- Calculating the area
   double            Square(void) const;
   static double     Square(const double w,const double h);// { return(w*h); }
  };
//+------------------------------------------------------------------+
//| Returns the area of the "Rectangle" object                       |
//+------------------------------------------------------------------+
double CRectangle::Square(void) const
  {
   return(Square(m_width,m_height));
  }
//+------------------------------------------------------------------+
//| Returns the product of two variables                             |
//+------------------------------------------------------------------+
static double CRectangle::Square(const double w,const double h)
  {
   return(w*h);
  }
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- Create a rectangle rect with the sides equal to 5 and 6
   CRectangle rect(5,6);
//--- Find the rectangle area using a constant method
   PrintFormat("rect.Square()=%.2f",rect.Square());
//--- Find the product of numbers using the static method of class CRectangle
   PrintFormat("CRectangle::Square(2.0,1.5)=%f",CRectangle::Square(2.0,1.5));
  }
```

An additional argument in favor of using the constancy control is the fact that in this case, the compiler generates a special optimization, for example, places a constant object in read-only memory.

A static function cannot be determined with the const modifier, because this modifier ensures the constancy of the instance members when calling this function. But, as mentioned above, the static function cannot access non-static class members.

See also

[Static Variables](../../Variables/Static-Variables/Static-Variables.md), [Variables](../../Variables/Variables.md#const), [References. Modifier & and Keyword this](../../Data-Types/References-Modifier-&-and-Keyword-this/References-Modifier-&-and-Keyword-this.md)