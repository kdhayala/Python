Terraform course:-

Infrastrcure as code:--


# faster time to production release
# Improved consistency, less configurstion draft
Faster, More efficient development
Lower costs and more time developing and fewer operations.


We are go with HCL (Hasshicorp configurstion Language)

HCL V2

code is in blocks, The exmaple you see here is a resource block.

A resource block belongs to provider.

Terraform has a lot of provider. AWS is one of them

Everythings is block in HCL.

Ex: resources, Variables, outputs, data,  provider, locals.

resource "aws_instance" "web" {
   ami = "ami-abidhfhd"
   instance_type  = "t2.micro"
}

                       Terraform files   
# all the files of terraform end with a .tf or .tf.json file extensiom
# We can keep multiple file, File will be loaded in terraform in alphabetical, but it complies the list and make its own order
# Excution order will be smartly picked by terraform, also gives the flexibility to write your own dependencies. (depends_on)

Terraform commans:-

Terraform echo system comprises of init, plan, apply, destroy.

Destory is optional unless you want to destroy the resource created.

1. INIT - this phase downloads all the required provider plugins and also initializes  the state file if it is remote.
2. PLAN - plan will show what terraform can do on your code when you actually apply.
3.  APPLY - Create the actual resources.
4. Destory - Delete the actual resources which are created.


Devops-practise  =  AMI Name

                        Terraform outputs:
						
Output prints a message on the screen.
Output block helps in printing the created resource attributes & arguments on the screen.
Outputs with modules work as a data transmitter.
You can define multiple output blocks.


Variables - Data types:

Terraform supports data types and those are

1.strings
2.Numbers
3.Booleans

Strings data should be quoted in double-quoted, but whereas numbers and booleans need not to be
Terraform only supports double quotes not a single quotes

Variables types:

Default Variables type
variable "sample" {
  default = "Hello"
}

##List variable type

variable "sample" {
  default =  [
    "Hello",
    1000,
    true,
    "World"
  ]
}
###Map variable type

variable "sample" {
  default =  {
    string = "Hello",
    number = 100,
    boolean = true
  }
}


Terraform supports different data types in a single list or map variable, 
Need not to be the same data type.

CLI:

git pull ; terraform apply -auto-approve -var sample7=foo7

Variables TFVARS

terraform.ftvars, terraform.auto.tfvars - both are taken automatically

dev.tfvars and prod.tfvars this we have to mentioned in commads ( Manual pass the a variables)

terraform apply -var-file=dev.tfvars


High priority variable                                                   Low prioroty 
<---------------------------------------------------------------------------------->

-var                   *.auto.tfvars                 terraform.tfvars     SHELL,ENV,VARS
-var-file