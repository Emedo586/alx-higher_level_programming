#include <Python.h>

/**
 * print_python_list_info - Prints basic info about python lists.
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
<<<<<<< HEAD
	int size, alloc, i;
	PyObject *obj;size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = Pylist_GetItem(p, i);
		printf{"%s\n", Py_TYPE(obj)->tp_name};
	}
=======
int size, alloc, i;
PyObject *obj;

size = Py_SIZE(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (i = 0; i < size; i++)
{
printf("Element %d: ", i);
obj = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(obj)->tp_name);
}
>>>>>>> 41047b4c468be576d9e80dcffd6d8ad4f859eeeb
}
