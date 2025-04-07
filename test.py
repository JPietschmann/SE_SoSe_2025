from my_classes import Subject, Supervisor, Experiment


if __name__ == "__main__":
    # Erstellen eines Leistungstests
    supervisor = Supervisor("Julia Pietschmann")
    subject = Subject("Timo", "Sieg", 27, "male")
    subject.estimate_max_hr()
    experiment = Experiment("Test: 1", "2025-04-07")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)
    print(experiment)