
## Notizen an sich selbst




## ToDos (offen)

```dataviewjs

let listTasks = dv.array([])

for(let x of dv.page("paul").file.inlinks){
	
let text = dv.page(x).file.tasks.text

let tasks = dv.page(x).file.tasks
	.where(t => (t.subtasks == "") ? t.text.includes("[[paul") :  (t.text.includes("[[paul") || t.subtasks.some(d => d.text.includes("[[paul"))
))
listTasks = listTasks.concat(tasks)
}	
if (listTasks.where(t => !t.fullyCompleted) == "" ){
dv.paragraph("Es gibt keine offenen Aufgaben an dieser Stelle!")

}
else{dv.taskList(listTasks.where(t => !t.fullyCompleted))}


```
## ToDos (abgeschlossen)
```dataviewjs
let listTasks = dv.array([])

for(let x of dv.current().file.inlinks){
	
let text = dv.page(x).file.tasks.text

let tasks = dv.page(x).file.tasks
	.where(t => (t.subtasks == "") ? t.text.includes("[[paul") :  (t.text.includes("[[paul") || t.subtasks.some(d => d.text.includes("[[paul"))
))
listTasks = listTasks.concat(tasks)
}	

if (listTasks.where(t => t.fullyCompleted) == "" ){
dv.paragraph("Es gibt noch keine abgeschlossene Aufgaben an dieser Stelle!")

}
else{dv.taskList(listTasks.where(t => t.fullyCompleted))}



```

