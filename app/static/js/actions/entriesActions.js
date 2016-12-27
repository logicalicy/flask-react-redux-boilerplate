import * as ActionTypes from '../constants/ActionTypes';

export const requestEntries = () => {
    return {
        type: ActionTypes.REQUEST_ENTRIES
    };
};

export const receiveEntries = (entries) => {
    return {
        type: ActionTypes.RECEIVE_ENTRIES,
        entries: entries
    };
};

export const fetchEntries = () => {
    return (dispatch) => {
        dispatch(requestEntries());
        fetch('/api/entries/')
            .then((response) => (response.json()))
            .then((responseJson) => {
                dispatch(receiveEntries(responseJson));
            });
    };
};
