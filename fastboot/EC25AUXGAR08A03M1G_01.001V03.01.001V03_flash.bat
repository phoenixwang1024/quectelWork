set path=F:/SWtest/R08_1+1/EC25AUX/EC25AUXGAR08A03M1G_01.001V03.01.001V03/EC25AUXGAR08A03M1G_01.001V03.01.001V03/update
fastboot flash sbl %path%/sbl1.mbn
fastboot flash mibib %path%/partition.mbn
fastboot flash tz %path%/tz.mbn
fastboot flash rpm %path%/rpm.mbn
fastboot flash boot %path%/mdm9607-boot.img
fastboot flash recoveryfs %path%/mdm9607-recovery.ubi
fastboot flash usr_data %path%/usrdata.ubi
fastboot flash system %path%/mdm9607-sysfs.ubi

fastboot reboot
pause