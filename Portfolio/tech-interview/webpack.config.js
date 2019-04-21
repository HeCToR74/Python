const webpack = require('webpack');
const path = require('path');
const Dotenv = require('dotenv-webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

const config = {
    entry:   path.join(__dirname, 'techinterview/static/src/app.js'),
    output: {
        path: path.join(__dirname,'techinterview/static/public'),
        filename: 'bundle.js'
    },
    resolve: {
        alias: {
            src: path.join(__dirname, 'techinterview/static/src'),
        }
    },
    module: {
        loaders: [
            {
                test: /\.js?/,
                include: path.join(__dirname, 'techinterview/static/'),
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['es2015', 'react'],
                    plugins:[ 'transform-object-rest-spread' ]
                }
            },
            {
                test: /\.less$/,
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    use: ['css-loader', 'less-loader']
                })
            },
            {
              test: /.css$/, loader: "css-loader" },

            {
                test: /\.(jpe?g|png|gif|svg)$/i,
                loader: 'file-loader'
            },
            {
                test: /\.jsx$/,
                exclude: /node_modules/,
                loader: "eslint-loader",
            },
        ]
    },
    plugins:[
        new ExtractTextPlugin({
            filename: 'style.css',
            disable: false,
            allChunks: true
        }),
      new Dotenv({path: '.env'})
    ],
};

module.exports = config;
