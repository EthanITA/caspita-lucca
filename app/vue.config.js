module.exports = {
  productionSourceMap: false,
  publicPath: process.env.NODE_ENV === 'production'
    ? '/lucca'
    : '/',
  pwa: {
    name: 'Caspita',
    themeColor: '#D777DD',
    msTileColor: '#FFFFFF',
    workboxOptions: {
      skipWaiting: true
    }
  },
}
