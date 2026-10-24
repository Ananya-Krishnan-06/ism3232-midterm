from business_rules import (
    calculate_print_cost,
    get_volume_discount,
    calculate_job_total,
    requires_proof,
    needs_overnight_run,
    total_invoiced,
    largest_job,
    format_job_line,
)

def test_print_cost_is_price_times_copies():
    assert round(calculate_print_cost(0.25, 100), 2) == 25.00

def test_discount_199_copies_is_zero():
    assert round(get_volume_discount(199), 2) == 0.00

def test_discount_200_copies():
    assert round(get_volume_discount(200), 2) == 0.08

def test_discount_999_copies():
    assert round(get_volume_discount(999), 2) == 0.08

def test_discount_1000_copies():
    assert round(get_volume_discount(1000), 2) == 0.15

def test_student_org_199_copies():
    assert round(get_volume_discount(199, student_org=True), 2) == 0.00

def test_student_org_200_copies():
    assert round(get_volume_discount(200, student_org=True), 2) == 0.13