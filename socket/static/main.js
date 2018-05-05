var socket = io.connect('http://127.0.0.1:5000/')

socket.on('connect', ()=>{
    socket.send('User is connected!')
})

socket.on('message', (msg)=>{
    message.innerHTML += `<li>${msg}</li>`
})

btn.addEventListener('click', ()=>{
    socket.send(mymsg.value)
    mymsg.value = ""
})
