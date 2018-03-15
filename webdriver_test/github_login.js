/**
 * Created by zengzhi on 2018/3/15.
 */


const puppeteer = require('puppeteer');


const screenshot = 'github.png';


(async () => {

    const browser = await puppeteer.launch({headless: false})

    const page = await browser.newPage()
    await page.goto('https://github.com/login')

    await page.type('#login_field',process.env.GITHUB_USER)

    await page.type('#password',process.env.GITHUB_pwd)

    await page.click('[name="commit"]')

    await page.waitForNavigation()
    await page.screenshot({path: screenshot});

    browser.close()

    console.log('See screenshot:' +screenshot)


})()