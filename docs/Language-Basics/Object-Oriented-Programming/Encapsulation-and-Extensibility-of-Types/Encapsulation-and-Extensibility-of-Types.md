# Encapsulation and Extensibility of Types

Encapsulation and Extensibility of Types

OOP is a balanced approach to writing software. Data and behavior are packed together. This encapsulation creates user-defined data types, extending the language data types and interacting with them. Types extensibility is an opportunity to add to the language user-defined data types, which are also easy to use, as well as [basic types](../../Data-Types/Data-Types.md#base_types).

An abstract data type, for example, a string, is a description of the ideal, well known behavior type.

The string user knows that the string operations, such as concatenation or print, have a certain behavior. Concatenation and print operations are called methods.

A certain implementation of ADT may have some restrictions, for example, strings can be limited in length. These limitations affect the behavior opened to all. At the same time, internal or private implementation details do not affect directly the way the user sees the object. For example, the string is often implemented as an array, while the internal base address of this array and its name are not essential for the user.

Encapsulation is the ability to hide the implementation details when the open interfaces to user-defined type is provided. In MQL5, as well as in C++, class and structure definitions ([class](../../Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#class) and [struct](../../Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md)) are used for the encapsulation provisions in combination with access keywords private, protected and public.

The public keyword shows that access to the members that stand behind it is open without restrictions. Without this keyword, class members are locked by default. Private members are accessible only by member functions only of its class.

Protected class functions are available to class functions not only in its class, but also in its inheritor classes. Public class functions are available for any function within the scope of the class declaration. The protection makes possible to hide part of the class implementation, thus preventing unexpected changes in the structure of data. Access restriction or data hiding is a feature of the object-oriented programming.

Usually, class functions are protected and declared with the protected modifier, the reading and writing of the values are performed by using special so-called set-and get-methods that are defined by the public access modifier.

 

Example:

|  |
| --- |
| class CPerson    {  protected:     string            m\_name;                     // name  public:     void              SetName(string n){m\_name=n;}// sets name     string            GetName(){return (m\_name);} // returns name    }; |

 

This approach offers several advantages. First, by function name we can understand what it does - sets or gets the value of a class member. Secondly, perhaps in the future we will need to change the type of the m\_name variable in the CPerson class or in any of its derivative classes.

In this case, we'll need just to change the implementation of functions SetName() and GetName(), while objects of the CPerson class will be available for using in a program without any code changes because the user will not even know that the data type of m\_name has changed.

Example:

|  |
| --- |
| struct Name    {     string            first\_name;                 // name     string            last\_name;                  // last name    };     class CPerson    {  protected:     Name              m\_name;                     // name  public:     void              SetName(string n);     string            GetName(){return(m\_name.first\_name+" "+m\_name.last\_name);}  private:     string            GetFirstName(string full\_name);     string            GetLastName(string full\_name);    };     void CPerson::SetName(string n)    {     m\_name.first\_name=GetFirstName(n);     m\_name.last\_name=GetLastName(n);    }     string CPerson::GetFirstName(string full\_name)    {     int pos=StringFind(full\_name," ");     if(pos>0) StringSetCharacter(full\_name,pos,0);     return(full\_name);    }     string CPerson::GetLastName(string full\_name)    {     string ret\_string;     int pos=StringFind(full\_name," ");     if(pos>0) ret\_string=StringSubstr(full\_name,pos+1);     else      ret\_string=full\_name;     return(ret\_string);    } |

See also

[Data Types](../../Data-Types/Data-Types.md)
