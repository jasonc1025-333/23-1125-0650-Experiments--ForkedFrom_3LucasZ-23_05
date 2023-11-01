//SETUP
//enable websocket
var socket = io();

//LISTENERS
socket.on('connect', function(){
    console.log('connected');
});

socket.on('disconnect', function(){
    console.log('disconnected');
});

//SENDERS
//button presses

function digDown(){
    socket.emit('digDown');
}

function digUp(){
    socket.emit('digUp');
}

function armDown(){
    socket.emit('armDown');
}

function armUp(){
    socket.emit('armUp');
}

function toggleLaser(){
    socket.emit('toggleLaser')
}