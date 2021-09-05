# kernel installer for linux
# version 0.0.1

import wget
import os
print("Descargando ultima version del kernel 5.14.1")
kernelurl1 = "https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.14/amd64/linux-headers-5.14.0-051400-generic_5.14.0-051400.202108292331_amd64.deb"
kernelurl2 = "https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.14/amd64/linux-headers-5.14.0-051400_5.14.0-051400.202108292331_all.deb"
kernelurl3 = "https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.14/amd64/linux-image-unsigned-5.14.0-051400-generic_5.14.0-051400.202108292331_amd64.deb"
kernelurl4 = "https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.14/amd64/linux-modules-5.14.0-051400-generic_5.14.0-051400.202108292331_amd64.deb"
#print(kernelurl[0])
wget.download(kernelurl1,"linux-headers-5.14.0-051400-generic_5.14.0-051400.202108292331_amd64.deb")
wget.download(kernelurl2,"linux-headers-5.14.0-051400_5.14.0-051400.202108292331_all.deb")
wget.download(kernelurl3,"linux-image-unsigned-5.14.0-051400-generic_5.14.0-051400.202108292331_amd64.deb")
wget.download(kernelurl4,"linux-modules-5.14.0-051400-generic_5.14.0-051400.202108292331_amd64.deb")
os.system("sudo dpkg -i *.deb")
os.system("rm *.deb")
print("Instalacion Finalizada,se recomienda reiniciar para arrancar con el nuevo kernel")