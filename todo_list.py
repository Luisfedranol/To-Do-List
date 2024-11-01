import mysql.connector
from tkinter import *
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener credenciales de la base de datos desde las variables de entorno
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Conexión a la base de datos MySQL
mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# Funciones de la aplicación
def add_task():
    task = task_entry.get()
    if task:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        mydb.commit()
        task_entry.delete(0, END)
        fetch_tasks()

def delete_task(task_id):
    cursor = mydb.cursor()
    cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = %s", (task_id,))
    mydb.commit()
    fetch_tasks()

def fetch_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM tasks WHERE status != 'completed'")
    for (task_id, task, status) in cursor:
        task_label = Label(task_frame, text=task)
        task_label.pack()
        delete_button = Button(task_frame, text="Eliminar", command=lambda task_id=task_id: delete_task(task_id))
        delete_button.pack()

# Interfaz gráfica con Tkinter
root = Tk()
root.title("Lista de Tareas")
task_frame = Frame(root)
task_frame.pack()
task_entry = Entry(root, width=50)
task_entry.pack()
add_button = Button(root, text="Añadir Tarea", command=add_task)
add_button.pack()
fetch_tasks()
root.mainloop()
