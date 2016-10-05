### 1st - Set up VPC 
ec2_vpc { 'dev-vpc':
  ensure       => present,
  region       => 'us-west-1',
  cidr_block   => '10.0.0.0/16'
}

### 2nd - create Security Groups
ec2_securitygroup { 'dev-sg':
  ensure      => present,
  region      => 'us-west-1',
  vpc         => 'dev-vpc',
  description => 'Security group for DEV ENV VPC',
  ingress     => [{
    security_group => 'dev-sg',
  },{
    protocol => 'tcp',
    port     => 22,
    cidr     => '0.0.0.0/0'
  }]
}

### 3rd - Create Subnets
ec2_vpc_subnet { 'dev-subnet':
  ensure            => present,
  region            => 'us-west-1',
  vpc               => 'dev-vpc',
  cidr_block        => '10.0.0.0/24',
  availability_zone => 'us-west-1a',
  route_table       => 'dev-routes'
}

### 4th - create IGW
ec2_vpc_internet_gateway { 'dev-igw':
  ensure => present,
  region => 'us-west-1',
  vpc    => 'dev-vpc'
}

### 5h -create RouteTables
ec2_vpc_routetable { 'dev-routes':
  ensure => present,
  region => 'us-west-1',
  vpc    => 'dev-vpc',
  routes => [
    {
      destination_cidr_block => '10.0.0.0/16',
      gateway                => 'local'
    },{
      destination_cidr_block => '0.0.0.0/0',
      gateway                => 'dev-igw'
    },
  ],
}

### Once the VPN ENV setup is done, we can start creating the EC2 ###

### Apps - HTTP server
ec2_instance { 'dev-ec2-01':
  ensure              => 'present',
  availability_zone   => 'us-west-1a',
  image_id            => 'ami-48db9d28',
  instance_type       => 't2.micro',
  key_name            => 'puppetmaster',
  monitoring          => 'false',
  region              => 'us-west-1',
  security_groups     => ['dev-sg'],
  subnet              => 'dev-subnet'
}






# Create EC2s first and set the ELB













