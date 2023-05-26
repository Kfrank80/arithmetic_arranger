

import pytest

from arithmetic_arranger import arithmetic_arranger

class Testarithmetic_arranger:
    def test_prueba(self):
        assert 0 == 0

    def test_no_letras(self):
        assert arithmetic_arranger(['k + 100','13 - 30','-45 - 100'], False) == f'Error: Numbers must only contain digits.'

    def test_no_bignumbers(self):
        assert arithmetic_arranger(['10000 + 100','13 - 30','-45 - 100'], False) == f'Error: Numbers cannot be more than four digits.'

    def test_only_plus_minus(self):
        assert arithmetic_arranger(['10 + 100','13 * 30','-45 - 100'], False) == f'Error: Operator must be \'+\' or \'-\'.'

    def test_many_operations(self):
        assert arithmetic_arranger(['10 + 100', '13 - 30', '-45 - 100', '23 + 36', '18 - 10', '19 + 20'], False) == f'E' \
                                                                                                                    f'rror: Too many problems.'
    def test_listnull(self):
        assert arithmetic_arranger([''], False) == f'Error: Must enter at least one exercise.'

    def test_numreal(self):
        assert arithmetic_arranger(['20 + 25', '23.56 + 0.46', '-500 - 694'], False) == f'Error: Numbers must only contain digits.'
