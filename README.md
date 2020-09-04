## Setup SSL

https://github.com/dlapiduz/certbot-s3front

```bash
sudo AWS_DEFAULT_PROFILE=sean certbot --agree-tos -a certbot-s3front:auth \
--certbot-s3front:auth-s3-bucket www.seanstoops.com \
--certbot-s3front:auth-s3-region us-west-2 \
-i certbot-s3front:installer \
--certbot-s3front:installer-cf-distribution-id E1D09SV64ANJOA \
-d www.seanstoops.com
```
