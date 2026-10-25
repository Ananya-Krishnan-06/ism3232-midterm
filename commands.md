# Terminal Record: [the business name]

## 1. Building the project
cd ~/ism3232
mkdir ism3232-midterm
cd ~/ism3232/ism3232-midterm
python3 -m venv .venv && source .venv/bin/activate
pip install pytest ruff && pip freeze > requirements.txt
echo '.venv/' > .gitignore && echo '_pycache_/' >> .gitignore
touch business_rules.py main.py commands.md README.md
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
echo "# ism3232-midterm" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Ananya-Krishnan-06/ism3232-midterm.git
git push -u origin main
git add . && git commit -m 'ism3232-midterm' && git push
## 2. The virtual environment

which python3

/home/cryst/ism3232/ism3232-midterm/.venv/bin/python3

The output showing that python3 is active inside the virtual environment bin ( /.venv/bin/python3) indicates that the virtual environment is active.
## 3. The project structure
tree -L 2

.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files

Pycache is not in the repository because Python creates it on my computer to store copies of my code and we don't commit this so it doesn't show up on github.
## 4. Every function and test

rg 'def'

business_rules.py
11:def calculate_print_cost(copy_price: float, copies: int) -> float:
15:def get_volume_discount(copies: int, student_org: bool = False) -> float:
29:def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
41:def requires_proof(total: float) -> bool:
46:def needs_overnight_run(copies: int, total: float) -> bool:
50:def total_invoiced(jobs: list) -> float:
61:def largest_job(jobs: list) -> str:
76:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:

tests/test_business_rules.py
12:def test_print_cost_is_price_multiple_of_copies():
15:def test_discount_199_copies_is_zero():
18:def test_discount_200_copies():
21:def test_discount_999_copies():
24:def test_discount_1000_copies():
27:def test_student_org_199_copies():
30:def test_student_org_200_copies():
33:def test_job_total_has_no_setup_fee():
36:def test_job_total_adds_setup_fee_one_cent_below_40():
39:def test_setup_fee_is_based_on_discounted_cost():
42:def test_job_total_rounds_to_cents():
45:def test_student_org_changes_the_job_total():
52:def test_proof_only_above_300():
55:def test_proof_required_at_300_and_one_cent():
58:def test_overnight_for_above_500_copies():
61:def test_overnight_needed_at_one_more_than_500_copies():
64:def test_overnight_only_above_400():
67:def test_overnight_needed_at_one_more_than_400():
70:def test_total_invoiced_sums_every_job_including_student_orgs():
78:def test_largest_job_returns_first_job_listed_on_a_tie():
86:def test_largest_job_of_empty_list_is_empty_string():
89:def test_format_job_line_shows_two_decimals_and_displays_correctly():

business_rules.py defines 8 functions and tests/test_business_rulespy defines 22 tests.
## 5. Which files print

rg -l 'print'

main.py
tests/test_business_rules.py
business_rules.py

main.py and tests/test_business_rules.py print because they have print commands; however business_rules.py also prints because it has a function with the word 'print' in it.
## 6. The commit history

git log --oneline

b8184da (HEAD -> main, origin/main) realized i added an extra function and changed the code to have only 8 functions
41cb1dc wrote and checked all tests and they pass
4f3c3f1 testing copies and discount functions to pass
bea5837 finished code for report and summary and made sure it runs
08fff89 fixed a couple of errors
69078d2 importing funstions and setting up report
5e2e579 business rules functions defined
b977d79 ism3232-midterm
5840c89 first commit

At this point I made 9 commits.