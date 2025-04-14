function loadTasks() {
    fetch('/tasks')
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById('taskList');
            ul.innerHTML = '';
            data.forEach(task => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <span class="task-title">${task[2]}</span>
                    <button class="task-delete" onclick="deleteTask(${task[0]})">Delete</button>
                `;
                ul.appendChild(li);
            });
        });
}

function deleteTask(taskId) {
    fetch(`/task/${taskId}`, {
        method: 'DELETE'
    })
    .then(() => loadTasks());
}
