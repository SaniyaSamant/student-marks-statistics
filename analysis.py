import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, t

data = pd.read_csv("student_marks.csv", delimiter=',', header=None)

data.columns = ['mid_sem_marks', 'end_sem_marks', 'result']

# Calculated average marks
data['avg_marks'] = (data['mid_sem_marks'] + data['end_sem_marks']) / 2

# Calculated the population mean
mean = data[['mid_sem_marks', 'end_sem_marks']].values.mean()

# Calculated variance and standard deviation
variance = ((data[['mid_sem_marks', 'end_sem_marks']].values - mean) ** 2).sum() / (len(data)-1)
standard_deviation = np.sqrt(variance)

# Total number of rows or entries in the dataset
total_rows = data.shape[0]

# Function to calculate confidence interval
def calculate_confidence_interval(n, confidence_level):
    if n < 30:
        # For n < 30, use t-table
        t_value = t.ppf((1 + confidence_level) / 2, n - 1)
        error = t_value * (standard_deviation / np.sqrt(n))
    else:
        # For n >= 30, use z-table
        z_value = norm.ppf((1 + confidence_level) / 2)
        error = z_value * (standard_deviation / np.sqrt(n))

    return error

while True:
    print("\nMenu:")
    print("1. Plot distribution of students based on result")
    print("2. Print statistics")
    print("3. Plot normal distribution of student marks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Function to plot distribution of students based on result
        def plot_distribution():
            distinction_students = data[data['avg_marks'] > 70]

            passed_count = len(data[data['result'] == 1])
            failed_count = len(data[data['result'] == 0])
            distinction_count = len(distinction_students)

            # Create a bar graph
            categories = ['Failed', 'Passed', 'Passed (Distinction)']
            counts = [failed_count, passed_count, distinction_count]

            plt.bar(categories, counts, color=['red', 'green', 'blue'])
            plt.xlabel('Categories')
            plt.ylabel('Number of Students')
            plt.title('Distribution of Students Based on Result')

            plt.show()

        plot_distribution()
    elif choice == '2':
        # Function to print statistics
        def print_statistics():
            total_passed = len(data[data['result'] == 1])
            total_failed = len(data[data['result'] == 0])
            total_students = total_passed + total_failed
            pass_probability = total_passed / total_students
            fail_probability = total_failed / total_students
            print('Total Students: ',total_students)
            print('Total Passed Students: ',total_passed)
            print('Probability of Passing: ',pass_probability)
            print('Total Failed Students: ',total_failed)
            print('Probability of Failing: ',fail_probability)
            print("Variance (Normal Variance): ",variance)
            print("Standard Deviation: ",standard_deviation)
            print("Mean: ",mean)
            confidence_level = float(input("Enter confidence level (e.g., 0.95): "))
            n = int(input("Enter value of n: "))
            error = calculate_confidence_interval(n, confidence_level)
            popul_mean_conf_val_high = mean + error
            popul_mean_conf_val_low = mean - error
            population_std=standard_deviation/np.sqrt(n)
            population_variance=population_std**2
            print("Confidence level population mean upper val : ", popul_mean_conf_val_high)
            print("Confidence level population mean lower val: ",popul_mean_conf_val_low)
            print("Population Variance: ",population_variance)
            print("Population Standard Deviation: ",population_std)
        print_statistics()
    elif choice == '3':
        # Plot normal distribution of student marks
        plt.figure(figsize=(10, 6))
        plt.hist(data['avg_marks'], bins=20, density=True, alpha=0.6, color='g')

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean, standard_deviation)
        plt.plot(x, p, 'k', linewidth=2)
        title = "Fit results: mean = %.2f,  std dev = %.2f" % (mean, standard_deviation)
        plt.title(title)

        plt.show()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")