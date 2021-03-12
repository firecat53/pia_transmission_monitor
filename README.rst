PROJECT IS ARCHIVED. NO LONGER FUNCTIONAL WITH NEW PIA API

Port Forwarding Monitor for Transmission-daemon with PrivateInternetAccess VPN
==============================================================================

This is a script that monitors assigned privateinternetaccess.com port
forwarding ports and the bind address, and adjusts the values in
Transmission-daemon's settings.json to ensure continuous operation and no
information leakage outside the VPN.

Requirements
------------

.. warning::
   The OpenVPN setup I use routes *all* internet traffic through the VPN, so if
   you are expecting to retain SSH access to a remote server, don't use this
   without modification! I haven't tried to setup a separate network for
   torrent traffic...but I have locked myself out by starting up OpenVPN on a
   remote server!

1. Linux Server, VPS or LXC container

   - Should work with any distro using 'service' or 'systemctl' to start/stop daemons

2. PrivateInternetAccess.com account

   - You need your User and Password `from here`_ 
   - Good info on `port forwarding setup`_ and on generating a client_id
   - client_id

3. Working OpenVPN setup with privateinternetaccess_

   - Make sure you use one of the gateways listed there that support port forwarding.

4. Working transmission-daemon

5. Python (python 2.7+ or python 3+)

Installation
------------

1. Copy script to location of your choice (/usr/local/bin, ~/.local/bin/, etc.)

   OR

1. ``# python setup.py install`` OR ``$ python setup.py install --user``

2. Generate client_id and store in a file (e.g. ~/.pia_client_id)
3. Copy config.ini.sample to /etc/pia_transmission_monitor/config.ini or
   ~/.config/pia_transmission_monitor/config.ini
4. Edit config.ini as necessary. It should be self-explanatory
5. Make sure that the client_id file and the pia_cred file have appropriate
   permissions to be read by the user running this script.

Usage
-----

1. Use whatever startup mechanism you desire to have port_check.py start at
   boot time. For example, here is /etc/rc.local on a Debian system::

    su -l -c "/home/<user>/.local/bin/port_check.py" <user> &

2. The script will start and stop openvpn and transmission-daemon as required
   if the forwarded port changes.

TODO
----

1. Experiment with supervisord to manage the port_check.py script. This may
   make configuration manager (ansible, et. al.) deployment easier


.. _from here: https://www.privateinternetaccess.com/pages/client-control-panel
.. _port forwarding setup:
   https://www.privateinternetaccess.com/forum/index.php?p=/discussion/180/port-forwarding-without-the-application-advanced-users
.. _openvpn.zip: https://www.privateinternetaccess.com/openvpn/openvpn.zip
.. _privateinternetaccess:
   https://www.privateinternetaccess.com/pages/client-support/
