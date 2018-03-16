/**
 * Created by zengzhi on 2018/3/16.
 */


const puppeteer = require('puppeteer');

(async () => {

    const browser = await puppeteer.launch({headless: false});
  //const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://www.baidu.com');

  await page.hover('.mnav')
  await page.screenshot({path: 'hover.png'});

  await browser.close();
})();