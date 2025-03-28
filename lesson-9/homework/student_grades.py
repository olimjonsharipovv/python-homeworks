
import csv

def read_grades(filename):
    grades = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
           
            row['Grade'] = int(row['Grade'])
            grades.append(row)
    return grades

def calculate_averages(grades):
    subject_grades = {}
    
    for record in grades:
        subject = record['Subject']
        grade = record['Grade']
        
        if subject not in subject_grades:
            subject_grades[subject] = {'total': 0, 'count': 0}
        
        subject_grades[subject]['total'] += grade
        subject_grades[subject]['count'] += 1
    
    averages = {}
    for subject, data in subject_grades.items():
        averages[subject] = data['total'] / data['count']
    
    return averages

def write_averages(filename, averages):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        
        for subject, avg_grade in averages.items():
            writer.writerow([subject, avg_grade])

def main():
    grades = read_grades('grades.csv')

    averages = calculate_averages(grades)

    write_averages('average_grades.csv', averages)
 
    print("Average grades calculated successfully:")
    for subject, avg in averages.items():
        print(f"{subject}: {avg:.2f}")

if __name__ == "__main__":
    main()











