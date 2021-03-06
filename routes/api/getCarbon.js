const express = require("express");
const router = express.Router();
const fs = require("fs");
let { PythonShell } = require("python-shell");

// @route GET api/items
// @desc Get All Items
// @access Public

router.post("/", (req, res) => {
  let options = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    args: []
  };

  fs.writeFile(
    "/var/www/Carboniferous/backend/input.json",
    JSON.stringify(req.body, null, 2),
    err => {
      if (err) throw error;
      console.log("saved file");
    }
  );

  PythonShell.run("backend/main.py", options, function(err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution

    console.log("Got results");

    for (var i = 0; i < results.length; i++) {
      results[i] = JSON.parse(results[i].replace(/'/g, '"'));
    }

    res.json(results);
  });
});

router.post("/map", (req, res) => {
  let options = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    args: [req.body.start, req.body.end, req.body.mode]
  };

  PythonShell.run("backend/map_link.py", options, function(err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    res.json({ link: results });
  });
});

module.exports = router;
