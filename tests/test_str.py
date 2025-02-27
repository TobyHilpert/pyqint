import unittest
from nose.tools import nottest
import pyqint
from pyqint import PyQInt, Molecule
import numpy as np
import multiprocessing
import os

class TestString(unittest.TestCase):

    def test_strings(self):
        """
        Test automatic integral evaluation for hydrogen molecule
        """

        # construct integrator object
        integrator = PyQInt()

        # build hydrogen molecule
        mol = Molecule('H2')
        mol.add_atom('H', 0.0, 0.0, 0.0)
        mol.add_atom('H', 0.0, 0.0, 1.4)
        cgfs, nuclei = mol.build_basis('sto3g')

        ans = "CGF; R=(0.000000,0.000000,0.000000)\n"
        ans += " 01 | GTO : c=0.154329, alpha=3.425251, l=0, m=0, n=0, R=(0.000000,0.000000,0.000000)\n"
        ans += " 02 | GTO : c=0.535328, alpha=0.623914, l=0, m=0, n=0, R=(0.000000,0.000000,0.000000)\n"
        ans += " 03 | GTO : c=0.444635, alpha=0.168855, l=0, m=0, n=0, R=(0.000000,0.000000,0.000000)\n"
        self.assertEqual(str(cgfs[0]), ans)

        ans = "Molecule: H2\n"
        ans += " H (0.000000,0.000000,0.000000)\n"
        ans += " H (0.000000,0.000000,1.400000)\n"
        self.assertEqual(str(mol), ans)

    def test_version(self):
        strver = pyqint.__version__.split('.')
        self.assertTrue(strver[0].isnumeric())
        self.assertTrue(strver[1].isnumeric())
        self.assertTrue(strver[2].isnumeric())
        self.assertTrue(strver[3].isnumeric())

    @nottest
    def test_compiler_info(self):
        """
        Test automatic integral evaluation for hydrogen molecule
        """
        # construct integrator object
        integrator = PyQInt()

        compiler_info = integrator.get_compile_info()
        self.assertTrue(len(compiler_info["compiler_version"]) > 4)
        self.assertTrue(len(compiler_info["compile_date"]) > 10)
        self.assertTrue(len(compiler_info["compile_time"]) > 4)
        self.assertTrue(len(compiler_info["openmp_version"]) > 2)

if __name__ == '__main__':
    unittest.main()
