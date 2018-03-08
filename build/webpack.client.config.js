const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');
const baseConfig = require('./webpack.base.config.js');
const { gHash } = require('./hashGenerate');

const NODE_ENV = process.env.NODE_ENV || 'development';

const PATH = path.join(__dirname, '..');
const DIST_DIR = path.join(PATH, 'dist');

var entry = {
    main: './src/js/main.js',
    admin: './src/js/admin.js',
}

var hash = NODE_ENV === 'development' ? 'dev' : gHash(20, 'webpack');


var clientConfig = merge(baseConfig, {
    context: PATH,
    name: 'client',
    target: 'web',
    entry,
    output: {
        path: path.join(PATH, 'dist'),
        publicPath: '/static/',
        filename: `js/[name].bundle.${hash}.js`,
        chunkFilename: `chunk/[id].bundle.${hash}.js`,
    },
    resolve: {
        extensions: ['.js', '.coffee'],
        alias: {
            '@src': path.join(PATH, 'src'),
        },
    },
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: ['common', 'vendor']
        }),
    ]
})

module.exports = clientConfig;
