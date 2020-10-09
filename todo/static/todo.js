

var cdEl = document.getElementById('cd')

var today = new Date()
var date = ` ${today.getMonth() + 1}-${today.getDate()}-${today.getFullYear()}`

cdEl.textContent = date

