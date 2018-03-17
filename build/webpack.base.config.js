const path = require('path');
const webpack = require('webpack');
const WebpackCleanupPlugin = require('webpack-cleanup-plugin');
const ProgressBarPlugin = require('progress-bar-webpack-plugin');
const make_hash = require('./hashmaker');

const NODE_ENV = process.env.NODE_ENV || 'development';

const PATH = path.join(__dirname, '..');


var isdev = NODE_ENV === 'development'
var hash = isdev ? '' : '-' + make_hash(20, 'webpack');


var config = {
    context: PATH,
    name: 'client',
    target: 'web',
    output: {
        path: isdev ? path.join(PATH, 'dist') : path.join(PATH, 'static'),
        publicPath: '/static/',
        filename: `js/[name]${hash}.js`,
        chunkFilename: `chunk/chunk-[id]${hash}.js`,
    },
    resolve: {
        extensions: ['.js', '.coffee'],
        alias: {
            '@src': path.join(PATH, 'src'),
        },
    },
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
    devtool: isdev ? 'eval-source-map' : false,
}



module.exports = config;
