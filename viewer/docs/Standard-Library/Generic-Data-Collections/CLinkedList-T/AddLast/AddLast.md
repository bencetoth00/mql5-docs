# AddLast


Adds an element at the end of the linked list

The version that adds an element by value.

```cpp
CLinkedListNode<T>* AddLast(
   T  value                      // an element to add
   );
```

Return Value

Returns a pointer to the added node.

The version that adds an element as a formed node by value.

```cpp
bool AddLast(
   CLinkedListNode<T>*  node     // the node to add
   );
```

Parameters

value

[in]  An element to be added.

\*node

[in]  A node to be added.

Return Value

Returns true on successful, or false otherwise.