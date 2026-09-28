# Student Marks Statistical Analysis

A **Probability & Statistics** project that performs statistical analysis on student exam results — computing descriptive statistics, confidence intervals, and visualizing mark distributions.

## What It Does

Given a dataset of student mid-semester and end-semester marks with pass/fail labels, the program provides an interactive menu to:

1. **Plot result distribution** — bar chart of Failed / Passed / Passed with Distinction students
2. **Print statistics** — mean, variance, standard deviation, pass/fail probability, and a configurable confidence interval for the population mean
3. **Plot normal distribution** — histogram of average marks overlaid with a fitted normal distribution curve

## Statistical Concepts Used

| Concept | Implementation |
|---------|---------------|
| Population mean | Average of all mid + end sem marks |
| Variance | Sample variance (divided by n−1) |
| Standard deviation | √variance |
| Confidence interval | t-distribution for n < 30, z-distribution for n ≥ 30 |
| Pass probability | P(pass) = passed students / total students |
| Distinction | Students with average marks > 70 |

## Dataset

`student_marks.csv` — comma-separated values with no header:

```
mid_sem_marks, end_sem_marks, result
34.62, 78.02, 0
60.18, 86.30, 1
...
```

- `result`: 1 = Pass, 0 = Fail
- 800 records

## Setup

```bash
pip install pandas matplotlib numpy scipy
```

## Run

```bash
python analysis.py
```

**Menu:**
```
1. Plot distribution of students based on result
2. Print statistics
3. Plot normal distribution of student marks
4. Exit
```

For option 2, you will be prompted to enter:
- `confidence level` — e.g., `0.95` for 95% confidence
- `n` — sample size (uses t-table if n < 30, z-table if n ≥ 30)

## Sample Output

**Statistics (example):**
```
Total Students:  800
Total Passed Students:  631
Probability of Passing:  0.789
Total Failed Students:  169
Probability of Failing:  0.211
Variance:  236.45
Standard Deviation:  15.38
Mean:  70.23
Confidence level population mean upper val:  71.30
Confidence level population mean lower val:  69.16
```
