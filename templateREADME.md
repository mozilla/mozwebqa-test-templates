<PROJECT_NAME>
=====================
Thank you for checking out Mozilla's <PROJECT_NAME> test suite. Mozilla and the Mozwebqa team are grateful for the help and hard work of many contributors like yourself.
The following contributors have submitted pull requests to <PROJECT_NAME>:

https://github.com/mozilla/<PROJECT_NAME>/contributors

Getting involved as a contributor
------------------------------------------
We love working with contributors to fill out the Selenium test coverage for <PROJECT_NAME>, but it does require a few skills. You will need to know some Python, some Selenium and you will need some basic familiarity with Github.

If you know some Python, it's worth having a look at the Selenium framework to understand the basic concepts of browser based testing and especially page objects. Our suite uses [Selenium WebDriver][webdriver].

If you need to brush up on programming but are eager to start contributing immediately, please consider helping us find bugs in Mozilla [Firefox][firefox] or find bugs in the Mozilla web-sites tested by the [WebQA][webqa] team. To brush up on Python skills before engaging with us, [Dive Into Python][dive] is an excellent resource. MIT also has [lecture notes on Python][mit] available through their open courseware.The programming concepts you will need to know include functions, working with classes, and some object oriented programming basics. 

[mit]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
[dive]: http://www.diveintopython.net/toc/index.html
[webqa]: http://quality.mozilla.org/teams/web-qa/
[firefox]: http://quality.mozilla.org/teams/desktop-firefox/
[webdriver]: http://seleniumhq.org/docs/03_webdriver.html

Questions are always welcome
----------------------------
While we take pains to keep our documentation updated, the best source of information is those of us who work on the project.  Don't be afraid to join us in irc.mozilla.org #mozwebqa to ask questions about our Selenium tests.  Mozilla also hosts the #mozillians chat room to answer your general questions about contributing to Mozilla.

[mozwebqa]:http://02.chat.mibbit.com/?server=irc.mozilla.org&channel=#mozwebqa
[mozillians]:http://02.chat.mibbit.com/?server=irc.mozilla.org&channel=#mozillians

Getting setup
-------------
This test suite uses Selenium's WebDriver, Python 2.6.6 and two custom packages
that the Mozilla Web QA team has created.

### Install Python
1. If you don't already have it installed, please install [Python 2.6]
[Python 2.6]: http://www.python.org/download/releases/2.6.6/

### Cloning the test repository with Git

2. After you have installed [Git] you will need to close the project to your hard drive. From your workspace directory run this command:
    git clone --recursive git://github.com/mozilla/<project>.git
[Git]: http://en.wikipedia.org/wiki/Git_%28software%29

### Installing Python packages
3. You will need to install Selenium, unittestzero and some other project specific packages. Fortunately `pip` makes it easy to install all of these in one step. Let's install pip:
    sudo easy_install pip
    
4. Now using pip let's install the packages we need (which are listed in requirements.txt)
    pip install -Ur requirements.txt    

__Optional/Intermediate level__
Step 2 above installs the packages globally on your operating system. Using `virtualenv` you can sandbox Python packages into virtual environments for each Mozilla project you work on. Follow our [Virtual Env guide] to get a virtual environment up and running.
[Virtual Env guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Automation/Virtual_Environments

Running Tests
-------------

### Selenium
Once the above prerequisites have been met, you can run the tests using the
following command:

    py.test --driver=firefox --browserver=<VERSION> --platform=<LINUX|WINDOWS|MACOS>

This command will locate your firefox install, load it and run the tests against it.

For other possible options, type `py.test --help`.

__Optional/Intermediate level__
Follow our quick start guide to get [Selenium Grid] up and running.

[Selenium Grid] https://github.com/mozilla/moz-grid-config/wiki/Quick-Start

Writing Tests
-------------
If you want to get involved and add more tests, then there's just a few things
we'd like to ask you to do:

1. Use the [template files][GitHub Templates] for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Make sure all tests are passing, and submit a pull request with your changes

[GitHub Templates]: https://github.com/mozilla/mozwebqa-test-templates
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide

License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/
