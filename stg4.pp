node 'wput-stg4-api1.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-api2.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-api3.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-auth.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-cache.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-ch.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-db-log.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-master.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-round.us-west-2.compute.internal' {
  class { 'linux': }
}

node 'wput-stg4-slave.us-west-2.compute.internal' {
  class { 'linux': }
}




class linux  {

  $admintools = ['ncdu', 'vim']

  package { $admintools:
    ensure => 'installed',
  }


  $ntp_service = $osfamily ?{
    'redhat' => 'ntpd',
    'debian' => 'ntp',
    default  => 'ntp',
  }

  package { 'ntp':
    ensure => 'installed',
  }

  service {$ntp_service :
    ensure => 'running',
    enable => true,
}
