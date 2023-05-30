var http = require('http').createServer(handler); //require http server, and create server with function handler()
var fs = require('fs'); //require filesystem module
var url = require('url');

var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
var LED = new Gpio(5, 'out'); //use GPIO pin 4 as output
var pushButton = new Gpio(17, 'in', 'both'); //use GPIO pin 17 as input, and 'both' button presses, and releases should be handled

http.listen(28080); //listen to port 28080

function handler (req, res) { //create server
  if (req.method === 'GET') {
    if (req.url == '/') {
      fs.readFile(__dirname + '/resources/web/menu.html', function(err, data) { //read file index.html in public folder
        if (err) {
          res.writeHead(404, {'Content-Type': 'text/html'}); //display 404 on error
          return res.end("404 Not Found");
        }
        res.writeHead(200, {'Content-Type': 'text/html'}); //write HTML
        res.write(data); //write data from index.html
        return res.end();
      });
    }

    else if (req.url == '/gen') {
      fs.readFile(__dirname + '/resources/web/makingPin.html', function(err, data) {
        if (err) {
          res.writeHead(404, {'Content-Type': 'text/html'});
          return res.end("404 Not Found");
        }
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
      });
    }

    else if (req.url == '/comp') {
      fs.readFile(__dirname + '/resources/web/typingPin.html', function(err, data) {
        if (err) {
          res.writeHead(404, {'Content-Type': 'text/html'});
          return res.end("404 Not Found");
        }
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
      });
    }

    else if (req.url == '/switch') {
      fs.readFile(__dirname + '/resources/web/index.html', function(err, data) {
        if (err) {
          res.writeHead(404, {'Content-Type': 'text/html'});
          return res.end("404 Not Found");
        }
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
      });
    }

    else if (req.url == '/on') {
      fs.readFile(__dirname + '/resources/web/gpio.html', function(err, data){
      LED.writeSync(1); //set pin state to 1 (turn LED on);
      res.writeHead(200, {'Content-Type': 'text/html'});
      console.log("led on");
      return res.end();
    });
    }
  

    else if (req.url == '/off') {
      fs.readFile(__dirname + '/resources/web/gpio.html', function(err, data){
      LED.writeSync(0); //set pin state to 1 (turn LED on);
      res.writeHead(200, {'Content-Type': 'text/html'});
      console.log("led off");
      return res.end();
    });
  }


  }

  else if (req.method === 'POST') {
    if (req.url == '/pininput') {
      let body = '';
        req.on('data', (chunk) => {
          body += chunk;
        });

        req.on('end', () => {
          try {
            const jsonData = JSON.parse(body);
            writeJSONToFile(jsonData);
            res.statusCode = 200;
            res.end('JSON data has been written to the file.');
          } catch (error) {
            res.statusCode = 400;
            res.end('Invalid JSON data.');
          }
        });
      } else {
        res.statusCode = 404;
        res.end('Not Found');

    }

    
  
  }
}

function writeJSONToFile(jsonData) {
  const filename = 'output.json';

  fs.writeFile(filename, JSON.stringify(jsonData, null, 2), (err) => {
    if (err) {
      console.error('Error writing JSON to file:', err);
    } else {
      console.log(`JSON data has been written to ${filename}`);
    }
  });
}


// function handler (req, res) { //create server
//   fs.readFile(__dirname + '/resources/web/menu.html', function(err, data) { //read file index.html in public folder
//     if (err) {
//       res.writeHead(404, {'Content-Type': 'text/html'}); //display 404 on error
//       return res.end("404 Not Found");
//     }
//     res.writeHead(200, {'Content-Type': 'text/html'}); //write HTML
//     res.write(data); //write data from index.html
//     return res.end();
//   });
// }
