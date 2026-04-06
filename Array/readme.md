# Array Operations in Python

this just a practice and understand deep logic building and understand data structure

---

## 📌 Overview

This project demonstrates how basic array operations work internally without using Python’s built-in dynamic list features.  
It mimics a **fixed-size array** and performs manual operations like:

- Insert (at start, middle, end)
- Delete (from start, middle, end)

---

## ⚙️ Core Concept

- Fixed-size array using Python list
- Empty slots are represented by `None`
- Manual shifting of elements

---

## 🧩 Functions Explanation

### 🔹 give_array(size)
Creates an array of given size filled with `None`.

### 🔹 length(li)
Counts number of actual elements (ignores `None`).

### 🔹 print_array(li)
Prints elements until `None` appears. Raises error if empty.

---

## ➕ Insert Operations

### 🔹 add_on_zero(array, value)
- Shifts elements right
- Inserts at index `0`

### 🔹 add_at_last(array, value)
- Inserts at next available position

### 🔹 add_at_mid(array, value, idx)
- Shifts elements right from index
- Inserts at given position

---

## ➖ Delete Operations

### 🔹 remove_at_zero(array)
- Shifts elements left
- Removes first element

### 🔹 remove_at_last(li)
- Removes last element

### 🔹 remove_at_mid(li, idx)
- Shifts elements left from index
- Removes element at given index

---

## ▶️ Execution Flow

1. Create array
2. Insert elements (start, end, middle)
3. Print array
4. Perform delete operations
5. Print after each operation

---

## 🧠 Full Code

```python
# play with array

# Basic functions
def give_array(size: int) -> list:
    return [None for _ in range(size)]

def length(li:list) -> int: 
    size = 0
    for ele in li :
        if ele != None:
            size += 1
    return size

def print_array(li:list)->None :
    if li[0] == None :
        raise ValueError("Empty array")
    for ele in li :
        if ele == None :
            print()
            break
        else :
            print(ele,end=" ")

# Add elements functions
def add_on_zero(array: list, value: int) -> None:
    size = length(array)

    if size == len(array):
        raise Exception("Array is full!")
        return

    for i in range(size, 0, -1):
        array[i] = array[i-1]

    array[0] = value

def add_at_last(array: list,value:int):
    size = length(array)
    array[size] = value

def add_at_mid(array,value,idx):
    size = length(array)
    for i in range(size,idx,-1):
        array[i] = array[i-1]
    array[idx] = value

# remove elements functions
def remove_at_zero(array: list) -> None:
    size = length(array)
    for i in range(1, size):
        array[i-1] = array[i]
    array[size-1] = None

def remove_at_last(li):
    size = length(li)
    li[size-1] = None

def remove_at_mid(li,idx):
    size = length(li)
    for i in range (idx,size):
        if i+1 < size :
            li[i] = li[i+1] 
    if li[size-1] != None:
        li[size-1] = None

if __name__ =="__main__" :
    li = give_array(5)

    add_on_zero(li, 10)
    add_on_zero(li, 20)
    add_at_last(li, 30)
    add_at_mid(li,80,2)

    print_array(li)

    remove_at_zero(li)
    print_array(li)

    remove_at_last(li)
    print_array(li)

    remove_at_mid(li,1)
    print_array(li)
