

var cdEl = document.getElementById('cd')

var today = new Date()
var date = ` 0${today.getMonth() + 1}-${today.getDate()}-${today.getFullYear()}`

cdEl.textContent = date

