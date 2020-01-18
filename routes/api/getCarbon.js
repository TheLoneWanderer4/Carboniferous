const express = require("express");
const router = express.Router();

let { PythonShell } = require("python-shell");

// @route GET api/items
// @desc Get All Items
// @access Public

router.post("/", (req, res) => {
  let options = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    args: [JSON.stringify(req.body)]
  };

  PythonShell.run("backend/testTheThing.py", options, function(err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log(JSON.parse(results[1]));
    res.json(JSON.parse(results[1]));
  });
});

module.exports = router;
