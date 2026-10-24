#business_rules.py
#Author: Ananya Krishnan

SETUP_FEE = 15.00
SETUP_FEE_THRESHOLD = 40.00
PROOF_THRESHOLD = 300.00
OVERNIGHT_COPIES = 500
OVERNIGHT_TOTAL = 400.00
STUDENT_BONUS = 0.05

def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Return the print cost before any discount."""
    return copy_price*copies

def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if copies >= 1000:
        rate = 0.15
    elif copies >= 200:
        rate = 0.08
    else:
        return 0.0
   
    if student_org:
        rate += STUDENT_BONUS
    return round(rate, 2)


def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
    """Return the job total: discounted cost plus setup fee when it applies."""
    cost = calculate_print_cost(copy_price, copies)
    discount = get_volume_discount(copies, student_org)
    discounted = round(cost * (1 - discount), 2)


    if discounted < SETUP_FEE_THRESHOLD:
        discounted += SETUP_FEE
    return round(discounted, 2)


def requires_proof(total: float) -> bool:
    """Return True when the job total requires a printed proof"""
    return total > PROOF_THRESHOLD


def needs_overnight_run(copies: int, total: float) -> bool:
    """Return True when the job needs an overnight press run."""
    return copies > OVERNIGHT_COPIES or total > OVERNIGHT_TOTAL


def _job_total(job: dict) -> float:
    """Helper: compute the total for one job dict."""
    return calculate_job_total(
        job["copy_price"],
        job["copies"],
        job.get("student_org", False),
    )


def total_invoiced(jobs: list) -> float:
    """Return the sum of the job totals for every job in the list."""
    total = 0.0
    for job in jobs:
        total += _job_total(job)
    return round(total, 2)

def largest_job(jobs: list) -> str:
    """Return the title of the job with the largest total (first win ties)."""
    best_title = ""
    best_total = None 
    for job in jobs:
        total = _job_total(job)
        if best_total is None or total > best_total:
            best_total = total
            best_title = job["title"]
    return best_title

def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
    """Return one report line"""
    proof_text = "yes" if proof else "no"
    overnight_text = "yes" if overnight_run else "no"
    return f"{title}: ${total:.2f} | proof: {proof_text} | overnight run: {overnight_text}"
