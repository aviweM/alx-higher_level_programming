#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - prints some basic info about pytohn list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int u;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (u = 0; u < size; u++)
		printf("Element %i: %s\n", u, Py_TYPE(obj->ob_item[u])->tp_name);
}
