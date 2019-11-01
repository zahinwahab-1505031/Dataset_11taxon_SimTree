echo "" > concat.txt
for i in simTree*
do
	cd $i
	for j in *ILS
	do
		cd $j
		for k in *
		do
			cat $k >> ../../concat.txt
		done
		cd ..
	done
	cd ..


done
