import random

# Constants
TOTAL_WORKING_HOURS = 100
WORKING_DAYS_PER_MONTH = 20
EMP_WAGE_PER_HOUR = 20
IS_FULL_TIME = 2
IS_PART_TIME = 1

def emp_attendance():
    """
    Determines employee attendance randomly.
    Returns:
        int: 0 if absent, 1 if present.
    """
    try:
        return random.choice([0, 1])  # 0 for absent, 1 for present
    except Exception as e:
        print(f"Error in emp_attendance(): {e}")
        return 0  # Default to absent in case of error

def calculate_daily_wage():
    """
    Calculates the daily wage of an employee based on work type.
    Returns:
        tuple: (total_hours, total_wages)
    """
    try:
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

        return total_hours, total_wages

    except Exception as e:
        print(f"Error in calculate_daily_wage(): {e}")
        return 0, 0  # Default to zero hours and wages

def calculate_wages_until_limit(max_hours=100, max_days=20):
    """
    Calculates the total wages and hours worked until the limit of hours or days is reached.
    """
    try:
        total_hours = 0
        total_wages = 0
        days_worked = 0

        while total_hours < max_hours and days_worked < max_days:
            daily_hours, daily_wage = calculate_daily_wage()
            total_hours += daily_hours
            total_wages += daily_wage
            days_worked += 1

        print(f"Total Hours Worked: {total_hours}")
        print(f"Total Wages Earned: {total_wages}")
        print(f"Total Days Worked: {days_worked}")

    except Exception as e:
        print(f"Error in calculate_wages_until_limit(): {e}")

if __name__ == "__main__":
    calculate_wages_until_limit()
