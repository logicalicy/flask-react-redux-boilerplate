var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    context: __dirname + '/app/static/js',
    entry: {
        app: './app.js',
    },
    output: {
        filename: 'app.js',
        path: __dirname + '/app/static/dist',
        publicPath: 'http://localhost:8080/',
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loaders: [
                    'react-hot',
                    'babel-loader?presets[]=react&presets[]=es2015&presets[]=stage-1'
                ]
            },
            {
                test: /\.scss$/,
                exclude: /node_modules/,
                loader: ExtractTextPlugin.extract(
                    'style',
                    'css?sourceMap!sass'
                )
            }
        ],
    },
    plugins: [
        new ExtractTextPlugin('[name].css'),
    ],
};
