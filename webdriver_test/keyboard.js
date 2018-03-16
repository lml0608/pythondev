/**
 * Created by zengzhi on 2018/3/16.
 */
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch()
  const page = await browser.newPage()
  await page.goto('https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#pdf')
  // await page.focus('trix-editor')
  // await page.keyboard.type('Just adding a title')
  await page.pdf({ path: 'keyboard.pdf' })
  await browser.close()
})()