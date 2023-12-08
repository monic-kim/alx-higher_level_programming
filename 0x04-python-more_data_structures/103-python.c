#include <python .h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int size;
	int x;
	char *trying_str = NULL ;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &trying_str, &sixe);
	printf(" size: %li\n", size);
	printf(" trying string: %s\n",tring_str);
	if(size < 10)
		printf(" first %li bytes:", size + 1);
	else
		printf(" first 10 bytes:");
	for (x = 0; x <= size && x < 10; x++)
		printf(" %02hhx", trying_str[i]);
	printf("/n");
}

void print_python_list(PyObject *p)
{
	long int = PyList_Size(p);
	int x;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (x = 0; x < size; x++)
	{
		type = (list->ob_item[x]->ob_type->tp_name);
		printf("Element %x: %s\n", x, type);
		if(!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[x]);
	}
}
