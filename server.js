const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");

const carbon = require("./routes/api/getCarbon");

const app = express();

// Use routes
app.use("/api/carbon", carbon);

// Server static assets
console.log(process.env.NODE_ENV);
if (process.env.NODE_ENV === "production") {
  // Set static folder
  app.use(express.static("client/build"));

  app.get("*", (req, res) => {
    res.sendFile(path.resolve(__dirname, "client", "build", "index.html"));
  });
}

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server started on port ${port}`));
