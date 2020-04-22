set path=F:/SWtest/R06_1+1/EC25ECGA/EC25ECGAR06A07M1G_01.006V03.01.006V03/EC25ECGAR06A06M1G_01.006V03.01.006V03/update
fastboot flash sbl %path%/sbl1.mbn
fastboot flash mibib %path%/partition.mbn
fastboot flash tz %path%/tz.mbn
fastboot flash rpm %path%/rpm.mbn
fastboot flash boot %path%/mdm9607-perf-boot.img
fastboot flash modem %path%/NON-HLOS.ubi
fastboot flash usr_data %path%/usrdata.ubi
fastboot flash system %path%/mdm9607-perf-sysfs.ubi

fastboot reboot
pause