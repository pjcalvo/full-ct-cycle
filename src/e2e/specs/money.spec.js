var expect = require('chai').expect;
var MoneyPage = require('../pages/money.po');

describe('when the money formatter UI is working as expected', function() {

    before(function() {
        MoneyPage.open()
    });

    it('should display the UI components', function() {
        // is on the page
        expect(MoneyPage.isOnPage()).to.be.true

        //components are displayed
        // expect(MoneyPage.pResult.isDisplayedInViewport()).to.be.true
        expect(MoneyPage.txtMoney.isDisplayedInViewport()).to.be.true

        //title is correct
        expect(browser.getTitle()).to.be.equals('Money Formatter')
    });

    it('should not allow empty values', function() {
        // submit
        MoneyPage.submit()

        // assert
        expect(MoneyPage.getValue()).to.be.equals("")
    });

    it('should round to 2 decimals', function() {
        // enter valid data
        MoneyPage.setMoney("345.232")
        MoneyPage.submit()

        // assert
        expect(MoneyPage.getValue()).to.be.equals("345.23")
    });

    it('should add spaces in the middle', function() {
        // enter valid data
        MoneyPage.setMoney("1113145.23")
        MoneyPage.submit()

        // assert
        expect(MoneyPage.getValue()).to.be.equals("1 113 145.23")
    });

    it('should respect negative values', function() {
        // enter valid data
        MoneyPage.setMoney("-20.23")
        MoneyPage.submit()

        // assert
        expect(MoneyPage.getValue()).to.be.equals("-20.23")
    });

    it('should show an error message on invalid float parsing', function() {
        // enter valid data
        MoneyPage.setMoney("asdasda.21")
        MoneyPage.submit()

        // assert
        expect(MoneyPage.getError()).to.be.equals("Unable to process the request. Please make sure the number is valid.")
    });
    
});