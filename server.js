const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");

const carbon = require("./routes/api/getCarbon");

const app = express();
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: true }));

// Use routes
app.use("/api/carbon", carbon);

// Server static assets
if (process.env.NODE_ENV !== "production") {
  // Set static folder
  app.use(express.static("client/build"));

  console.log("in production");

  app.get("*", (req, res) => {
    res.sendFile(path.resolve(__dirname, "client", "build", "index.html"));
  });
}

const port = 5000;

app.listen(port, () => console.log(`Server started on port ${port}`));
