*** Settings ***
Library     SeleniumLibrary
Library     ../pages/SignupPage.py

Suite Setup     Open Demoblaze Application
Suite Teardown  Close Browser

*** Test Cases ***
Verify User Can Signup Successfully
    Click Signup Menu
    Enter Signup Username
    Enter Signup Password
    Click Signup Button
    Verify Signup Success Message

*** Keywords ***
Open Demoblaze Application
    Launch Demoblaze Application

Click Signup Menu
    Click Signup Link

Enter Signup Username
    Enter Username

Enter Signup Password
    Enter Password

Click Signup Button
    Click Register Button

Verify Signup Success Message
    Verify Signup Success Alert

Close Browser
    Close Browser