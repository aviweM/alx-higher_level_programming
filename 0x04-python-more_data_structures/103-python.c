#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Function that prints basic info about python objects
 * @p: PyObject
 */

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


void print_python_list(PyObject *p)
{
	int size, u, alloc;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (u = 0; u < size; u++)
	{
		type = list->ob_item[u]->ob_type->tp_name;
		printf("Element %d: %s\n", u, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[u]);
	}
}

/**
 * print_python_bytes - Fucntion that prints basic info of python bytes
 * @p: Pyobject of byte CPython structure
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char size, d;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (d = 0; d < size; d++)
	{
		printf("%02hhx", bytes->ob_sval[d]);
		if (d == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
