import os

# 👇 Set your project folder here
PROJECT_DIR = "PYthon_Project"

# Create the folder automatically if it doesn't exist
os.makedirs(PROJECT_DIR, exist_ok=True)

def create_file(filename):
    try:
        file_path = os.path.join(PROJECT_DIR, filename)  # ✅ always inside python_project
        with open(file_path, 'x') as f:
            print(f"✅ File '{filename}' created inside '{PROJECT_DIR}'!")
    except FileExistsError:
        print(f"⚠️ File '{filename}' already exists in '{PROJECT_DIR}'!")
    except Exception as e:
        print(f"❌ Error: {e}")

def view_all_files():
    print(f"\n📂 Files inside '{PROJECT_DIR}':")
    files = os.listdir(PROJECT_DIR)
    if not files:
        print("   (No files found)")
    else:
        for f in files:
            print(f"   📄 {f}")

def delete_file(filename):
    try:
        file_path = os.path.join(PROJECT_DIR, filename)
        os.remove(file_path)
        print(f"🗑️ File '{filename}' deleted from '{PROJECT_DIR}'.")
    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found in '{PROJECT_DIR}'.")
    except Exception as e:
        print(f"❌ Error: {e}")

def read_file(filename):
    try:
        file_path = os.path.join(PROJECT_DIR, filename)
        with open(file_path, 'r') as f:
            content = f.read()
            print(f"\n📖 Content of '{filename}':\n{'-'*30}\n{content}\n{'-'*30}")
    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found in '{PROJECT_DIR}'.")
    except Exception as e:
        print(f"❌ Error: {e}")

def edit_file(filename):
    try:
        file_path = os.path.join(PROJECT_DIR, filename)
        with open(file_path, 'a') as f:
            content = input("✍️ Enter text to add: ")
            f.write(content + "\n")
            print(f"✅ Content added to '{filename}' in '{PROJECT_DIR}'.")
    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found in '{PROJECT_DIR}'.")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    while True:
        print("\n=== FILE MANAGEMENT APP ===")
        print("1️⃣  Create file")
        print("2️⃣  View all files")
        print("3️⃣  Delete file")
        print("4️⃣  Read file")
        print("5️⃣  Edit file")
        print("6️⃣  Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            filename = input("Enter filename to create: ").strip()
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter filename to delete: ").strip()
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter filename to read: ").strip()
            read_file(filename)
        elif choice == '5':
            filename = input("Enter filename to edit: ").strip()
            edit_file(filename)
        elif choice == '6':
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid input, please enter 1–6.")

if __name__ == "__main__":
    main()
