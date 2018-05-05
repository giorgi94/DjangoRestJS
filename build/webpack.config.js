// const path = require("path");
const webpack = require("webpack");
const merge = require("webpack-merge");
const baseConfig = require("./config/webpack.base.config.js");

const WatchLiveReloadPlugin = require("webpack-watch-livereload-plugin");

var entry = {
    main: "./src/js/main.js",
};


var clientConfig = merge(baseConfig, {
    entry: Object.assign({
        vendor: ["babel-polyfill", "axios"]
    }, entry),
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: ["common", "vendor"]
        }),
        new WatchLiveReloadPlugin({
            files: [
                "./dist/**/*.js",
                "./dist/**/*.css",
                "./templates/jinja2/pages/*.html",
            ]
        }),
    ]
});

module.exports = clientConfig;
