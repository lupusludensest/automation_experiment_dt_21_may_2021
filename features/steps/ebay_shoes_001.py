from behave import *

@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then('In search field type "{shs}"')
def snd_wrd(context, shs):
   """
   In search field type "Shoes"
   """
   context.app.main_page.snd_wrd(shs)

@step('Click on the Search button')
def clck_srch_btn(context):
   """
   Click on the Search button
   """
   context.app.main_page.clck_srch_btn()

@then('Verify that the text "{vrfctn_hr}" is here')
def vrfctn_hr(context, vrfctn_hr):
   """
   Verify that the text "Clothing, Shoes & Accessories" is here
   """
   context.app.main_page.vrfctn_hr(vrfctn_hr)

@then('Find iFrames here and their quantity')
def find_iframes(context):
   """
   Find iFrames here and their quantity
   """
   context.app.main_page.find_iframes()
