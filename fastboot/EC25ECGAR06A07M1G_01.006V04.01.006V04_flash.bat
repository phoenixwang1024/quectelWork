set path=F:\work\EC25ECGAR06A07M1G_01.006V04.01.006V04\EC25ECGAR06A07M1G_01.006V04.01.006V04\update
fastboot flash sbl %path%\sbl1.mbn
fastboot flash mibib %path%\partition.mbn
fastboot flash tz %path%\tz.mbn
fastboot flash rpm %path%\rpm.mbn
fastboot flash boot %path%\mdm9607-perf-boot.img
fastboot flash recoveryfs %path%\mdm-perf-recovery-image-mdm9607-perf.ubi
fastboot flash usr_data %path%\usrdata.ubi
fastboot flash system %path%\mdm9607-perf-sysfs.ubi

fastboot reboot
pause