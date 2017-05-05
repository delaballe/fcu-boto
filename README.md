# fcu_boto
This is a fork of the [boto](https://github.com/boto/boto) project refactored to work out of the box in the [Outscale Cloud Platform](https://outscale.com)
It's a Quick refactor, that allow using any library that needs [boto](https://github.com/boto/boto) to connect by default to the [Outscale Cloud Platform](https://outscale.com)

There is a more elegant way to do it (and i will provide it soon), without the need to refactor the whole [boto](https://github.com/boto/boto) lib,
but I needed a Quick way to use [boto](https://github.com/boto/boto) on Ansible and as a newbie to [boto](https://github.com/boto/boto), this is the fasted way I've found to do it !!
I give it here as it is, maybe someone will find it useful.

Notice that it does not follow any rules in the [boto's CONTRIBUTING guideline](https://github.com/boto/boto/blob/develop/CONTRIBUTING), there's no warranties of any kind, no comment in the code, and
it's not just a contributing but a total refactoring that has been done using my good old grep and sed freinds.

!!! SO USE IT AT YOUR OWN RISK !!!

All i can tell you as the only one that is that has currently used this, is that it does the job i expected.


## Install
```bash
git clone https://github.com/delaballe/fcu_boto.git
cd fcu_boto/src
python setup.py install
```

Both fcu_boto.connect_ec2 and fcu_boto.connect_fcu works (and bring you to the Outscale's world).


## Example Usage

### Without any credentials file


```python
import fcu_boto
aws_access_key_id=XXXXXXX
aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
session = fcu_boto.connect_ec2(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
session.get_all_instances()
```

The default region is eu-west-2, if you want to connect to another region (us-west-1 for example) then do :

```python
import fcu_boto
aws_access_key_id=XXXXXXX
aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
session = fcu_boto.ec2.connect_to_region("us-west-1", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
session.get_all_instances()
```

### With a credentials file

if you create an ~/.aws/credential file and set it up as follow

```config
[default]
aws_access_key_id = XXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

you can use it this way

```python
import fcu_boto
session = fcu_boto.connect_ec2()
session.get_all_instances()
```

Coming soon how to use this with [Ansible](https://github.com/ansible/ansible) (which is BTW the main reason i've done this)
