var http = require('http');

http.createServer((req,res) => {
    res.writeHead(505, {'Content-Type': 'text/plain'});
    res.end('Hello world');
}).listen(8080);

