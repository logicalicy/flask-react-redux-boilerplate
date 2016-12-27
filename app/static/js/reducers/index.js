import { combineReducers } from 'redux';
import EntriesReducer from './EntriesReducer';

const reducers = combineReducers({
    entries: EntriesReducer
});

export default reducers;