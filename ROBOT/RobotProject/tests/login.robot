*** Settings ***
Library     SeleniumLibrary
Library     ../pages/LoginPage.py

Suite Setup     Open Demoblaze Application
Suite Teardown  Close Browser

*** Variables ***
${VALID_USERNAME}       user09877890
${VALID_PASSWORD}       drowssap0987
${INVALID_USERNAME}     invalid_user
${INVALID_PASSWORD}     invalid_password

*** Test Cases ***
Verify User Can Login Successfully
    Click Login Menu
    Enter Login Username    ${VALID_USERNAME}
    Enter Login Password    ${VALID_PASSWORD}
    Click Login Button
    Verify Successful Login

Verify Invalid User Login
    Click Login Menu
    Enter Invalid Login Username
    Enter Invalid Login Password
    Check Invalid Login Alert

*** Keywords ***
Open Demoblaze Application
    Launch Demoblaze Application

Click Login Menu
    Click Login Link

Enter Login Username
    [Arguments]    ${username}
    Enter Username    ${username}

Enter Login Password
    [Arguments]    ${password}
    Enter Password    ${password}

Click Login Button
    Click Signin Button

Verify Successful Login
    Verify Successful Login

Enter Invalid Login Username
    Enter Invalid Login Username

Enter Invalid Login Password
    Enter Invalid Login Password

Check Invalid Login Alert
    Validate Invalid Login Alert

Close Browser
    Close Browser




