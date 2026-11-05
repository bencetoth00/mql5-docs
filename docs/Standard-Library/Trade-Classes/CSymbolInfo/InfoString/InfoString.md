# InfoString

InfoString

Gets the value of specified string type property.

|  |
| --- |
| bool  InfoString(     ENUM\_SYMBOL\_INFO\_STRING  prop\_id,     // property ID     string&                  var          // reference to variable     ) const |

Parameters

prop\_id

[in]  ID of text property.

var

[out]  Reference to [string](../../../../Language-Basics/Data-Types/String-Type/String-Type.md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The symbol should be selected by [Name](../Name/Name.md) method.
