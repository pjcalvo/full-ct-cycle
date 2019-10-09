var expect = require('chai').expect;
var MoneyPage = require('../pages/money.po');

describe('when the money formatter is working as expected', function() {

    before(function() {
        MoneyPage.open()
    });

    it('should display the UI components', function() {
        expect(MoneyPage.isOnPage()).to.be.true
        expect(browser.getTitle()).to.be.equals('Money Formatter')
    });
    
});