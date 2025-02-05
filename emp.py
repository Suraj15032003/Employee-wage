import random

def emp_attendance():
    return random.choice([0, 1])  # 0 for absent, 1 for present

def calculate_wages():
    worktype = random.randint(0, 2)  # 0: No work, 1: Part-time, 2: Full-time
    part_time_hours = 4
    full_time_hours = 8
    wages_per_hour = 20
    total_hours = 0
    total_wages = 0

    if emp_attendance() == 1:
        if worktype == 1:
            total_hours = part_time_hours
            total_wages = part_time_hours * wages_per_hour
        elif worktype == 2:
            total_hours = full_time_hours
            total_wages = full_time_hours * wages_per_hour
        else:
            total_hours = 0
            total_wages = 0
    else:
        total_hours = 0
        total_wages = 0

    print(f"Hours Worked: {total_hours}")
    print(f"Total Wage: ${total_wages}")

# Example usage
if __name__ == "__main__":
    calculate_wages()
