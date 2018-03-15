/**
 * Created by zengzhi on 2018/3/15.
 */


const puppeteer = require('puppeteer');

//
// let timeout = function (delay) {
//      return new Promise((resolve, reject) => {
//            setTimeout(() => {
//                   try {
//                       resolve(1)
//                   } catch (e) {
//                       reject(0)
//                    }
//            }, delay);
//      })
// }



(async () => {

    const browser = await puppeteer.launch({headless: false});
  //const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://portaltest.wgmf.com/wgmfjz/index.html');
    const title = await page.title()

    console.log(title)

    await page.screenshot({path: 'baidu.png'});

    //await timeout(3000);

    await

    await browser.close();

})()