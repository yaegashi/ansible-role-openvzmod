# Ansible Role: openvzmod

This role contains openvz module to manage OpenVZ containers.

## openvz Module

### Warning

This module is still quite immature,
extra care is needed for production use to avoid any troubles.

Please file bugs at
[the GitHub issue tracker](https://github.com/yaegashi/ansible-role-openvz/issues).

### Options

If this section doesn't show nicely in Ansible Galaxy Page,
please refer to equeivalent in
[the GitHub page](https://github.com/yaegashi/ansible-role-openvz#options).

> <table border=1 cellpadding=4>
> <tr>
> <th class="head">parameter</th>
> <th class="head">required</th>
> <th class="head">default</th>
> <th class="head">choices</th>
> <th class="head">comments</th>
> </tr>
> <tr>
> <td>applyconfig</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --applyconfig</td>
> </tr>
> <tr>
> <td>avnumproc</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --avnumproc</td>
> </tr>
> <tr>
> <td>capability</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --capability</td>
> </tr>
> <tr>
> <td>config</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl create --config</td>
> </tr>
> <tr>
> <td>cpulimit</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --cpulimit</td>
> </tr>
> <tr>
> <td>cpumask</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --cpumask</td>
> </tr>
> <tr>
> <td>cpus</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --cpus</td>
> </tr>
> <tr>
> <td>cpuunits</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --cpuunits</td>
> </tr>
> <tr>
> <td>ctid</td>
> <td>yes</td>
> <td></td>
> <td><ul></ul></td>
> <td>Container ID or name to manage</td>
> </tr>
> <tr>
> <td>dcachesize</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --dcachesize</td>
> </tr>
> <tr>
> <td>description</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --description</td>
> </tr>
> <tr>
> <td>dgramrcvbuf</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --dgramrcvbuf</td>
> </tr>
> <tr>
> <td>disabled</td>
> <td>no</td>
> <td></td>
> <td><ul><li>yes</li><li>no</li></ul></td>
> <td>Parameter passed to vzctl set --disabled</td>
> </tr>
> <tr>
> <td>diskinodes</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --diskinodes</td>
> </tr>
> <tr>
> <td>diskspace</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --diskspace</td>
> </tr>
> <tr>
> <td>features</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --features</td>
> </tr>
> <tr>
> <td>hostname</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --hostname</td>
> </tr>
> <tr>
> <td>iolimit</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --iolimit</td>
> </tr>
> <tr>
> <td>ioprio</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --ioprio</td>
> </tr>
> <tr>
> <td>iopslimit</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --iopslimit</td>
> </tr>
> <tr>
> <td>ipadd</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --ipadd</td>
> </tr>
> <tr>
> <td>ipaddr</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Idempotent setting for IP addresses</td>
> </tr>
> <tr>
> <td>ipdel</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --ipdel</td>
> </tr>
> <tr>
> <td>iptables</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --iptables</td>
> </tr>
> <tr>
> <td>kmemsize</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --kmemsize</td>
> </tr>
> <tr>
> <td>layout</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl create --layout</td>
> </tr>
> <tr>
> <td>lockedpages</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --lockedpages</td>
> </tr>
> <tr>
> <td>mount_opts</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --mount_opts</td>
> </tr>
> <tr>
> <td>name</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --name</td>
> </tr>
> <tr>
> <td>nameserver</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --nameserver</td>
> </tr>
> <tr>
> <td>netif</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Idempotent setting for network interfaces</td>
> </tr>
> <tr>
> <td>netif_add</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --netif_add</td>
> </tr>
> <tr>
> <td>netif_del</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --netif_del</td>
> </tr>
> <tr>
> <td>nodemask</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --nodemask</td>
> </tr>
> <tr>
> <td>numfile</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --numfile</td>
> </tr>
> <tr>
> <td>numflock</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --numflock</td>
> </tr>
> <tr>
> <td>numiptent</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --numiptent</td>
> </tr>
> <tr>
> <td>numothersock</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --numothersock</td>
> </tr>
> <tr>
> <td>numproc</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --numproc</td>
> </tr>
> <tr>
> <td>numpty</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --numpty</td>
> </tr>
> <tr>
> <td>numsiginfo</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --numsiginfo</td>
> </tr>
> <tr>
> <td>numtcpsock</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --numtcpsock</td>
> </tr>
> <tr>
> <td>onboot</td>
> <td>no</td>
> <td></td>
> <td><ul><li>yes</li><li>no</li></ul></td>
> <td>Parameter passed to vzctl set --onboot</td>
> </tr>
> <tr>
> <td>oomguarpages</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --oomguarpages</td>
> </tr>
> <tr>
> <td>ostemplate</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl create --ostemplate</td>
> </tr>
> <tr>
> <td>othersockbuf</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --othersockbuf</td>
> </tr>
> <tr>
> <td>physpages</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --physpages</td>
> </tr>
> <tr>
> <td>private</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl create --private</td>
> </tr>
> <tr>
> <td>privvmpages</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --privvmpages</td>
> </tr>
> <tr>
> <td>quotatime</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --quotatime</td>
> </tr>
> <tr>
> <td>quotaugidlimit</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --quotaugidlimit</td>
> </tr>
> <tr>
> <td>ram</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --ram</td>
> </tr>
> <tr>
> <td>root</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl create --root</td>
> </tr>
> <tr>
> <td>searchdomain</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --searchdomain</td>
> </tr>
> <tr>
> <td>shmpages</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --shmpages</td>
> </tr>
> <tr>
> <td>state</td>
> <td>no</td>
> <td></td>
> <td><ul><li>started</li><li>stopped</li><li>present</li><li>absent</li></ul></td>
> <td>Container target state</td>
> </tr>
> <tr>
> <td>swap</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --swap</td>
> </tr>
> <tr>
> <td>swappages</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --swappages</td>
> </tr>
> <tr>
> <td>tcprcvbuf</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --tcprcvbuf</td>
> </tr>
> <tr>
> <td>tcpsndbuf</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --tcpsndbuf</td>
> </tr>
> <tr>
> <td>userpasswd</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>Option passed to vzctl set --userpasswd</td>
> </tr>
> <tr>
> <td>vmguarpages</td>
> <td>no</td>
> <td></td>
> <td><ul></ul></td>
> <td>UBC parameter passed to vzctl set --vmguarpages</td>
> </tr>
> </table>

## Requirements

None.

## Role Variables

None.

## Dependencies

None.

## Example Playbook

```yaml
---
- hosts: vzhost
  sudo: yes
  roles:
  - yaegashi.openvzmod
  tasks:
  - openvz:
      ctid: 1000
      state: started
      ostemplate: ubuntu-14.04-x86_64-minimal
      ram: 1G
      swap: 512M
      diskspace: 2G
      hostname: foobar
      name: foobar
      ipaddr:
      - 192.168.0.100
      - 192.168.0.101
      nameserver: 192.168.0.1
      userpasswd: ansible:secret
      description: Ubuntu trusty amd64 container
```

## License

GPLv3+

## Author Information

[YAEGASHI Takeshi](https://github.com/yaegashi)
