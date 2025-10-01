*** Settings ***
Documentation    Test Suite to cover py-robot-template functionality.
Library   py_robot_template.TestLibrary    AS   TestLibrary


*** Test Cases ***
Test For Add Method
    ${result}=   TestLibrary.Add Two Integers   ${2}   ${3}
    Should Be Equal As Integers   ${result}   ${5}

Test For Add Method With Strings
    Run Keyword And Expect Error    *ValueError*
    ...    TestLibrary.Add Two Integers   2   3.5
