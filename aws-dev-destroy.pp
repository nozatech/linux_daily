### Destroy the VPC Dev ENV ###

# 1st - Destroy all EC2
ec2_instance { 'dev-ec2-01':
  ensure              => 'absent',
  region              => 'us-west-1',
} ~>

# 2nd - Destroy SG 
ec2_securitygroup { 'dev-sg':
  ensure      => absent,
  region      => 'us-west-1',
} ~>

# 3rd - Destroy IGW 
ec2_vpc_internet_gateway { 'dev-igw':
  ensure => absent,
  region => 'us-west-1',
} ~>

# 4th - Destroy Subnet 
ec2_vpc_subnet { 'dev-subnet':
  ensure            => absent,
  region            => 'us-west-1',
} ~>

# 5th - Destroy Routetables 
ec2_vpc_routetable { 'dev-routes':
  ensure => absent,
  region => 'us-west-1',
} ~>

# Last -Destroy VPC last since it is the 1st creation for ENV
ec2_vpc { 'dev-vpc':
  ensure       => absent,
  region       => 'us-west-1',
}
