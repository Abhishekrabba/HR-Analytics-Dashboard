import pandas as pd

def load_data():
    df = pd.read_csv('data/employee_data.csv')
    return df

def generate_summary(df):
    avg_salary = df['Salary'].mean()
    avg_tenure = df['Tenure'].mean()
    attrition_rate = (df['Attrition'] == 'Yes').mean() * 100
    dept_counts = df['Department'].value_counts()

    print("\n📊 HR Analytics Dashboard")
    print(f"Average Salary: ₹{avg_salary:.2f}")
    print(f"Average Tenure: {avg_tenure:.1f} years")
    print(f"Attrition Rate: {attrition_rate:.1f}%")
    print("\nEmployees by Department:")
    print(dept_counts)

    return {
        "Average Salary": avg_salary,
        "Average Tenure": avg_tenure,
        "Attrition Rate (%)": attrition_rate,
        "Department Counts": dept_counts.to_dict()
    }

def save_report(df):
    df.to_csv('reports/hr_summary.csv', index=False)
    print("\n✔ Report saved to 'reports/hr_summary.csv'")

def main():
    df = load_data()
    generate_summary(df)
    save_report(df)

if __name__ == "__main__":
    main()
