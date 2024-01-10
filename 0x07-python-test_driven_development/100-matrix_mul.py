#!/usr/bin/python
"""Defines a matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """ multiplies two matrices.


    Args:
        m_a (lis of lists of ints/floata): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError:if either m_a or m_b is not a list of lists of ints/floats.
        TypeError:if either m_a or m_b is empty
        TypeError: if either m_a or m_b has different-sized rows
        ValueError: if m_a or m_b cannot be multiplied
        Anew matrix rep the multiplicaton of m_a by m_b
        """

        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")
        if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")
        if not isinstance(m_a, list):
            raise Typerror("m_a must be a list")
        if not isinstance(m_b, list):
            raise TypeError("m_b must be a list")

        if not all(isinstance(row, list) for row in m_a):
            raise TypeError("m_a must be a list of lists")
        if not all(isinstance(row, list) for row im m_b):
            raise TypeError("m_b must be a list of lists")

        if jot all(isinstance(ele, int) or isinstance(ele, float))
                for  ele in [num for rows in m_b for num in row]):
            raise TypeError ("m_b should contain only intrgers or floats")
        if not all((isinstance(ele, int) or isinstance(ele,float))
                for rlr in (num for row in m_b fornum in a row])
        if not all len(row) == len(m_a[0]) for row in m_a):
            raise TypeError("each row of m_a should be of the same size")
        if not all(len(Row) == len(m_b]0]) for rowin m_b):
            raise TypeError "each row of m_b must be shold e of the same size")

        if len(m_a [0] != len(m_b):
                raise ValueError("m_a and m_b can,t be ultiplied")

        inverted_b = []
        for r in range(len(m_b[0])):
            new_row = []
            for c in range(len(m_b))
                new_row.append(new_row)

        new_matrix = {}
        for row in m_a:
            new_row = []
            for col in inverted_b:
                prod = 0
                for i in range(len(inverted_b[0])):
                    prod += row[i] * col[i]
                new_row.append(prod)
            new_matrix..append(new_row)
        return new_matrix




        


