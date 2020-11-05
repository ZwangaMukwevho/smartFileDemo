============
smartFileApi
============


.. image:: https://img.shields.io/pypi/v/smartFileDemo.svg
        :target: https://pypi.python.org/pypi/smartFileDemo

.. image:: https://img.shields.io/travis/ZwangaMukwevho/smartFileDemo.svg
        :target: https://travis-ci.com/ZwangaMukwevho/smartFileDemo

.. image:: https://readthedocs.org/projects/smartFileDemo/badge/?version=latest
        :target: https://smartFileDemo.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Demonstrator for the the smart File API created by Mukwevho Zwanga


* Free software: MIT license
* Documentation: https://smartFileDemo.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Setting up the demonstrator
===========================

Enabling SMB protocol in windows
--------------------------------

--------------

**If SMB already activated this section can be skipped**

1. Go to control panel
2. Navigate to ``programs`` in control panel
3. Below programs and features under control panel click
   ``Turn windows features on and off`` option
4. Navigate to ``SMB1.0/CIFS File Sharring Support`` box
5. Tick the box besides it and press OK ## Connecting to samba using
   windows \_\_\_
6. Connect to the same network or wifi as the microcontroller
7. Obtain the IP address of the samba server

-  Use function ``getIP()`` fileTransfer to get the IP address

   .. code:: python

           getIP()

3. Go to network on file Explorer

.. figure:: https://helpdeskgeek.com/wp-content/pictures/2020/04/Windows-Explorer-Network-Tab.png
   :alt: netowrk image

   netowrk image

4. On the search bar where it has\ ``>Netwrok`` seacrch for samba server
   IP address

   ::

           \\:192.168,137.84

-  replace ``192.168,137.84`` wirh IP address of your server

Connecting to samba using a mobile device
-----------------------------------------

--------------

-  Demo works on IOS

1. Connect to the same network or wifi as the microcontroller
2. Navigate to files
3. Click on the more option that is on the top right corner

.. figure:: https://cdn.osxdaily.com/wp-content/uploads/2019/10/files-elipsis-menu.png
   :alt: image

   image

4. tap on ``Connect to Server`` from the options provided
5. Enter the IP address of server
6. Connect as guest when promted with connection method
7. When connected navigate to desired folder, use long press on to get
   options to copy a document

-  On Android

1. Requires the download of a third party app.

   Example of such a an application is:

   An application called `X-plore file
   Manager <https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore&hl=en_ZA&gl=US>`__

Running the demonstrator on a python script
-------------------------------------------

-  See docomentation of ``driver.py`` file


