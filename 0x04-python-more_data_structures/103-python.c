#include <Python.h>
#include <bytesobject.h>
#include <object.h>
#include <listobject.h>

#define GET PyList_GetItem
#define SIZE Py_SIZE


/**
 * print_python_list - prints info about python lists
 * @p: pointer, pyobject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	Py_ssize_t index;

	list = (PylistListObject *) p;

	printf("[*] Python list info\n")
	printf("[*] Size of the Python List = %d\n", (int) SIZE(list));
	printf("[*] Allocated = %d\n", (int) list->allocated);

	for (index = 0; index < SIZE(list); index++)
	{
		item = GET(p, index);
		if (item != NULL)
			printf("Element %d: %s\n", (int) index, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints info about Python Bytes
 * @p: PyObject
 */

void print_python_bytes(PyObject *p)
{
	
}
