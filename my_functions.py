def estimate_max_hr(age_years: int, sex: str) -> int:
    """
    See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
    """
    if sex == "male":
        max_hr_bpm = 223 - 0.9 * age_years
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 * age_years
    else:
        # The input() opens a prompt for the user to enter maximum heart rate
        max_hr_bpm = input("Enter maximum heart rate:")
    return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    person_info = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "estimate_max_hr": estimate_max_hr(age, sex),
    }
    return person_info

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    experiment_info = {
        "experiment_name": experiment_name,
        "date": date,
        "supervisor": supervisor,
        "subject": subject,
    }
    return experiment_info