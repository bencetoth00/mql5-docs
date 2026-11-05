# Levels of Elliott Wave


Elliott Waves are represented by two graphical objects of types OBJ\_ELLIOTWAVE5 and OBJ\_ELLIOTWAVE3. To set the wave size (method of wave labeling), the OBJPROP\_DEGREE property is used, to which one of values of the ENUM\_ELLIOT\_WAVE\_DEGREE enumeration can be assigned.

ENUM\_ELLIOT\_WAVE\_DEGREE

| ID | Description |
| --- | --- |
| ELLIOTT\_GRAND\_SUPERCYCLE | Grand Supercycle |
| ELLIOTT\_SUPERCYCLE | Supercycle |
| ELLIOTT\_CYCLE | Cycle |
| ELLIOTT\_PRIMARY | Primary |
| ELLIOTT\_INTERMEDIATE | Intermediate |
| ELLIOTT\_MINOR | Minor |
| ELLIOTT\_MINUTE | Minute |
| ELLIOTT\_MINUETTE | Minuette |
| ELLIOTT\_SUBMINUETTE | Subminuette |

Example:

```cpp
   for(int i=0;i<ObjectsTotal(0);i++)
     {
      string currobj=ObjectName(0,i);
      if((ObjectGetInteger(0,currobj,OBJPROP_TYPE)==OBJ_ELLIOTWAVE3) ||
         ((ObjectGetInteger(0,currobj,OBJPROP_TYPE)==OBJ_ELLIOTWAVE5)))
        {
         //--- set the marking level in INTERMEDIATE
         ObjectSetInteger(0,currobj,OBJPROP_DEGREE,ELLIOTT_INTERMEDIATE);
         //--- show lines between tops of waves
         ObjectSetInteger(0,currobj,OBJPROP_DRAWLINES,true);
         //--- set line color
         ObjectSetInteger(0,currobj,OBJPROP_COLOR,clrBlue);
         //--- set line width
         ObjectSetInteger(0,currobj,OBJPROP_WIDTH,5);
         //--- set description
         ObjectSetString(0,currobj,OBJPROP_TEXT,"test script");
        }
     }
```