/**
 * Created by zengzhi on 2018/3/15.
 */

const cookie = {
    name: 'customerId',
    value: '16788112',
    domain: 'test.wgmf.com',
    url: 'https://test.wgmf.com',
    path: '/',
    httpOnly: true,
    secure: true
};

const puppeteer = require('puppeteer');

const devices = require('puppeteer/DeviceDescriptors')


const screenshot = 'github.png';




(async () => {

    const browser = await puppeteer.launch({headless: false})

    const page = await browser.newPage()
    await page.setCookie(cookie)

    await page.emulate(devices['iPhone 6'])
    await page.goto('http://test.wgmf.com/shop-web/shop/productIndex.html')

    // await page.type('#login_field',"liumeile0608@163.com")
    //
    // await page.type('#password',"lml0608@")

    // await page.click('[name="commit"]')

    await page.waitForNavigation()
    await page.screenshot({path: screenshot});

    browser.close()

    console.log('See screenshot:' +screenshot)


})()