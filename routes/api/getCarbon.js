const express = require("express");
const router = express.Router();

// @route GET api/items
// @desc Get All Items
// @access Public

var exampleBody = {
  start: "TUS",
  end: "DNV",
  priceMax: "100",
  maxTravelTime: "100",
  modes: {
    train: true,
    car: true,
    bus: true
  }
};

router.get("/", (req, res) => {
  console.log(req.body);
  res.json({ good: true });
});

module.exports = router;
