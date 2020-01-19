import { REQUEST_CARBON, ITEMS_LOADING, GET_MAP } from "../actions/types.js";

const initialState = {
  paths: [],
  link: "",
  loading: false
};

export default (state = initialState, action) => {
  switch (action.type) {
    case REQUEST_CARBON:
      console.log(action.payload);
      return {
        ...state,
        paths: action.payload,
        loading: false
      };

    case GET_MAP:
      return { ...state, link: action.payload };

    case ITEMS_LOADING:
      return {
        ...state,
        loading: true
      };

    default:
      return state;
  }
};
