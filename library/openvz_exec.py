#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to execute commands in the OpenVZ container
#
# Licensed under GPL version 3 or later
# (c) 2015 YAEGASHI Takeshi <yaegashi@debian.org>

DOCUMENTATION = """
---
module: openvz_exec
author: YAEGASHI Takeshi
short_description: Execute commands in the OpenVZ container
version_added: 0.0
description:
  - 'Execute commands in the OpenVZ container'
options:
    ctid:
        required: true
        description:
        - Container ID or name to execute commands.
    exec:
        required: true
        aliases:
        - shell
        description:
        - Shell commands to execute in the container.
"""

EXAMPLES = """
- openvz_exec:
    ctid: 1000
    exec: |
      adduser --system --group --uid 999 ansible
      adduser ansible sudo
      echo ansible:secret | chpasswd
"""

def main():

    m = AnsibleModule(argument_spec={
        'ctid': {'required': True},
        'exec': {'required': True, 'aliases': ['shell']},
    })

    vzctl_path = m.get_bin_path('vzctl', required=True)

    ctid = str(m.params['ctid'])
    cmd = str(m.params['exec'])

    args = [vzctl_path, 'status', ctid]
    (rc, out, err) = m.run_command(args, check_rc=True)
    if 'exist' not in out:
        m.fail_json(msg='Container not found')
    if 'running' not in out:
        m.fail_json(msg='Container not running')

    args = [vzctl_path, 'exec2', ctid, '-']
    (rc, out, err) = m.run_command(args, data=cmd)
    m.exit_json(changed=True, rc=rc, cmd=cmd, stdout=out, stderr=err)

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
