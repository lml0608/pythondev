/**
 * Created by zengzhi on 2018/3/16.
 */


const viewPort = { width: 1280, height: 800 }
const options = {
  path: 'clipped_stocktickers.png',
  fullPage: false,
  clip: {
    x: 0,
    y: 240,
    width: 1000,
    height: 100
  }
}

const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({headless: false})
  const page = await browser.newPage()
  await page.setViewport(viewPort)
  await page.goto('https://www.baidu.com')
  await page.screenshot(options)
  await browser.close()
})()