# 🧠 MindMap CLI with python

A command-line tool to **create and explore mind maps** directly in your terminal.

---

## ⚙️ Installation

1. **Clone the project** (if not already done):

   ```bash
   git clone <REPO_URL>
   cd project_name
   
2. **Install requirements**:
   ```bash
   pip install -r requirements.txt

3. **Run the CLI**:
   ```bash
   python main.py
   
---

## 🚀 How It Works
Once the CLI starts, you’ll be greeted with a menu to:

Create a new MindMap

Load a MindMap from a YAML file

Exit the program

---

## 🧭 MindMap Navigation
After creating or loading a mind map, you can interact with it through the following options:

0 ➕ Add a new idea to the current node (max. 3 children)

1 🔙 Go back to the previous node

2 💾 Save the current MindMap to a file

3 🔍 Find the path to a specific node by name

4 🌳 Display the full tree from the current node

5 ✏️ Edit a node’s name

6 🗑️ Delete a node

7 ❌ Exit the program

8+ 📂 Navigate to a child node

The navigation is interactive, and you always see your position and available options.

---

## 📁 MindMap Storage
MindMaps are saved as .yml files using a simple YAML structure.

You can load existing maps anytime to continue editing or exploring.

---

## 🛠 Project Structure
main.py – the entry point and user interface

mindmap/models.py – defines the Node class

mindmap/manager.py – handles logic like editing, deleting, and searching nodes

mindmap/storage.py – manages loading/saving to YAML files

---

## 🚧 Notes
Each node can have up to 3 children.

The interface is fully interactive and text-based.

Make sure to save regularly to avoid losing progress.
