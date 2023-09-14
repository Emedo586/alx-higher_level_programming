#!/usr/bin/python3
#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
* print_python_list - Prints basic info about Python lists.
* @p: A pyObject list object.
*/
void print_python_list(PyObject *p)
{
    int size, alloc, i;
    const char *type;
    PyListObject *list = ()
}
