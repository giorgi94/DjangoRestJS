const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');
const baseConfig = require('./webpack.base.config.js');


var entry = {
    main: './src/js/main.js',
    admin: './src/js/admin.js',
}




var clientConfig = merge(baseConfig, {
    entry,
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: ['common', 'vendor']
        }),
    ]
})

module.exports = clientConfig;
