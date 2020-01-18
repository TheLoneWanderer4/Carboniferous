import { combineReducers } from "redux";
import itemReducer from "./carbonReducer";

export default combineReducers({
  item: itemReducer
});
