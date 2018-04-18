const WebSocket = require('ws');

const wsPort = 80;

const wss = new WebSocket.Server({ port: wsPort });
console.log("Websocket server listening on: " + wsPort);

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    if(message)
    console.log('received: %s', message);
      ws.send(JSON.stringify({'desc': "helloooooooo"}))
  });
  setTimeout(function(){
    ws.emit(testT, "hello!");
    console.log("sent hello!");
  }, 5000);
});
