import * as ActionTypes from '../constants/ActionTypes';

const initialState = {
    entries: [],
    isFetching: false
};

const EntriesReducer = (state = initialState, action) => {
    switch (action.type) {
        case ActionTypes.REQUEST_ENTRIES:
            return {
                ...state,
                isFetching: true
            };
        case ActionTypes.RECEIVE_ENTRIES:
            return {
                ...state,
                entries: action.entries,
                isFetching: false
            };
        default:
            return state;
    }
};

export default EntriesReducer;