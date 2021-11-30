#include <check.h>
#include <stdlib.h>
#include "../src/q3.h"

START_TEST(test_f_function)
{
    ck_assert_double_eq_tol(f(2.5,6.2), -6.02652, 0.001);
    ck_assert_double_eq_tol(f(1.1,9.1), -9.47506, 0.001);

}
END_TEST

Suite * f_suite(void)
{
    //creating a testing suite with test cases that hold the tests written above
    Suite *s = suite_create("Q3");
    TCase *tc_core = tcase_create("Core");
    tcase_add_test(tc_core, test_f_function);
    suite_add_tcase(s, tc_core);
    return s;
}

int main(void)
{
    int number_failed;
    Suite *s;
    SRunner *sr;

    s = f_suite();
    sr = srunner_create(s);

    srunner_run_all(sr, CK_NORMAL);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
    
}