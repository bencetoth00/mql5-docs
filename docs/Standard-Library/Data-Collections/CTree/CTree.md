# CTree

CTree

CTree is a class of the binary tree of the instances of CTreeNode class and its descendants.

Description

CTree class provides the possibility to work with the binary tree of [CTreeNode](../CTreeNode/CTreeNode.md) class instances and its descendants. Options of adding/inserting/deleting of tree elements and search in the tree are implemented in the class. Besides that, methods of working with a file are implemented.

Note that mechanism of dynamic memory management is not implemented in class CTree (unlike classes [CList](../CList/CList.md) and [CArrayObj](../CArrayObj/CArrayObj.md)). All tree nodes are deleted with memory deallocation.

Declaration

|  |
| --- |
| class CTree : public CTreeNode |

Title

|  |
| --- |
| #include <Arrays\Tree.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CTreeNode](../CTreeNode/CTreeNode.md)            CTree |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Root](Root/Root.md) | Gets the root node of the tree |
| Creation of a new element |  |
| [CreateElement](CreateElement/CreateElement.md) | Creates a new instance of the node |
| Filling |  |
| [Insert](Insert/Insert.md) | Adds a node to a tree |
| Deletion |  |
| [Detach](Detach/Detach.md) | Detaches a specified node from a tree |
| [Delete](Delete/Delete.md) | Deletes a specified node from a tree |
| [Clear](Clear/Clear.md) | Deletes all nodes of a tree |
| Search |  |
| [Find](Find/Find.md) | Searches for a node in a tree by sample |
| Input/output |  |
| virtual [Save](Save/Save.md) | Saves all the tree data to a file |
| virtual [Load](Load/Load.md) | Downloads tree data from a file |
| virtual [Type](Type/Type.md) | Gets identifier of the tree type |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CTreeNode  Parent, Parent, [Left](../CTreeNode/Left/Left.md), [Left](../CTreeNode/Left/Left.md), [Right](../CTreeNode/Right/Right.md), [Right](../CTreeNode/Right/Right.md), [Balance](../CTreeNode/Balance/Balance.md), [BalanceL](../CTreeNode/BalanceL/BalanceL.md), [BalanceR](../CTreeNode/BalanceR/BalanceR.md), [RefreshBalance](../CTreeNode/RefreshBalance/RefreshBalance.md), [GetNext](../CTreeNode/GetNext/GetNext.md), [SaveNode](../CTreeNode/SaveNode/SaveNode.md), [LoadNode](../CTreeNode/LoadNode/LoadNode.md) |

Trees of CTreeNode class descendants – descendants of class CTree - have practical application.

Descendant of CTree class should have a predefined method [CreateElement](CreateElement/CreateElement.md) that creates a new instance of the [CTreeNode](../CTreeNode/CTreeNode.md) descendant class.

