
## Notizen an sich selbst


eine weitere Notiz für mich!

## ToDos (offen)

```dataviewjs

let listTasks = dv.array([])

for(let x of dv.page("kilian").file.inlinks){
	
let text = dv.page(x).file.tasks.text

let tasks = dv.page(x).file.tasks
	.where(t => (t.subtasks == "") ? t.text.includes("[[kilian") :  (t.text.includes("[[kilian") || t.subtasks.some(d => d.text.includes("[[kilian"))
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
	.where(t => (t.subtasks == "") ? t.text.includes("[[kilian") :  (t.text.includes("[[kilian") || t.subtasks.some(d => d.text.includes("[[kilian"))
))
listTasks = listTasks.concat(tasks)
}	

if (listTasks.where(t => t.fullyCompleted) == "" ){
dv.paragraph("Es gibt noch keine abgeschlossene Aufgaben an dieser Stelle!")

}
else{dv.taskList(listTasks.where(t => t.fullyCompleted))}



```

