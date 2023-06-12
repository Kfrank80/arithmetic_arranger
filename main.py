from test_module import Test_arithmetic_arranger
from arithmetic_arranger import arithmetic_arranger


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
    tests = Test_arithmetic_arranger()
    tests.test_num_real()
    tests.test_no_letras()
    tests.test_no_big_numbers()
    tests.test_many_operations()
    tests.test_list_null()
    tests.test_only_plus_minus()

   
