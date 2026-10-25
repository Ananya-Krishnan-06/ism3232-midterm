# ISM3232 Midterm: Brightline Print Shop

- **Name:** Ananya Krishnan
- **Version:** Final
- **Date:** 10/24/2026

## What This Program Does
This program creates a job report for Brightline Print Shop. The program calculates the total cost using the price per copy and number of copies, and applies the volume discount, then adds the extra student organization discount, and then $15 setup fee for small jobs. It also flags whether a job needs printed proof or an overnight press run, and prints a single report line for each job. The program also provides a summary of the job count, the total invoiced, an average job total, largest job, the number of proofs required, and the number of overnight runs. 
## Business Rules
1) The print cost is equal to the price per copy multiplied by the number of copies
2) There is no volume discount if it is under 200 copies, but it will be 8% for any number of copies between 200 upto 999, and 15% for more than 1000 copies.
3) Student organizations get an additional 5% off, but only on print jobs of 200 copies or more.
4) If the discounted cost is below $40, then an additional setup fee of $15 must be added.
5) A printed proof is required if the total for the print job goes over $300.
6) When a print job requires more than 500 copies or totals over $400, then it requires an overnight press run.
## How to Run
```
cd ~/ism3232
mkdir ism3232-midterm
cd ~/ism3232/ism3232-midterm
python3 -m venv .venv && source .venv/bin/activate
pip install pytest ruff && pip freeze > requirements.txt
echo '.venv/' > .gitignore && echo '_pycache_/' >> .gitignore
touch business_rules.py main.py commands.md README.md
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
python3 main.py
```

## How to Test
```
ruff format .
ruff check .
pytest -v
```
The test file has 22 tests.

## Files in This Repository
`README.md`: this file
`business_rules.py`: the eight functions and the constants for this program
`commands.md`: the terminal commands that I used to build and check the project, with the outputs and explanations
`main.py`: the sample jobs and the summary report
`requirements.txt`: the required packages to be installed
`.gitignore`: used to keep `.venv/` and `__pycache__/` out of the repository
`tests/test_business_rules.py`: this is the file with the pytest tests
`tests/__init__.py`: an empty file that allows the tests to import the required functions

## AI Use Statement

I did not use AI on this exam.
