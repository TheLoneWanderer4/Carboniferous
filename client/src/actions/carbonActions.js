import axios from "axios";

import { REQUEST_CARBON, ITEMS_LOADING, GET_MAP } from "./types.js";

export const requestCarbon = state => dispatch => {
  // use the app based on the input, set payload to the list of objects
  dispatch(setItemsLoading());
  console.log("Submit Successful");
  axios
    .post("/api/carbon", state)
    .then(res => dispatch({ type: REQUEST_CARBON, payload: res.data }));
};

export const requestMap = req => dispatch => {
  console.log(req);
  axios
    .post("/api/carbon/map", req)
    .then(res => dispatch({ type: GET_MAP, payload: res.data.link }));
};

export const setItemsLoading = () => {
  return { type: ITEMS_LOADING };
};
