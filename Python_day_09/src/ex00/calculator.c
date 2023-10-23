#include <Python.h>

static PyObject *add(PyObject *self, PyObject *args) {
  double num1, num2 = 0;

  if (!PyArg_ParseTuple(args, "dd", &num1, &num2)) {
    return NULL;
  }

  return PyFloat_FromDouble(num1 + num2);
}

static PyObject *sub(PyObject *self, PyObject *args) {
  double num1, num2 = 0;

  if (!PyArg_ParseTuple(args, "dd", &num1, &num2)) {
    return NULL;
  }

  return PyFloat_FromDouble(num1 - num2);
}

static PyObject *mul(PyObject *self, PyObject *args) {
  double num1, num2 = 0;

  if (!PyArg_ParseTuple(args, "dd", &num1, &num2)) {
    return NULL;
  }

  return PyFloat_FromDouble(num1 * num2);
}

static PyObject *divide(PyObject *self, PyObject *args) {
  double num1, num2 = 0;

  if (!PyArg_ParseTuple(args, "dd", &num1, &num2)) {
    return NULL;
  }

  if (num2 == 0) {
    PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero");
    return NULL;
  }

  return PyFloat_FromDouble(num1 / num2);
}

static PyMethodDef CalculatorMethods[] = {
    {"add", add, METH_VARARGS, "Add function"},
    {"sub", sub, METH_VARARGS, "Sub function"},
    {"mul", mul, METH_VARARGS, "Mul function"},
    {"div", divide, METH_VARARGS, "Div function"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef CalculatorModule = {
    PyModuleDef_HEAD_INIT, "calculator", "Calculator", -1, CalculatorMethods};

PyMODINIT_FUNC PyInit_calculator(void) {
  return PyModule_Create(&CalculatorModule);
}