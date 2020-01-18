import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

import { Provider } from "react-redux";
import store from "./store";

import AppControls from "./components/Controls.js";
import TripForm from "./components/TripForm.js";
import LandingScreen from "./components/LandingScreen.js";

function App() {
  return (
    <Provider store={store} className="h-100">
      <div className="App h-100">
        <AppControls />
        <LandingScreen />
        <TripForm />
      </div>
    </Provider>
  );
}

export default App;
