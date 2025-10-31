def task_manager():
    tasks = []
    print('------ Welcome to Task Management App ------')

    # Step 1: Ask how many tasks to add
    while True:
        try:
            total_task = int(input('Enter how many tasks you want to add: '))
            if total_task < 0:
                print("⚠️ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    # Step 2: Get all tasks in one input
    if total_task > 0:
        raw = input(f'Enter your {total_task} task(s), separated by commas: ').strip()
        all_entered = [t.strip() for t in raw.split(',') if t.strip()]

        # If entered fewer than expected, pad with manual entry
        if len(all_entered) < total_task:
            print(f"⚠️ You entered only {len(all_entered)} tasks. Please enter the remaining ones manually:")
            for i in range(len(all_entered) + 1, total_task + 1):
                t = input(f'Enter task {i}: ').strip()
                if t:
                    all_entered.append(t)

        tasks = all_entered
    else:
        print("📭 No initial tasks added.")

    print("\n✅ Today's tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"   {i}. {t}")

    # Step 3: Main menu loop
    while True:
        print("\n--- Task Operations ---")
        print("1️⃣  Add Task(s)")
        print("2️⃣  Update Task")
        print("3️⃣  Delete Task")
        print("4️⃣  View All Tasks")
        print("5️⃣  Exit")

        try:
            operation = int(input('Enter your choice (1–5): '))
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1–5.")
            continue

        # Add task(s)
        if operation == 1:
            add = input('Enter new task(s) separated by commas: ').strip()
            new_tasks = [t.strip() for t in add.split(',') if t.strip()]
            if not new_tasks:
                print("⚠️ No valid task entered.")
            else:
                for t in new_tasks:
                    if t in tasks:
                        print(f"⚠️ Task '{t}' already exists, skipped.")
                    else:
                        tasks.append(t)
                        print(f"✅ Task '{t}' added successfully!")

        # Update task
        elif operation == 2:
            if not tasks:
                print("📭 No tasks to update.")
                continue

            print("\n📋 Current Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"   {i}. {t}")

            update_val = input('Enter the task you want to update: ').strip()
            if update_val in tasks:
                up = input('Enter new task: ').strip()
                if up:
                    ind = tasks.index(update_val)
                    tasks[ind] = up
                    print(f"🔁 Task updated to: '{up}'")
                else:
                    print("⚠️ Cannot update with an empty task!")
            else:
                print(f"⚠️ Task '{update_val}' not found!")

        # Delete task
        elif operation == 3:
            if not tasks:
                print("📭 No tasks to delete.")
                continue

            print("\n📋 Current Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"   {i}. {t}")

            del_val = input('Enter the task you want to delete: ').strip()
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"🗑️ Task '{del_val}' deleted successfully.")
            else:
                print(f"⚠️ Task '{del_val}' not found!")

        # View all tasks
        elif operation == 4:
            if tasks:
                print("\n📋 Your Current Tasks:")
                for i, t in enumerate(tasks, start=1):
                    print(f"   {i}. {t}")
            else:
                print("📭 No tasks available!")

        # Exit
        elif operation == 5:
            print("👋 Closing the program... Goodbye!")
            break

        # Invalid choice
        else:
            print("❌ Invalid choice! Please select between 1–5.")


# Run the app
if __name__ == "__main__":
    task_manager()
