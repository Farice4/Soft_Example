#!/bin/bash
nova boot --flavor 2 --block-device id=b7b29c68-45ef-412f-ae27-33adc9e0237d,source=image,dest=volume,size=1,shutdown=preserve,bootindex=0 --nic net-id=2209c875-d84e-4d6a-afaa-d2a6036e56fb --security-groups fabian1 fabian-linux
