# LoadNode


Reads node data from a file.

```cpp
bool  LoadNode(
   int         file_handle,     // handle
   CTreeNode*  main             // node
   )
```

Parameters

file\_handle

[in] Handle of a binary file that was earlier opened for reading.

main

[in]  Node for data.

Return Value

true - success, otherwise false.