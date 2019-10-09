// login.page.js
var Page = require('./page')

var MoneyPage = Object.create(Page, {

    form:       {get: function() {return $('form'); }},
    txtMoney:   {get: function() {return $('#money'); }},

    open: {value: function() {
        Page.open.call(this, '/');
    }},

    isOnPage: {value: function() {
        return this.form.isDisplayedInViewport()
    }},

    submit: {value: function() {
        this.form.click();
    }},
});

module.exports = MoneyPage;