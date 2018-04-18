const WebSocket = require('ws');

const wsPort = 8080;

const wss = new WebSocket.Server({ port: wsPort });
console.log("Websocket server listening on: " + wsPort);

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    if(message)
    console.log('received: %s', message);
  });
  while(true){
    ws.send(JSON.stringify({'desc': "helloooooooo"}))
  }
});
