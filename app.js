const fs = require('fs');

try { 
    const data = fs.readFileSync('data.json','utf8');
    const jsonData = JSON.parse(data);

    console.log(jsonData);
} catch (err) {
    console.error(err);
}