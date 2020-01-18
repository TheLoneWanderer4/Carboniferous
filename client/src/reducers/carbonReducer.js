import { REQUEST_CARBON, ITEMS_LOADING } from "../actions/types.js";

const initialState = {
  paths: [],
  loading: false
};

export default (state = initialState, action) => {
  switch (action.type) {
    case REQUEST_CARBON:
      return {
        ...state,
        paths: action.payload
      };

    case ITEMS_LOADING:
      return {
        ...state,
        loading: true
      };

    default:
      return state;
  }
};
