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

def test_print_cost_is_price_multiple_of_copies():
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

def test_job_total_has_no_setup_fee():
    assert round(calculate_job_total(40.00, 1), 2) == 40.00

def test_job_total_adds_setup_fee_one_cent_below_40():
    assert round(calculate_job_total(39.99, 1), 2) == 54.99

def test_setup_fee_is_based_on_discounted_cost():
    assert round(calculate_job_total(0.20, 200), 2) == 51.80

def test_job_total_rounds_to_cents():
    assert round(calculate_job_total(0.10, 501), 2) == 46.09

def test_student_org_changes_the_job_total():
    regular = round(calculate_job_total(1.00, 200, student_org=False), 2)
    student = round(calculate_job_total(1.00, 200, student_org=True), 2)
    assert regular == 184.00  
    assert student == 174.00   
    assert student <= regular

def test_proof_only_above_300():
    assert requires_proof(300.00) is False

def test_proof_required_at_300_and_one_cent():
    assert requires_proof(300.01) is True

def test_overnight_for_above_500_copies():
    assert needs_overnight_run(500, 100.00) is False

def test_overnight_needed_at_one_more_than_500_copies():
    assert needs_overnight_run(501, 100.00) is True

def test_overnight_only_above_400():
    assert needs_overnight_run(100, 400.00) is False

def test_overnight_needed_at_one_more_than_400():
    assert needs_overnight_run(100, 400.01) is True

def test_total_invoiced_sums_every_job_including_student_orgs():
    jobs = [
        {"title": "A", "copy_price": 0.25, "copies": 100, "student_org": False},
        {"title": "B", "copy_price": 1.00, "copies": 200, "student_org": False},
        {"title": "C", "copy_price": 1.00, "copies": 200, "student_org": True},
    ]
    assert round(total_invoiced(jobs), 2) == 398.00

def test_largest_job_returns_first_job_listed_on_a_tie():
    jobs = [
        {"title": "Small", "copy_price": 0.25, "copies": 100, "student_org": False},
        {"title": "Big", "copy_price": 1.20, "copies": 250, "student_org": False},
        {"title": "Medium", "copy_price": 1.00, "copies": 200, "student_org": False},
    ]
    assert largest_job(jobs) == "Big"

def test_largest_job_of_empty_list_is_empty_string():
    assert largest_job([]) == ""

def test_format_job_line_shows_two_decimals_and_displays_correctly():
    assert format_job_line("Tickets", 5, False, True) == "Tickets: $5.00 | proof: no | overnight run: yes"
