#include <check.h>
#include <stdlib.h>
#include "../src/q1.h"

START_TEST(test_isLeapYr_function)
{
    ck_assert_int_eq(isLeapYr(2000), 1);
    ck_assert_int_eq(isLeapYr(1896), 1);
    ck_assert_int_eq(isLeapYr(1968), 1);
    ck_assert_int_eq(isLeapYr(1988), 1);
    ck_assert_int_eq(isLeapYr(1805), 0);
    ck_assert_int_eq(isLeapYr(2005), 0);

}
END_TEST

Suite * leapYr_suite(void)
{
    //creating a testing suite with test cases that hold the tests written above
    Suite *s = suite_create("Q1");
    TCase *tc_core = tcase_create("Core");
    tcase_add_test(tc_core, test_isLeapYr_function);
    suite_add_tcase(s, tc_core);
    return s;
}

int main(void)
{
    int number_failed;
    Suite *s;
    SRunner *sr;

    s = leapYr_suite();
    sr = srunner_create(s);

    srunner_run_all(sr, CK_NORMAL);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
    
}