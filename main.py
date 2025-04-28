from mindmap.models import Node
from mindmap.storage import save_mindmap, load_mindmap

def choose_start():
    print("\nWelcome to MindMap CLI 🌟")
    print("1. Create a new MindMap")
    print("2. Load a MindMap from a file")
    print("0. Exit")
    return input("Choice: ").strip()

def show_menu(current_node):
    print(f"\n📍 You are at: {current_node.name}")
    print("0. ➕ Add a new idea here")

    for idx, child in enumerate(current_node.children, start=1):
        print(f"{idx}. 📂 {child.name}")

    print(f"{len(current_node.children)+1}. 🔙 Go back")
    print(f"{len(current_node.children)+2}. 💾 Save the MindMap")
    print(f"{len(current_node.children)+3}. 🔍 Find path of a node")
    print(f"{len(current_node.children)+4}. ❌ Exit")

def navigation_menu(root_node):
    current_node = root_node
    history = []

    while True:
        show_menu(current_node)
        choice = input("\nEnter your choice: ").strip()

        try:
            choice = int(choice)
        except ValueError:
            print("❗ Please enter a number.")
            continue

        if choice == 0:
            new_name = input("Name of the new idea: ").strip()
            if new_name:
                new_node = Node(new_name, [])
                current_node.children.append(new_node)
                print(f"✅ Idea '{new_name}' added.")
            else:
                print("❗ Idea name cannot be empty.")

        elif 1 <= choice <= len(current_node.children):
            selected_child = current_node.children[choice - 1]
            history.append(current_node)
            current_node = selected_child

        elif choice == len(current_node.children) + 1:
            if len(history) > 0:
                current_node = history.pop()
            else:
                print("❗ You are already at the root.")

        elif choice == len(current_node.children) + 2:
            filename = input("Enter filename to save (YAML): ").strip()
            if filename:
                save_mindmap(root_node, filename)
                print(f"✅ MindMap saved to '{filename}'.")
            else:
                print("❗ Filename cannot be empty.")

        elif choice == len(current_node.children) + 3:
            print("👋 Goodbye!")
            break

        elif choice == len(current_node.children) + 4:
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid choice.")

def main():

    while True:
        action = choose_start()

        if action == "1":
            title = input("Enter title for the new MindMap: ").strip()
            if title:
                root_node = Node(title, [])
                break
            else:
                print("❗ Title cannot be empty.")

        elif action == "2":
            filename = input("Enter filename to load (YAML): ").strip()
            try:
                root_node = load_mindmap(filename)
                break
            except Exception as e:
                print(f"❌ Error loading file: {e}")

        elif action == "0":
            print("👋 Goodbye!")
            return

        else:
            print("❗ Invalid choice.")

    navigation_menu(root_node)

if __name__ == "__main__":
    main()
