# CTreeNode

CTreeNode

CTreeNode is a class of the CTree binary tree node.

Description

CTreeNode provides the ability to work with nodes of the [CTree](../CTree/CTree.md) binary tree. Options of navigation through the tree are implemented in the class. Besides, methods of working with the file are implemented.

Declaration

|  |
| --- |
| class CTreeNode : public CObject |

Title

|  |
| --- |
| #include <Arrays\TreeNode.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CTreeNode  Direct descendants  [CTree](../CTree/CTree.md) |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Owner](Owner/Owner.md) | Gets/sets the pointer of the owner node |
| [Left](Left/Left.md) | Gets/sets the pointer of the left node |
| [Right](Right/Right.md) | Gets/sets the pointer of the right node |
| [Balance](Balance/Balance.md) | Gets the node balance |
| [BalanceL](BalanceL/BalanceL.md) | Gets the balance of the left sub-branch of the node |
| [BalanceR](BalanceR/BalanceR.md) | Gets the balance of the right sub-branch of the node |
| Creation of a new element |  |
| [CreateSample](CreateSample/CreateSample.md) | Creates a new node instance |
| Comparison |  |
| [RefreshBalance](RefreshBalance/RefreshBalance.md) | Recalculates the node balance |
| Search |  |
| [GetNext](GetNext/GetNext.md) | Gets the pointer of the next node |
| Input/Output |  |
| [SaveNode](SaveNode/SaveNode.md) | Saves the node data to a file |
| [LoadNode](LoadNode/LoadNode.md) | Downloads the node data from a file |
| virtual [Type](Type/Type.md) | Gets the identifier of the node type |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |

Trees of CTreeNode class descendants have practical application.

A descendant of CTreeNode class should have predefined methods: [CreateSample](CreateSample/CreateSample.md) creates a new instance of the descendant class of CTreeNode, [Compare](../../Basic-Class-CObject/Compare/Compare.md) compares values of key fields of the descendant class of CTreeNode, [Type](../../Basic-Class-CObject/Type/Type.md) (if it is necessary to identify a node), [SaveNode](SaveNode/SaveNode.md) and [LoadNode](LoadNode/LoadNode.md) (if it is necessary to work with a file).

Let's consider an example of a CTree descendant class.

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                                   MyTreeNode.mq5 |  //|                        Copyright 2010, MetaQuotes Software Corp. |  //|                                       https://www.metaquotes.net/ |  //+------------------------------------------------------------------+  #property copyright "2010, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  //---  #include <Arrays\TreeNode.mqh>  //+------------------------------------------------------------------+  //| Describe CMyTreeNode class derived from CTreeNode.               |  //+------------------------------------------------------------------+  //| Class CMyTreeNode.                                               |  //| Purpose: Class of element of a binary tree.                      |  //|             Descendant of class CTreeNode.                       |  //+------------------------------------------------------------------+  class CMyTreeNode : public CTreeNode    {  protected:     //--- user's data     long              m\_long;            // key field of long type     double            m\_double;          // custom variable of double type     string            m\_string;          // custom variable of string type     datetime          m\_datetime;        // custom variable of datetime type     public:                       CMyTreeNode();     //--- methods of accessing user's data     long              GetLong(void)                { return(m\_long); }     void              SetLong(long value)          { m\_long=value;  }     double            GetDouble(void)              { return(m\_double); }     void              SetDouble(double value)      { m\_double=value;  }     string            GetString(void)              { return(m\_string); }     void              SetString(string value)      { m\_string=value;  }     datetime          GetDateTime(void)            { return(m\_datetime); }     void              SetDateTime(datetime value)  { m\_datetime=value;  }     //--- methods for working with files     virtual bool      Save(int file\_handle);     virtual bool      Load(int file\_handle);  protected:     virtual int       Compare(const CObject \*node,int mode);     //--- method of creating class instances     virtual CTreeNode\* CreateSample();    };  //+------------------------------------------------------------------+  //| CMyTreeNode class constructor.                                   |  //| INPUT:  none.                                                    |  //| OUTPUT: none.                                                    |  //| REMARK: none.                                                    |  //+------------------------------------------------------------------+  void CMyTreeNode::CMyTreeNode()    {  //--- initialization of user's data     m\_long        =0;     m\_double      =0.0;     m\_string      ="";     m\_datetime    =0;    }  //+------------------------------------------------------------------+  //| Comparison with another tree node by the specified algorithm.    |  //| INPUT:  node - tree element to compare,                          |  //|         mode - identifier of comparison algorithm.               |  //| OUTPUT: result of comparison (>0,0,<0).                          |  //| REMARK: none.                                                    |  //+------------------------------------------------------------------+  int CMyTreeNode::Compare(const CObject \*node,int mode)    {  //--- mode parameter is ignored, because tree construction algorithm is the only one     int res=0;  //--- explicit type casting     CMyTreeNode \*n=node;     res=(int)(m\_long-n.m\_long);  //---     return(res);    }  //+------------------------------------------------------------------+  //| Creation of a new class instance.                                |  //| INPUT:  none.                                                    |  //| OUTPUT: pointer to a new instance of CMyTreeNode class.          |  //| REMARK: none.                                                    |  //+------------------------------------------------------------------+  CTreeNode\* CMyTreeNode::CreateSample()    {     CMyTreeNode \*result=new CMyTreeNode;  //---     return(result);    }  //+------------------------------------------------------------------+  //| Write tree node data to a file.                                  |  //| INPUT:  file\_handle -handle of a file pre-opened for writing.    |  //| OUTPUT: true if OK, otherwise false.                             |  //| REMARK: none.                                                    |  //+------------------------------------------------------------------+  bool CMyTreeNode::Save(int file\_handle)    {     uint i=0,len;  //--- checks     if(file\_handle<0) return(false);  //--- writing user data  //--- writing custom variable of long type     if(FileWriteLong(file\_handle,m\_long)!=sizeof(long))          return(false);  //--- writing custom variable of double type     if(FileWriteDouble(file\_handle,m\_double)!=sizeof(double))    return(false);  //--- writing custom variable of string type     len=StringLen(m\_string);  //--- write string length     if(FileWriteInteger(file\_handle,len,INT\_VALUE)!=INT\_VALUE)   return(false);  //--- write the string     if(len!=0 && FileWriteString(file\_handle,m\_string,len)!=len) return(false);  //--- writing custom variable of datetime type     if(FileWriteLong(file\_handle,m\_datetime)!=sizeof(long))      return(false);  //---     return(true);    }  //+------------------------------------------------------------------+  //| Read tree node data from a file.                                 |  //| INPUT:  file\_handle -handle of a file pre-opened for reading.    |  //| OUTPUT: true if OK, otherwise false.                             |  //| REMARK: none.                                                    |  //+------------------------------------------------------------------+  bool CMyTreeNode::Load(int file\_handle)    {     uint i=0,len;  //--- checks     if(file\_handle<0) return(false);  //--- reading     if(FileIsEnding(file\_handle)) return(false);  //--- reading custom variable of char type  //--- reading custom variable of long type     m\_long=FileReadLong(file\_handle);  //--- reading custom variable of double type     m\_double=FileReadDouble(file\_handle);  //--- reading custom variable of string type  //--- read the string length     len=FileReadInteger(file\_handle,INT\_VALUE);  //--- read the string     if(len!=0) m\_string=FileReadString(file\_handle,len);     else       m\_string="";  //--- reading custom variable of datetime type     m\_datetime=FileReadLong(file\_handle);  //---     return(true);    } |
