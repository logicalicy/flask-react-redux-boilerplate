import React from 'react';
import 'whatwg-fetch';
import { Provider } from 'react-redux';
import { render } from 'react-dom';
import store from './store/store';
import AppComponent from './components/AppComponent';
import '../sass/app.scss';

const App = (
    <Provider store={store}>
        <AppComponent />
    </Provider>
);

render(App, document.getElementById('root'));
