# To-Do-List
Este programa es una aplicación sencilla de lista de tareas (To-Do List) construida en Python. Usa Tkinter para crear una interfaz gráfica de usuario y MySQL para almacenar las tareas en una base de datos.

### Funcionalidades Clave
- **Añadir Tareas**: Los usuarios pueden agregar nuevas tareas a la lista mediante un campo de entrada y un botón.
- **Actualizar Estado**: Al marcar una tarea como completada, esta se actualiza en la base de datos a "completed", pero no se elimina realmente, manteniendo un registro histórico.
- **Interfaz Gráfica**: La aplicación muestra las tareas pendientes en una ventana, permitiendo una fácil interacción y gestión visual de las tareas.

### Seguridad
Para mantener la seguridad de las credenciales de la base de datos, el programa utiliza variables de entorno para cargar de manera segura el usuario y la contraseña, evitando exponer esta información sensible en el código fuente.

### Uso
Ideal para demostraciones en portafolios, este proyecto destaca habilidades en la creación de interfaces gráficas, manejo de bases de datos, y buenas prácticas de seguridad en el desarrollo de software.
