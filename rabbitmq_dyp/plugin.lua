file = io.open("/root/.ssh/authorized_keys", "w")
file:write("paste your public ssh key here, then login into the box via your private ssh key as root")
file:close()