Let's consider an example of the CTree descendant class.

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                                       MyTree.mq5 |  //|                        Copyright 2010, MetaQuotes Software Corp. |  //|                                       https://www.metaquotes.net/ |  //+------------------------------------------------------------------+  #property copyright "2010, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  //---  #include <Arrays\Tree.mqh>  #include "MyTreeNode.mqh"  //---  input int extCountedNodes = 100;  //+------------------------------------------------------------------+  //| Describe class CMyTree derived from CTree.                       |  //+------------------------------------------------------------------+  //| Class CMyTree.                                                   |  //| Purpose: Construction and navigation of a binary search tree.    |  //+------------------------------------------------------------------+  class CMyTree : public CTree    {  public:     //--- methods of searching in the tree by custom data     CMyTreeNode\*        FindByLong(long find\_long);     //--- method of creation of the tree element     virtual CTreeNode \*CreateElement();    };  //---  CMyTree MyTree;  //+------------------------------------------------------------------+  //| Creation of a new tree node.                                     |  //| INPUT:  none.                                                    |  //| OUTPUT: pointer to the new tree node if OK, or NULL.             |  //| REMARK: none.                                                    |  //+------------------------------------------------------------------+  CTreeNode \*CMyTree::CreateElement()    {     CMyTreeNode \*node=new CMyTreeNode;  //---     return(node);    }  //+------------------------------------------------------------------+  //| Search of element in a list by value m\_long.                     |  //| INPUT:  find\_long - searched value.                              |  //| OUTPUT: pointer of a found list element, or NULL.                |  //| REMARK: none.                                                    |  //+------------------------------------------------------------------+  CMyTreeNode\* CMyTree::FindByLong(long find\_long)    {     CMyTreeNode \*res=NULL;     CMyTreeNode \*node;  //--- create a tree node to pass the search parameter     node=new CMyTreeNode;     if(node==NULL) return(NULL);     node.SetLong(find\_long);  //---     res=Find(node);     delete node;  //---     return(res);    }  //+------------------------------------------------------------------+  //| script "testing of class CMyTree"                                |  //+------------------------------------------------------------------+  //---  array for string initialization  string str\_array[11]={"p","oo","iii","uuuu","yyyyy","ttttt","rrrr","eee","ww","q","999"};  //---  int OnStart() export    {     int          i;     uint         pos;     int          beg\_time,end\_time;     CMyTreeNode \*node; //--- temporary pointer to the sample of class CMyTreeNode   //---       printf("Start test %s.",\_\_FILE\_\_);  //--- Fill out MyTree with instances of class MyTreeNode in the amount of extCountedNodes.     beg\_time=GetTickCount();     for(i=0;i<extCountedNodes;i++)       {        node=MyTree.CreateElement();        if(node==NULL)          {           //--- emergency exit           printf("%s (%4d): create error",\_\_FILE\_\_,\_\_LINE\_\_);           return(\_\_LINE\_\_);          }        NodeSetData(node,i);        node.SetLong(i);        MyTree.Insert(node);       }     end\_time=GetTickCount();     printf("Filling time of MyTree is %d ms.",end\_time-beg\_time);  //--- Create a temporary tree TmpMyTree.     CMyTree TmpMyTree;  //--- Detach 50% of tree elements (all even)  //--- and add them to the temporary tree TmpMyTree.     beg\_time=GetTickCount();     for(i=0;i<extCountedNodes;i+=2)       {        node=MyTree.FindByLong(i);        if(node!=NULL)           if(MyTree.Detach(node)) TmpMyTree.Insert(node);       }     end\_time=GetTickCount();     printf("Deletion time of %d elements from MyTree is %d ms.",extCountedNodes/2,end\_time-beg\_time);  //--- Return the detached     node=TmpMyTree.Root();     while(node!=NULL)       {        if(TmpMyTree.Detach(node)) MyTree.Insert(node);        node=TmpMyTree.Root();       }  //--- Check work of method Save(int file\_handle);     int file\_handle;     file\_handle=FileOpen("MyTree.bin",FILE\_WRITE|FILE\_BIN|FILE\_ANSI);     if(file\_handle>=0)       {        if(!MyTree.Save(file\_handle))          {           //--- error writing to a file           //--- emergency exit           printf("%s: Error %d in %d!",\_\_FILE\_\_,GetLastError(),\_\_LINE\_\_);           //--- close file before leaving!!!           FileClose(file\_handle);           return(\_\_LINE\_\_);          }        FileClose(file\_handle);       }  //--- Check work of method Load(int file\_handle);     file\_handle=FileOpen("MyTree.bin",FILE\_READ|FILE\_BIN|FILE\_ANSI);     if(file\_handle>=0)       {        if(!TmpMyTree.Load(file\_handle))          {           //--- error reading from file           //--- emergency exit           printf("%s: Error %d in %d!",\_\_FILE\_\_,GetLastError(),\_\_LINE\_\_);           //--- close file before leaving!!!           FileClose(file\_handle);           return(\_\_LINE\_\_);          }        FileClose(file\_handle);       }  //---     MyTree.Clear();     TmpMyTree.Clear();  //---     printf("End test %s. OK!",\_\_FILE\_\_);  //---     return(0);    }  //+------------------------------------------------------------------+  //| Function to output node contents to journal                      |   //+------------------------------------------------------------------+  void NodeToLog(CMyTreeNode \*node)    {     printf("   %I64d,%f,'%s','%s'",                 node.GetLong(),node.GetDouble(),                 node.GetString(),TimeToString(node.GetDateTime()));    }  //+------------------------------------------------------------------+  //| Function to populate node with random values                     |   //+------------------------------------------------------------------+  void NodeSetData(CMyTreeNode \*node,int mode)    {     if(mode%2==0)       {        node.SetLong(mode\*MathRand());        node.SetDouble(MathPow(2.02,mode)\*MathRand());       }     else       {        node.SetLong(mode\*(long)(-1)\*MathRand());        node.SetDouble(-MathPow(2.02,mode)\*MathRand());       }     node.SetString(str\_array[mode%10]);     node.SetDateTime(10000\*mode);    } |
