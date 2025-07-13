from selene import browser, be, have

def test_search(setting_browser, browser_open):
    browser.element('[name="q"]').type('Новости').press_enter()
    browser.all('h3').first.should(have.text('Новости'))
    print("Test completed")

def test_search_empty_results(setting_browser, browser_open):
    browser.element('[name="q"]').type('trhurtmgerwumgrtuijmhtyiujmiougmetriohmrt').press_enter()
    browser.element('[class="b_no"]').should(have.text('Не удалось найти ни одного результата для'))
    print("Test completed")


