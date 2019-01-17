from test_framework import generic_test


def find_salary_cap(target_payroll, current_salaries):
    # TODO - you fill in here.
    current_salaries.sort()
    salary_sum = 0.0
    length = len(current_salaries)
    for index, salary in enumerate(current_salaries):
        salary_sum += salary
        total_sum = salary_sum + (length - index - 1) * salary
        if total_sum >= target_payroll:
            return (target_payroll - (salary_sum - salary)) / (length - index)
    return -1.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
