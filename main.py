from mindmap.manager import search_node, delete_node, list_nodes
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
    print(f"1. 🔙 Go back")
    print(f"2. 💾 Save the MindMap")
    print(f"3. 🔍 Find path of a node")
    print(f"4. 🔍 Display tree")
    print(f"5. 🗑️ Delete a node")
    print(f"6. ❌ Exit")

    for idx, child in enumerate(current_node.children, start=1):
        print(f"{idx + 6}. 📂 {child.name}")



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
        elif choice == 1:
            if len(history) > 0:
                current_node = history.pop()
            else:
                print("❗ You are already at the root.")

        elif choice == 2:
            filename = input("Enter filename to save (YAML): ").strip()
            if filename:
                save_mindmap(root_node, filename)
                print(f"✅ MindMap saved to '{filename}'.")
            else:
                print("❗ Filename cannot be empty.")

        elif choice == 3:
            node_name = input("Enter node to find from here: ").strip()
            print(search_node(current_node, node_name))

        elif choice == 4:
            print(list_nodes(current_node, ''))

        elif choice == 5:
            node_to_delete = input("Which node you want to delete ? : ").strip()
            cleaned_list = delete_node(current_node,node_to_delete)
            if cleaned_list is not None:
                current_node.children = cleaned_list
            else:
                print("❗ Couldn't found any node with this name")


        elif choice == 6:
            print("👋 Goodbye!")
            break

        elif choice <= (len(current_node.children) + 7):
            selected_child = current_node.children[choice - 7]
            history.append(current_node)
            current_node = selected_child

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
