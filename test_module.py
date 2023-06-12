from arithmetic_arranger import arithmetic_arranger


class Test_arithmetic_arranger:
    def test_prueba(self):
        assert 0 == 0

    def test_no_letras(self):
        assert arithmetic_arranger(['k + 100', '13 - 30', '-45 - 100'],
                                   False) == f'Error: Numbers must only contain digits.'

    def test_no_big_numbers(self):
        assert arithmetic_arranger(['10000 + 100', '13 - 30', '-45 - 100'],
                                   False) == f'Error: Numbers cannot be more than four digits.'

    def test_only_plus_minus(self):
        assert arithmetic_arranger(['10 + 100', '13 * 30', '-45 - 100'],
                                   False) == f'Error: Operator must be \'+\' or \'-\'.'

    def test_many_operations(self):
        assert arithmetic_arranger(['10 + 100', '13 - 30', '-45 - 100', '23 + 36', '18 - 10', '19 + 20'],
                                   False) == f'Error: Too many problems.'

    def test_list_null(self):
        assert arithmetic_arranger([''], False) == f'Error: Must enter at least one exercise.'

    def test_num_real(self):
        assert arithmetic_arranger(['20 + 25', '23.56 + 0.46', '-500 - 694'],
                                   False) == f'Error: Numbers must only contain digits.'

