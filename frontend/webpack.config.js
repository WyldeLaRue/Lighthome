const webpack = require('webpack');
const config = {
    entry:  __dirname + '/src/index.jsx',
    output: {
        path: __dirname + '/static/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
        {
          test: /\.jsx?/,
          exclude: /node_modules/,
          use: 'babel-loader'
        },
        {
          test:/\.css$/,
          exclude: /node_modules/,
          use:['style-loader','css-loader']
        }
      ]
    }
};
module.exports = config;


