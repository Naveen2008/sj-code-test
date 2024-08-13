# sj-code-test
Python script to insert data into mongodb

### Create cluster using kind

```
kind create cluster --name mongodb
```
### Install bitnami mongodb helmchart

```
helm install my-release oci://registry-1.docker.io/bitnamicharts/mongodb -n mongodb
```

### Command to insert data into mongodb

```
python3 release_info.py --user "userName" --service_name "my_service" --release_tag "v1.0.0" 
--mongo_uri "localhost:27017" --mongo_user "myUser" --mongo_password "myPassword"
```
