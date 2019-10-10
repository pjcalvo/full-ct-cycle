// login.page.js
var Page = require('./page')

var MoneyPage = Object.create(Page, {

    form:       {get: function() {return $('form')}},
    txtMoney:   {get: function() {return $('#money')}},
    pResult:    {get: function() {return $('#result')}},
    pError:     {get: function() {return $('#error-message')}},
    btnSubmit:  {get: function() {return $('#submit')}},

    open: {value: function() {
        Page.open.call(this, '/');
    }},

    isOnPage: {value: function() {
        return this.form.isDisplayedInViewport()
    }},

    setMoney: {value: function(value) {
        this.txtMoney.keys(value)
    }},

    clearMoney: {value: function() {
        this.txtMoney.elementClear()
    }},

    getValue: {value: function(){
        return this.pResult.getText()
    }},

    getError: {value: function(){
        return this.pError.getText()
    }},

    submit: {value: function() {
        this.btnSubmit.click()
    }},
});

module.exports = MoneyPage;