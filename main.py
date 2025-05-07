def fitness_tracker():
    print("🏋️ Welcome to the Gym Fitness Tracker! 🏋️")
    workout_log = []

    while True:
        workout = input("\nEnter workout name (or type 'done' to finish): ").strip()
        if workout.lower() == 'done':
            break

        try:
            sets = int(input("Enter number of sets: "))
            reps = int(input("Enter number of reps per set: "))
            weight = float(input("Enter weight used (kg): "))
        except ValueError:
            print("Invalid input! Please enter numeric values for sets, reps, and weight.")
            continue

        workout_log.append({
            'Workout': workout,
            'Sets': sets,
            'Reps': reps,
            'Weight (kg)': weight
        })

    print("\n📋 Your Workout Summary:")
    for entry in workout_log:
        print(f"• {entry['Workout']} - {entry['Sets']} sets × {entry['Reps']} reps @ {entry['Weight (kg)']} kg")

if __name__ == "__main__":
    fitness_tracker()
