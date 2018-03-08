const path = require('path');
const webpack = require('webpack');
const WebpackCleanupPlugin = require('webpack-cleanup-plugin');
const ProgressBarPlugin = require('progress-bar-webpack-plugin');

const NODE_ENV = process.env.NODE_ENV || 'development';

var config = {
    module: {
        rules: [
            {
                test: /\.js$/,
                use: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.coffee$/,
                use: ['babel-loader','coffee-loader'],
                exclude: /node_modules/
            },
        ]
    },
    plugins: [
        new ProgressBarPlugin(),
        new WebpackCleanupPlugin({
            exclude: ["img/*", 'fonts/*', 'css/*'],
        }),
        new webpack.DefinePlugin({
            'NODE_ENV': JSON.stringify(NODE_ENV),
            'process.env.NODE_ENV': JSON.stringify(NODE_ENV),
            'PRODUCTION': JSON.stringify(NODE_ENV!=='development'),
        }),
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: NODE_ENV == 'development',
            compress: {
                warnings: false
            }
        }),
        new webpack.optimize.ModuleConcatenationPlugin(),
        new webpack.LoaderOptionsPlugin({
            minimize: true
        }),
    ],
    devtool: NODE_ENV == 'development' ? 'eval-source-map' : false,
}



module.exports = config;
