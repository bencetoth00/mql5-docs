# Object Create Operator new


The new operator automatically creates an object of a corresponding size, calls the object constructor and returns [a descriptor of created object](../../Data-Types/Object-Pointers/Object-Pointers.md). In case of failure, the operator returns a null descriptor that can be compared with the [NULL](../../Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) constant.

The new operator can be applied only to [class](../../Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md) objects. It can't be applied to structures.

The operator shall not be used to create arrays of objects. To do this, use the [ArrayResize()](../../../Array-Functions/ArrayResize/ArrayResize.md) function.

Example:

```cpp
//+------------------------------------------------------------------+
//| Figure creation                                                  |
//+------------------------------------------------------------------+
void CTetrisField::NewShape()
  {
   m_ypos=HORZ_BORDER;
//--- randomly create one of the 7 possible shapes
   int nshape=rand()%7;
   switch(nshape)
     {
      case 0: m_shape=new CTetrisShape1; break;
      case 1: m_shape=new CTetrisShape2; break;
      case 2: m_shape=new CTetrisShape3; break;
      case 3: m_shape=new CTetrisShape4; break;
      case 4: m_shape=new CTetrisShape5; break;
      case 5: m_shape=new CTetrisShape6; break;
      case 6: m_shape=new CTetrisShape7; break;
     }
//--- draw
   if(m_shape!=NULL)
     {
      //--- pre-settings
      m_shape.SetRightBorder(WIDTH_IN_PIXELS+VERT_BORDER);
      m_shape.SetYPos(m_ypos);
      m_shape.SetXPos(VERT_BORDER+SHAPE_SIZE*8);
      //--- draw
      m_shape.Draw();
     }
//---
  }
```

It should be noted that object descriptor is not a pointer to memory address.

An object created with the new operator must be explicitly removed using the [delete](../Object-Delete-Operator-delete/Object-Delete-Operator-delete.md) operator.

See also

[Initialization of Variables](../../Variables/Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)