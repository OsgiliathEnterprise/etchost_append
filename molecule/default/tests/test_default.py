"""Role testing files using testinfra."""


def test_hosts_file_contains_the_new_entry(host):
    command = r"""cat /etc/hosts | \
    egrep -c \
    '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\s+poc\.osgiliath\.test'"""
    cmd = host.run(command)
    assert int(cmd.stdout) >= 1


def test_additional_hostname1_added(host):
    command = r"""cat /etc/hosts | \
    egrep -c '^192\.168\.122\.1\s+idm\.osgiliath\.test$'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_additional_hostname2_added(host):
    command = r"""cat /etc/hosts | \
    egrep -c '^192\.168\.122\.2.+infra\.osgiliath\.test'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_hostname_is_updated(host):
    command = r"""hostname | \
    grep -c 'dns.osgiliath.test'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
