const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {

  mode: 'development',
  watch: true,
 
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm-bundler.js'
    }
  },

  plugins: [new MiniCssExtractPlugin({
    filename: './css/[name].css'
  })],
  
  entry: {
    main: path.resolve(__dirname, 'app/web/src/js/main.js'),
  },

  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [MiniCssExtractPlugin.loader,  'css-loader','postcss-loader', 'sass-loader'],
      },
    ],
  },

  output: {
    path: path.resolve(__dirname, 'app/web/assets'),
    filename: './js/[name].bundle.js',
  },
  
}