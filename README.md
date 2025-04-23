# ✅ Task Tracker CLI

A lightweight and easy-to-use **Command-Line Interface (CLI)** tool for managing your daily tasks!  
Built with Python, this simple task tracker lets you **add**, **list**, **complete**, and **delete** tasks using just a few commands.

---

## 🧩 Features

- 🆕 Add new tasks with descriptions and due dates
- 📋 List all tasks in a neat format
- ✅ Mark tasks as completed
- 🗑️ Remove completed or irrelevant tasks
- 💾 Tasks are saved in a `tasks.json` file
- 🔄 Option to reset the task list

---

## 📁 Project Folder Structure

```
task_tracker/
│
├── main.py # CLI entry point
├── task_manager.py # Functions to add, viewm delete, mark complete
├── storage.py # Functions to read/write JSON file
 tasks.json # Stores task data
├── README.md # Instructions & how to run
├── .gitignore
├── demo # output images data
└── requirements.txt
```

---

## 🚀 Getting Started

Follow these simple steps to set up and start using the Task Tracker CLI.

### 1. Clone the repository

```bash
git clone https://github.com/r1tikpatil/task-tracker-cli.git
```

### ✅ 2. Navigate to Project Folder

```bash
cd task-tracker-cli
```

### 🐍 3. Set Up Virtual Environment

```bash
python -m venv venv
```

```bash
source venv/bin/activate # For Linux/Mac
# OR
venv\Scripts\activate # For Windows
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### ⚙️ 5. Run the CLI App

#### 🆕 Add a Task

```bash
python main.py add "Buy groceries" --description "Milk, eggs, bread" --due "2025-04-25"
```

#### 📋 List Tasks

```bash
python main.py list
```

#### ✅ Mark Task as Completed

```bash
python main.py complete 1
```

#### 🗑️ Delete Task

```bash
python main.py delete 1
```

### 🧼 6. (Optional) Reset Task File

```bash
echo "[]" > tasks.json
```

---

## 🖼️ Demo / Screenshot

![alt text](demo/image-2.png)

![alt text](demo/image-3.png)

![alt text](demo/image.png)

![alt text](demo/image-4.png)

---
